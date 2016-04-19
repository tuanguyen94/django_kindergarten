from django.conf.urls import url 

from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^k5/', views.k5,name='k5'),
	url(r'^k6/', views.k6,name='k6'),
	url(r'^k7/', views.k7,name='k7'),
	url(r'^k8/', views.k8,name='k8'),

	url(r'^l1/', views.l1,name='l1'),
	url(r'^l2/', views.l2,name='l2'),

	url(r'^answeer/', views.checkAnsweer,name='checkAnsweer'),
]