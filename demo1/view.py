from django.http import HttpResponse
def index(request):
    return HttpResponse('hello world')
def hello(request):
    return HttpResponse('哈哈哈哈哈')
