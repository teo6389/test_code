'''
from book.api.viewsets import bookviewsets
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register('book', bookviewsets, base_name ='book_api')
'''