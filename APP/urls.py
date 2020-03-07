from django.conf.urls import url
from APP import views

urlpatterns=[
    url(r'^hello/',views.hello,name='hello'),
    url(r'^news/',views.news,name='news'),
    url(r'^jokes/',views.jokes,name='jokes'),

    url(r'^home/', views.home, name='home'),
    url(r'^get_phone/', views.get_phone, name='get_phone'),
    url(r'^get_ticket/', views.get_ticket, name='get_ticket'),
    url(r'^search/', views.search, name='search'),
    url(r'^calc/', views.calc, name='calc'),
    url(r'^add_students/', views.add_students, name='add_students'),
    url(r'^students_list/', views.students_list, name='students_list'),
    url(r'^get_students_with_page/', views.get_students_with_page, name='get_students_with_page'),


]