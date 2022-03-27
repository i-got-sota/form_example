from django.urls import path

from . import views

urlpatterns = [
    path('1', views.inquiry1, name='inquiry1'),
    path('2', views.inquiry2, name='inquiry2'),
    path('done', views.done, name='inquiry_done')
]