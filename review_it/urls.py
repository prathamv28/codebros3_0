from django.conf.urls import url
from . import views

app_name = 'review_it'

urlpatterns = [
    url(r'^$', views.home , name = 'home'),
    url(r'^logout/$', views.logout_ , name = 'logout'),
    url(r'^login_page/$' , views.login_page , name = 'login_page'),
    url(r'^login_auth/$', views.login_auth , name='login_auth'),
    url(r'^signup/$' , views.signup , name = 'signup'),
    url(r'^add_user/$' , views.add_user , name = 'add_user'),
    url(r'^write_review/$' , views.write_review , name = 'write_review'),
    url(r'^add_review/$' , views.add_review , name = 'add_review'),
    url(r'^search/$' , views.search , name = 'search'),
]
