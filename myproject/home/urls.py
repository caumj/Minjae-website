from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^about/$', views.about, name='about'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^order/$', views.order, name='order'),
    url(r'^user/$', views.user, name='user'),
    url(r'^signout/$', views.logout, name='logout'),

]
