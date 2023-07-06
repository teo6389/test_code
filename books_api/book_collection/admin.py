from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserExtend)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(ISBN10)
admin.site.register(SubjectPlace)
admin.site.register(Cover)
admin.site.register(Author)
admin.site.register(PublishPlace)
admin.site.register(Genre)
admin.site.register(SourceRecord)
admin.site.register(LCCN)
admin.site.register(DeweyDecimalClass)
admin.site.register(OCLCNumber)
admin.site.register(Subject)
admin.site.register(Btype)
admin.site.register(LastModified)
admin.site.register(Language)
admin.site.register(Work)
admin.site.register(FavoriteBook)