from django.db import models

# Create your models here.
class Book(models.Model):

	number_of_pages = models.CharField(max_length=200, blank=True, null=True)
	pagination = models.CharField(max_length=200, blank=True, null=True)
	key = models.CharField(max_length=200, blank=True, null=True)
	title = models.CharField(max_length=200, blank=True, null=True)
	notes = models.CharField(max_length=200, blank=True, null=True)
	publish_date = models.CharField(max_length=200, blank=True, null=True)
	publish_country = models.CharField(max_length=200, blank=True, null=True)
	by_statement = models.CharField(max_length=200, blank=True, null=True)
	ocaid = models.CharField(max_length=200, blank=True, null=True)
	latest_revision = models.CharField(max_length=200, blank=True, null=True)
	revision = models.CharField(max_length=200, blank=True, null=True)

class Publisher(models.Model):

	name = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class ISBN10(models.Model):

	isbn = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class SubjectPlace(models.Model):

	pname = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class Cover(models.Model):

	cover = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class Author(models.Model):

	name = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class PublishPlace(models.Model):

	pname = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class Genre(models.Model):

	name = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class SourceRecord(models.Model):

	record = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class LCCN(models.Model):

	number = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class DeweyDecimalClass(models.Model):

	ddclass = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class OCLCNumber(models.Model):

	number = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class Subject(models.Model):

	name = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class Btype(models.Model):

	type_name = models.CharField(max_length=200)
	val = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class LastModified(models.Model):

	type_name = models.CharField(max_length=200)
	val = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

# differenet management
class Language(models.Model):
	type_name = models.CharField(max_length=200)# this might be repeated
	val = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

class Work(models.Model):
	type_name = models.CharField(max_length=200)# this might be repeated
	val = models.CharField(max_length=200)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)
