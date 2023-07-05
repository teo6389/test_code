from django.shortcuts import render
import requests

def fetch_books(keyword):

	books_response = requests.get('https://openlibrary.org/search.json?q='+keyword)
	books_dct = books_response.json()
	# print(books_dct)

	books_lst = []

	for book in books_dct['docs']:

		book_response = requests.get('https://openlibrary.org/books/'+book['key'].replace('/books/','')+'.json')
		book_dct = book_response.json()
		print(book_dct)

		valid_book = True

		book_init_dct_obj = {
			'publisher':[],#Publisher
			'isbn10':[],#ISBN10
			'subjectplace':[],#SubjectPlace
			'cover':[],#Cover
			'lcclassification':[],#LCClassification
			'author':[],#Author
			'publishPlace':[],#PublishPlace
			'genre':[],#Genre
			'sourcerecord':[],#SourceRecord
			'lccn':[],#LCCN
			'deweydecimalclass':[],#DeweyDecimalClass
			'oclcnumber':[],#OCLCNumber
			'subject':[],#Subject
			'classification':[],#Classification
			'btype':[],#Btype
			'created':[],#Created
			'lastmodified':[],#LastModified
			'language':[],#Language
			'work':[],#Work
			'identifiers':[],#Identifiers
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
		
		if 'publisher' in book_dct:
			for publisher in book['publisher']:
				book_init_dct_obj['publisher'].append(publisher)


		if 'isbn' in book_dct:
			for isbn in book['isbn']:
				book_init_dct_obj['isbn10'].append(isbn)


		# does not exist
		if 'subject_place' in book_dct:
			for subject_place in book['subject_place']:
				book_init_dct_obj['subjectplace'].append(subject_place)


		# does not exist
		# cover_edition_key
		# cover_i
		if 'covers' in book_dct:
			for covers in book['covers']:
				book_init_dct_obj['cover'].append(covers)


		# does not exist
		if 'lc_classifications' in book_dct:
			for lc_classifications in book['lc_classifications']:
				book_init_dct_obj['lcclassification'].append(lc_classifications)

		'''
		# does not exist
		# author_key
		# author_name
		if 'authors' in book_dct:
			for in book['authors']:
				book_init_dct_obj['author'].append()


		# does not exist
		if 'publish_places' in book_dct:
			for in book['publish_places']:
				book_init_dct_obj['publishPlace'].append()


		# does not exist
		if 'genres' in book_dct:
			for in book['genres']:
				book_init_dct_obj['genre'].append()


		# does not exist
		if 'source_records' in book_dct:
			for in book['source_records']:
				book_init_dct_obj['sourcerecord'].append()


		if 'lccn' in book_dct:
			for in book['lccn']:
				book_init_dct_obj['lccn'].append()


		# does not exist
		if 'dewey_decimal_class' in book_dct:
			for in book['dewey_decimal_class']:
				book_init_dct_obj['deweydecimalclass'].append()


		# does not exist
		# oclc
		if 'oclc_numbers' in book_dct:
			for in book['oclc_numbers']:
				book_init_dct_obj['oclcnumber'].append()


		# does not exist
		# subject
		if 'subjects' in book_dct:
			for in book['subjects']:
				book_init_dct_obj['subject'].append()


		# does not exist
		if 'classifications' in book_dct:
			for in book['classifications']:
				book_init_dct_obj['classification'].append({
					'':'',
				})


		if 'type' in book_dct:
			for in book['type']:
				book_init_dct_obj['btype'].append({
					'':'',
				})


		# does not exist
		if 'created' in book_dct:
			for in book['created']:
				book_init_dct_obj['created'].append({
					'':'',
				})


		# does not exist
		# last_modified_i
		if 'last_modified' in book_dct:
			for in book['last_modified']:
				book_init_dct_obj['lastmodified'].append({
					'':'',
				})


		# does not exist
		# language
		if 'languages' in book_dct:
			for in book['languages']:
				book_init_dct_obj['language'].append({
					'':'',
				})


		# seed -> '/works'
		if 'works' in book_dct:
			for in book['works']:
				book_init_dct_obj['work'].append({
					'':'',
				})


		# does not exist
		if 'identifiers' in book_dct:
			for in book['identifiers']:
				book_init_dct_obj['identifiers'].append({
					'':'',
				})


		# does not exist
		# number_of_pages_median
		if 'number_of_pages' in book_dct:
			book_init_dct_obj['number_of_pages'] = book['number_of_pages']

		# does not exist
		if 'pagination' in book_dct:
			book_init_dct_obj['pagination'] = book['pagination']

		if 'key' in book_dct:
			book_init_dct_obj['key'] = book['key']

		if 'title' in book_dct:
			book_init_dct_obj['title'] = book['title']

		# does not exist
		if 'notes' in book_dct:
			book_init_dct_obj['notes'] = book['notes']

		if 'publish_date' in book_dct:
			book_init_dct_obj['publish_date'] = book['publish_date']

		# does not exist
		if 'publish_country' in book_dct:
			book_init_dct_obj['publish_country'] = book['publish_country']

		# does not exist
		if 'by_statement' in book_dct:
			book_init_dct_obj['by_statement'] = book['by_statement']

		# does not exist
		if 'ocaid' in book_dct:
			book_init_dct_obj['ocaid'] = book['ocaid']

		# does not exist
		if 'latest_revision' in book_dct:
			book_init_dct_obj['latest_revision'] = book['latest_revision']

		# does not exist
		if 'revision' in book_dct:
			book_init_dct_obj['revision'] = book['revision']

		
		if valid_book:
			books_lst.append(book_init_dct_obj)
		else:
			pass
			# write to log
		'''

	return books_lst


def fetch_books_wrap(request):

	fetch_books('spacecraft')


def books2db(books_lst):

	for book_dct in books_lst:

		pass
		# models manage

fetch_books('spacecraft')