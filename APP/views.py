import random
from time import sleep

from django.core.paginator import Paginator

from APP.models import Student

#使用django内置默认的缓存
#from django.core.cache import cache

#使用redis缓存
from django.core.cache import caches
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


def hello(request):
    return HttpResponse("Hello")

#使用装饰器缓存
@cache_page(60)
def news(request):

#使用django内置默认的缓存
#    result = cache.get("news")

#使用指定的redis缓存
    cache = caches['redis_backend']
    result = cache.get('news')
    if result:
        return HttpResponse(result)

    news_list = []
    for i in range(20):
        news_list.append("news message %d" % i)
    sleep(5)
    data = {
        'news_list': news_list
    }
    response = render(request,'news.html',context=data)
    cache.set("news",response.content,timeout=60)

    return response
#设置缓存在指定的缓存里
#@cache_page(60,cache='default')
@cache_page(60,cache='redis_backend')
def jokes(request):
    sleep(5)
    return HttpResponse("Jokes List")


def home(request):
    return HttpResponse("home")


def get_phone(request):

    if random.randrange(100) > 80:
        return HttpResponse("恭喜你抢到 小米10 手机")
    else:
        return HttpResponse("正在进行排队.........")


def get_ticket(request):
    return HttpResponse("还剩99张，优惠")


def search(request):

    return HttpResponse("这是你搜索到的资源")


def calc(request):
    a = 20
    b = 50
    result = (a+b)/0
    return HttpResponse(result)

def add_students(request):
    for i in range(100):
        student = Student()
        student.s_name="Hugo%d" % i
        student.save()
    return HttpResponse("100个学生添加成功")

def students_list(request):
    all_students = Student.objects.all()
    page = int(request.GET.get("page",1))
    per_page = int(request.GET.get("per_page",5))
    students=all_students[per_page*(page-1):per_page*page]
    data = {
        'students':students,
    }
    return render(request,'students_list.html',context=data)


def get_students_with_page(request):
    all_students = Student.objects.all()
    page = int(request.GET.get("page",1))
    per_page = int(request.GET.get("per_page",10))
    paginator = Paginator(all_students,per_page)
    page_object = paginator.page(page)
    data = {
        'page_object': page_object,
        'page_range': paginator.page_range
    }
    return render(request,'get_students_with_page.html',context=data)
