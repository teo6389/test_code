from django.shortcuts import render
from book_collection import models as model_k
import requests


def fetch_books(keyword):

	books_response = requests.get('https://openlibrary.org/search.json?q='+keyword)
	books_dct = books_response.json()
	# print(books_dct)

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

		# print(book)
		# print(valid_book)

		if valid_book:
			books_lst.append(book_init_dct_obj)
		else:
			pass
			# write to log

	return books_lst


def fetch_books_wrap(request):

	books_lst = fetch_books('spacecraft')

	if books_lst:
		books2db(books_lst)


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
				place=subjectplace,
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
				place=publishPlace,
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

def get_all_books(request):

	pass