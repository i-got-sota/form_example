from django.urls import path

from . import views

urlpatterns = [
    path('', views.inquiry1, name='inquiry'),
    path('done', views.done, name='inquiry_done')
]