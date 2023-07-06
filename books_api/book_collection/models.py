from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_extend(sender, instance, created, **kwargs):
    if created:
        UserExtend.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_extend(sender, instance, **kwargs):
    instance.userextend.save()

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

class FavoriteBook(models.Model):
	user = models.ForeignKey('UserExtend', on_delete=models.CASCADE)
	book = models.ForeignKey('Book', on_delete=models.CASCADE)

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
