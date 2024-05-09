from django.urls import path
from APP import views

urlpatterns=[
    path('hello/',views.hello,name='hello'),
    path('news/',views.news,name='news'),
    path('jokes/',views.jokes,name='jokes'),

    path('home/', views.home, name='home'),
    path('get_phone/', views.get_phone, name='get_phone'),
    path('get_ticket/', views.get_ticket, name='get_ticket'),
    path('search/', views.search, name='search'),
    path('calc/', views.calc, name='calc'),
    path('add_students/', views.add_students, name='add_students'),
    path('students_list/', views.students_list, name='students_list'),
    path('get_students_with_page/', views.get_students_with_page, name='get_students_with_page'),


]