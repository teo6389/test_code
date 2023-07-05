# from django.contrib.auth.models import User, Group
from book_collection import models as model_k
from rest_framework import serializers

# to be tested
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = model_k.Book
        fields = ['all']