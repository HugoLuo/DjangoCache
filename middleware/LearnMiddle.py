import random
import time

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddle(MiddlewareMixin):
    def process_request(self,request):
        #信息收集
        IP = request.META.get("REMOTE_ADDR")
        print(IP)

        #有return....切断当前这个流程，直接返回
#        if request.path == "/APP/get_phone/":
#            if IP == '127.0.0.1':
#                if random.randrange(100) > 30:
#                    return HttpResponse("恭喜你获取小米10 手机")
#        if request.path == "/APP/get_ticket/":
#            if IP.startswith("192.168.3.5"):
#                return HttpResponse("已抢光")

#        if request.path == "/APP/search/":
#            result = cache.get(IP)
#            if result:
#                return HttpResponse("你的请求过于频繁，请20秒后再试试")
#            cache.set(IP,IP,timeout=20)
            #这里没有返回就继续后面的流程

#        requests = cache.get(IP,[])
#        black_list = cache.get('black',[])

#        if IP in black_list:
#            return HttpResponse("你在黑名单了，禁止访问一天")

        #帅选数据，剔除不需要的
#        while requests and time.time() - requests[-1] > 60:
#            requests.pop()
#        requests.insert(0,time.time())
#        cache.set(IP,requests,timeout=60)

#        if len(requests) > 30:
#            black_list.append(IP)
#            cache.set('black',black_list,timeout=60*60*24)
#            return HttpResponse("请求次数过于频繁,一分钟都都访问超过30次了")


#        if len(requests) > 10:
#            return HttpResponse("请求次数过于频繁")


#    def process_exception(self,request,exception):
#        print(request,exception)
#        return redirect(reverse('APP:home'))

