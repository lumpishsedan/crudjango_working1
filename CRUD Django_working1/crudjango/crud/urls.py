from django.conf.urls import url
from . import views
from pbapp.views import list_and_create_view

urlpatterns= [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
#    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),

    url(r'^edit/(?P<id>\d+)$', list_and_create_view, name='home'),
#    path('post/<int:pk>/', BlogDetailView.as_view(), name='home'), # new
]
