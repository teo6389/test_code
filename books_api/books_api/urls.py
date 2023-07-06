"""
URL configuration for books_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
# from router import router
from rest_framework.authtoken import views
from book_collection import views as b_views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'book', b_views.bookviewsets)

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('books/', include('book_collection.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]
