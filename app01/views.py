from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    return HttpResponse('app01')
def zj(request):
    # person=Person(name='张颖',age=18,height=180,birthday='1998-02-06')
    # person.save()
    # person=Person()
    # person.name='张大胸'
    # person.age=50
    # person.height=140
    # person.birthday='1988-02-02'
    # person.save()
    Person.objects.create(name='张大胸',age=87)
    # data=dict(name='张大胸',age=67)
    # Person.objects.create(**data)
    return HttpResponse("增加")

def cx(request):
    # data=Person.objects.all()
    # for i in data:
    #     print(i.name)
    # print(data)
    # data=Person.objects.get(id=1)
    # print(data)
    # data=Person.objects.filter(age=18)
    # print(data[0].name)
    # data=Person.objects.order_by('age')
    # print(data)
    # data=Person.objects.filter(name='张大胸').first()
    # print(data)
    # data = Person.objects.filter(name='张大胸').last()
    # print(data)
    # 小于
    # data=Person.objects.filter(id__lt=3)
    # data=Person.objects.filter(id__lte=3)
    # print(data)
    # 大于
    # data=Person.objects.filter(id__gt=2)
    # data=Person.objects.filter(id__gte=2)
    # print(data)
    # in包含
    # data=Person.objects.filter(id__in=[1,2,9])
    # print(data)
    # range范围
    # data=Person.objects.filter(id__range=[1,3])
    # print(data)
    # startswith开始
    # data=Person.objects.filter(name__startswith='张')
    # print(data)
    # data=Person.objects.filter(name__endswith='颖')
    # print(data)
    data = Person.objects.filter(name__contains='大')
    print(data)
    data = Person.objects.filter(name__icontains='大')
    print(data)
    return HttpResponse('查询')

def xg(request):
    # data=Person.objects.get(id=2)
    # data.name='张大屁股'
    # data.save()
    data=Person.objects.filter(name='张大胸').first()
    data.name='张长腿'
    data.save()
    return HttpResponse('修改')

def sc(request):
    Person.objects.filter(id=5).delete()
    return HttpResponse('删除')


def duozj(request):
    # 增加出版社
    # Publish.objects.create(name='清华出版社',address='北京')
    # Publish.objects.create(name='北大出版社',address='北京朝阳')
    # Publish.objects.create(name='河北出版社',address='石家庄')
    # 增加书
    # 第一种办法
    # Book.objects.create(name='python',publish_id=1)
    # publish=Publish.objects.get(name='北大出版社')
    # Book.objects.create(name='python入门',publish_id=publish.id)
    # 第二种办法
    # Book.objects.create(name='pythonDjango入门',publish=Publish.objects.get(id=1))
    #第三种办法
    # 正向操作  从外键所在的表到主表叫正向
    # book=Book()
    # book.name='python从入门到精通'
    # book.publish=Publish.objects.get(name='河北出版社')
    # book.save()
    #反向操作  从主表到外键所在的表叫反向
    # public=Publish.objects.get(name='河北出版社')
    # public.book_set.create(name='python从入门到放弃')
    return HttpResponse('一对多增加')


def duocx(request):
    # 第一种办法
    # publish=Publish.objects.get(name='清华出版社')
    # book=Book.objects.filter(publish_id=publish.id)
    # for i in book:
    #     print(i.name)
    # 第二种方法
    # 正向查询  从外键所在的表到主表叫正向
    # 查询python从入门到放弃属于哪个出版社
    # book=Book.objects.filter(name='python从入门到放弃').first()
    # print(book.name)
    # print(book.publish.name)
    # 第三种办法
    # 反向查询 从主表到外键所在的表叫反向
    publish=Publish.objects.get(name='清华出版社')
    book=publish.book_set.all()
    for i in book:
        print(i.name)
    return HttpResponse('一对多查询')
