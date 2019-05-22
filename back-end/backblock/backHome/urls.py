from django.urls import path , include
from django.conf.urls import url
from .views import *




urlpatterns = [
    url(r'^work$',WorktoList.as_view()),
    url(r'work/(?P<pk>[0-9]+)$',WorktoDetail.as_view()),
    url(r'^Student$',StudenttoList.as_view()),
    url(r'Student/(?P<pk>[0-9]+)$',StudenttoDetail.as_view()),
    url(r'^Company$',CompanytoList.as_view()),
    url(r'Company/(?P<pk>[0-9]+)$',CompanytoDetail.as_view()),
    url(r'^status$',statusWorktoList.as_view()),
    url(r'status/(?P<pk>[0-9]+)$',statusWorktoDetail.as_view()),

]
