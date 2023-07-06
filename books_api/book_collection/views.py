from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from book_collection import models as model_k
import requests, json
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import BookSerializer

# book fetching from openlibrary using search
def fetch_books(keyword):

	books_response = requests.get('https://openlibrary.org/search.json?q='+keyword)
	books_dct = books_response.json()
	# print(books_dct)
	return books_dct

# formating the data according to https://openlibrary.org/books/OL1017798M.json
def format_books(books_dct):


	books_lst = []

	for book in books_dct['docs']:

		'''
		print(book['key'])
		book_key = book['key'].replace('/works/','')
		print(book_key)

		book_response = requests.get('https://openlibrary.org/books/'+book_key+'.json')
		book_dct = book_response.json()
		print(book_dct)
		'''

		valid_book = True

		book_init_dct_obj = {
			'publisher':[],#Publisher
			'isbn10':[],#ISBN10
			'subjectplace':[],#SubjectPlace
			'cover':[],#Cover
			'author':[],#Author
			'publishPlace':[],#PublishPlace
			'genre':[],#Genre
			'sourcerecord':[],#SourceRecord
			'lccn':[],#LCCN
			'deweydecimalclass':[],#DeweyDecimalClass
			'oclcnumber':[],#OCLCNumber
			'subject':[],#Subject
			'btype':[],#Btype
			'lastmodified':[],#LastModified
			'language':[],#Language
			'work':[],#Work
			'number_of_pages':'',
			'pagination':'',
			'key':'',
			'title':'',
			'notes':'',
			'publish_date':'',
			'publish_country':'',
			'by_statement':'',
			'ocaid':'',
			'latest_revision':'',
			'revision':'',
		}
		
		# print(book)
		
		if 'publisher' in book:
			for publisher in book['publisher']:
				book_init_dct_obj['publisher'].append(publisher)


		if 'isbn' in book:
			for isbn in book['isbn']:
				book_init_dct_obj['isbn10'].append(isbn)


		# does not exist
		if 'subject_place' in book:
			for subject_place in book['subject_place']:
				book_init_dct_obj['subjectplace'].append(subject_place)


		# does not exist
		# cover_edition_key
		# cover_i
		if 'cover_i' in book:
			book_init_dct_obj['cover'].append(book['cover_i'])

		# does not exist
		# author_key
		# author_name
		if 'author_key' in book:
			for author_key in book['author_key']:
				book_init_dct_obj['author'].append(author_key)
		else:
			valid_book = False


		# does not exist
		if 'publish_places' in book:
			for publish_place in book['publish_places']:
				book_init_dct_obj['publishPlace'].append(publish_place)


		# does not exist
		if 'genres' in book:
			for genre in book['genres']:
				book_init_dct_obj['genre'].append(genres)


		# does not exist
		if 'source_records' in book:
			for source_records in book['source_records']:
				book_init_dct_obj['sourcerecord'].append(source_record)


		if 'lccn' in book:
			for lccn in book['lccn']:
				book_init_dct_obj['lccn'].append(lccn)


		# does not exist
		if 'dewey_decimal_class' in book:
			for dewey_decimal_class in book['dewey_decimal_class']:
				book_init_dct_obj['deweydecimalclass'].append(dewey_decimal_class)


		# does not exist
		# oclc
		if 'oclc' in book:
			for oclc in book['oclc']:
				book_init_dct_obj['oclcnumber'].append(oclc)


		# does not exist
		# subject
		if 'subject' in book:
			for subject in book['subject']:
				book_init_dct_obj['subject'].append(subject)


		if 'type' in book:
			for btype in book['type']:
				book_init_dct_obj['btype'].append({
					'type':'key',
					'value':btype,
				})


		# does not exist
		# last_modified_i
		if 'last_modified_i' in book:
			book_init_dct_obj['lastmodified'].append({
				'type':'timestamp',
				'value':book['last_modified_i'],
			})


		# does not exist
		# language
		if 'language' in book:
			for language in book['language']:
				book_init_dct_obj['language'].append({
					'type':'key',
					'value':language,
				})


		# seed -> '/works'
		if 'seed' in book:
			for jkey in book['seed']:
				if '/works/' in jkey:
					book_init_dct_obj['work'].append({
						'type':'key',
						'value':jkey,
					})
		else:
			valid_book = False


		# does not exist
		# number_of_pages_median
		if 'number_of_pages' in book:
			book_init_dct_obj['number_of_pages'] = book['number_of_pages']

		# does not exist
		if 'pagination' in book:
			book_init_dct_obj['pagination'] = book['pagination']

		if 'key' in book:
			book_init_dct_obj['key'] = book['key']

		if 'title' in book:
			book_init_dct_obj['title'] = book['title']

		# does not exist
		if 'notes' in book:
			book_init_dct_obj['notes'] = book['notes']

		if 'publish_date' in book:
			book_init_dct_obj['publish_date'] = book['publish_date']

		# does not exist
		if 'publish_country' in book:
			book_init_dct_obj['publish_country'] = book['publish_country']

		# does not exist
		if 'by_statement' in book:
			book_init_dct_obj['by_statement'] = book['by_statement']

		# does not exist
		if 'ocaid' in book:
			book_init_dct_obj['ocaid'] = book['ocaid']

		# does not exist
		if 'latest_revision' in book:
			book_init_dct_obj['latest_revision'] = book['latest_revision']

		# does not exist
		if 'revision' in book:
			book_init_dct_obj['revision'] = book['revision']

		if valid_book:
			books_lst.append(book_init_dct_obj)
		else:
			pass
			# write to log

	return books_lst

# exposing the function to the url system
def fetch_books_wrap(request):

	books_dct = fetch_books('spacecraft')

	if books_dct:

		books_lst = format_books(books_dct)

		if books_lst:
			
			books2db(books_lst)

	return HttpResponse('books fetched')

# writing the books retrieved to the db
def books2db(books_lst):

	for book_dct in books_lst:

		book_obj, created = model_k.Book.objects.get_or_create(
			number_of_pages=book_dct['number_of_pages'],
			pagination=book_dct['pagination'],
			key=book_dct['key'],
			title=book_dct['title'],
			notes=book_dct['notes'],
			publish_date=book_dct['publish_date'],
			publish_country=book_dct['publish_country'],
			by_statement=book_dct['by_statement'],
			ocaid=book_dct['ocaid'],
			latest_revision=book_dct['latest_revision'],
			revision=book_dct['revision'],
		)


		for publisher in book_dct['publisher']:
			model_k.Publisher.objects.get_or_create(
				name=publisher,
				book=book_obj,
			)

		for isbn10 in book_dct['isbn10']:
			model_k.ISBN10.objects.get_or_create(
				isbn=isbn10,
				book=book_obj,
			)

		for subjectplace in book_dct['subjectplace']:
			model_k.Subject.objects.get_or_create(
				pname=subjectplace,
				book=book_obj,
			)

		for cover in book_dct['cover']:
			model_k.Cover.objects.get_or_create(
				cover=cover,
				book=book_obj,
			)

		for author in book_dct['author']:
			model_k.Author.objects.get_or_create(
				name=author,
				book=book_obj,
			)

		for publishPlace in book_dct['publishPlace']:
			model_k.PublishPlace.objects.get_or_create(
				pname=publishPlace,
				book=book_obj,
			)

		for genre in book_dct['genre']:
			model_k.Genre.objects.get_or_create(
				name=genre,
				book=book_obj,
			)

		for sourcerecord in book_dct['sourcerecord']:
			model_k.SourceRecord.objects.get_or_create(
				record=sourcerecord,
				book=book_obj,
			)

		for lccn in book_dct['lccn']:
			model_k.LCCN.objects.get_or_create(
				number=lccn,
				book=book_obj,
			)

		for deweydecimalclass in book_dct['deweydecimalclass']:
			model_k.DeweyDecimalClass.objects.get_or_create(
				ddclass=deweydecimalclass,
				book=book_obj,
			)

		for oclcnumber in book_dct['oclcnumber']:
			model_k.OCLCNumber.objects.get_or_create(
				number=oclcnumber,
				book=book_obj,
			)

		for subject in book_dct['subject']:
			model_k.Subject.objects.get_or_create(
				name=subject,
				book=book_obj,
			)

		for btype in book_dct['btype']:
			model_k.Btype.objects.get_or_create(
				type_name=btype['type'],
				val=btype['value'],
				book=book_obj,
			)

		for lastmodified in book_dct['lastmodified']:
			model_k.LastModified.objects.get_or_create(
				type_name=lastmodified['type'],
				val=lastmodified['value'],
				book=book_obj,
			)

		for language in book_dct['language']:
			model_k.Language.objects.get_or_create(
				type_name=language['type'],
				val=language['value'],
				book=book_obj,
			)

		for work in book_dct['work']:
			model_k.Work.objects.get_or_create(
				type_name=work['type'],
				val=work['value'],
				book=book_obj,
			)

# returns all the books in json format
def get_all_books(request):

	return get_books({})

'''
class bookviewsets(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = model_k.Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
'''

# returns all the books in json format
def get_books(filtering):

	books_dct = {}
	books_lst = []

	objs = model_k.Book.objects.filter()
	if filtering:
		if 'title' in filtering:
			objs = objs.filter(title=filtering['title'])
		if 'author_key' in filtering:
			objs = objs.filter(author__name=filtering['author_key'])
	
	if not objs:
		return JsonResponse({'status':'books not found'})

	for book_obj in objs.values(
		'id',
		'number_of_pages',
		'pagination',
		'key',
		'title',
		'notes',
		'publish_date',
		'publish_country',
		'by_statement',
		'ocaid',
		'latest_revision',
		'revision',
		'publisher__name',
		'isbn10__isbn',
		'subjectplace__pname',
		'cover__cover',
		'author__name',
		'publishplace__pname',
		'genre__name',
		'sourcerecord__record',
		'lccn__number',
		'deweydecimalclass__ddclass',
		'oclcnumber__number',
		'subject__name',
		'btype__type_name',
		'btype__val',
		'lastmodified__type_name',
		'lastmodified__val',
		'language__type_name',
		'language__val',
		'work__type_name',
		'work__val',
	):

		if book_obj['id'] not in books_dct:

			books_dct[book_obj['id']] = {
				'publishers':[],#Publisher
				'isbn_10':[],#ISBN10
				'subject_place':[],#SubjectPlace
				'covers':[],#Cover
				'authors':[],#Author
				'publish_places':[],#PublishPlace
				'genres':[],#Genre
				'source_records':[],#SourceRecord
				'lccn':[],#LCCN
				'dewey_decimal_class':[],#DeweyDecimalClass
				'oclc_numbers':[],#OCLCNumber
				'subjects':[],#Subject
				'type':[],#Btype
				'last_modified':[],#LastModified
				'languages':[],#Language
				'works':[],#Work
				'number_of_pages':book_obj['number_of_pages'],
				'pagination':book_obj['pagination'],
				'key':book_obj['key'],
				'title':book_obj['title'],
				'notes':book_obj['notes'],
				'publish_date':book_obj['publish_date'],
				'publish_country':book_obj['publish_country'],
				'by_statement':book_obj['by_statement'],
				'ocaid':book_obj['ocaid'],
				'latest_revision':book_obj['latest_revision'],
				'revision':book_obj['revision'],
			}


		if book_obj['publisher__name'] and book_obj['publisher__name'] not in books_dct[book_obj['id']]['publishers']:
			books_dct[book_obj['id']]['publishers'].append(book_obj['publisher__name'])
			print(book_obj['publisher__name'])

		if book_obj['isbn10__isbn'] and book_obj['isbn10__isbn'] not in books_dct[book_obj['id']]['isbn_10']:
			books_dct[book_obj['id']]['isbn_10'].append(book_obj['isbn10__isbn'])

		if book_obj['subjectplace__pname'] and book_obj['subjectplace__pname'] not in books_dct[book_obj['id']]['subject_place']:
			books_dct[book_obj['id']]['subject_place'].append(book_obj['subjectplace__pname'])

		if book_obj['cover__cover'] and book_obj['cover__cover'] not in books_dct[book_obj['id']]['covers']:
			books_dct[book_obj['id']]['covers'].append(book_obj['cover__cover'])

		if book_obj['author__name'] and book_obj['author__name'] not in books_dct[book_obj['id']]['authors']:
			books_dct[book_obj['id']]['authors'].append(book_obj['author__name'])

		if book_obj['publishplace__pname'] and book_obj['publishplace__pname'] not in books_dct[book_obj['id']]['publish_places']:
			books_dct[book_obj['id']]['publish_places'].append(book_obj['publishplace__pname'])

		if book_obj['genre__name'] and book_obj['genre__name'] not in books_dct[book_obj['id']]['genres']:
			books_dct[book_obj['id']]['genres'].append(book_obj['genre__name'])

		if book_obj['sourcerecord__record'] and book_obj['sourcerecord__record'] not in books_dct[book_obj['id']]['source_records']:
			books_dct[book_obj['id']]['source_records'].append(book_obj['sourcerecord__record'])

		if book_obj['lccn__number'] and book_obj['lccn__number'] not in books_dct[book_obj['id']]['lccn']:
			books_dct[book_obj['id']]['lccn'].append(book_obj['lccn__number'])

		if book_obj['deweydecimalclass__ddclass'] and book_obj['deweydecimalclass__ddclass'] not in books_dct[book_obj['id']]['dewey_decimal_class']:
			books_dct[book_obj['id']]['dewey_decimal_class'].append(book_obj['deweydecimalclass__ddclass'])

		if book_obj['oclcnumber__number'] and book_obj['oclcnumber__number'] not in books_dct[book_obj['id']]['oclc_numbers']:
			books_dct[book_obj['id']]['oclc_numbers'].append(book_obj['oclcnumber__number'])

		if book_obj['subject__name'] and book_obj['subject__name'] not in books_dct[book_obj['id']]['subjects']:
			books_dct[book_obj['id']]['subjects'].append(book_obj['subject__name'])

		if book_obj['btype__type_name'] and book_obj['btype__val']:
			b_type_dct = {book_obj['btype__type_name']:book_obj['btype__val']}
			if b_type_dct not in books_dct[book_obj['id']]['type']:
				books_dct[book_obj['id']]['type'].append(b_type_dct)

		if book_obj['lastmodified__type_name'] and book_obj['lastmodified__val']:
			lastmodified_dct = {
				'type':book_obj['lastmodified__type_name'],
				'value':book_obj['lastmodified__val'],
			}
			if lastmodified_dct not in books_dct[book_obj['id']]['last_modified']:
				books_dct[book_obj['id']]['last_modified'].append(lastmodified_dct)
		
		if book_obj['language__type_name'] and book_obj['language__val']:
			language_dct = {book_obj['language__type_name']:book_obj['language__val']}
			if language_dct not in books_dct[book_obj['id']]['languages']:
				books_dct[book_obj['id']]['languages'].append(language_dct)
		
		if book_obj['work__type_name'] and book_obj['work__val']:
			work_dct = {book_obj['work__type_name']:book_obj['work__val']}
			if work_dct not in books_dct[book_obj['id']]['works']:
				books_dct[book_obj['id']]['works'].append(work_dct)

	for book_id, book_dct in books_dct.items():
		clean_book_dct = {}
		for key, val in book_dct.items():
			if val:
				clean_book_dct[key] = val


		books_lst.append(clean_book_dct)


	return JsonResponse({'books_lst':books_lst})

# CRUD examples follow

@csrf_exempt
def book_create(request):

	p_dct = json.loads(request.body)
	
	try:
		r_status = 'Success'
		books_lst = format_books(p_dct)
		if books_lst:
			books2db(books_lst)
		else:
			return JsonResponse({'status':'"author_key" and/or "works" missing'})

	except:
		r_status = 'Error'

	return JsonResponse({'status':r_status})

@csrf_exempt
def book_retrieve(request):

	p_dct = json.loads(request.body)

	filters_dct = {}
	
	try:
		r_status = 'Success'

		if 'title' in p_dct:
			filters_dct['title'] = p_dct['title']

		if 'author_key' in p_dct:
			filters_dct['author_key'] = p_dct['author_key']

		return get_books(filters_dct)

	except:
		r_status = 'Error'

	return JsonResponse({'status':r_status})

@csrf_exempt
def book_update(request):

	p_dct = json.loads(request.body)
	
	try:
		r_status = 'Success'

		if 'title' not in p_dct:
			return JsonResponse({'status':'"title" is mandatory'})

		if 'updates' not in p_dct:
			return JsonResponse({'status':'"updates" is mandatory'})

		if 'title' not in p_dct['updates']:
			return JsonResponse({'status':'"title update" is mandatory'})

		objs = model_k.Book.objects.filter(title=p_dct['title'])
		if not objs:
			return JsonResponse({'status':'books not found'})

		objs.update(
			title=p_dct['updates']['title']
		)
	except:
		r_status = 'Error'

	return JsonResponse({'status':r_status})

@csrf_exempt
def book_delete(request):

	try:
		r_status = 'Success'
		p_dct = json.loads(request.body)

		if 'title' not in p_dct:
			return JsonResponse({'status':'"title" is mandatory'})

		objs = model_k.Book.objects.filter(title=p_dct['title'])
		if not objs:
			return JsonResponse({'status':'books not found'})

		objs.delete()
	except:
		r_status = 'Error'

	return JsonResponse({'status':r_status})
