from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import index, detect, trainer, create_dataset, match, fetch, image_data_view
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('match/', match, name="match"),
    path('fetch/', fetch, name='fetch'),
    path('image-data/', image_data_view, name='image_data'),
    url(r'^$', index),
    url(r'^create_dataset$', create_dataset),
    url(r'^detect$', detect),
    url(r'^trainer$', trainer),
]

