from django.http import HttpResponse


def index(request):
    return HttpResponse('hello world')
def hello(request):
    return HttpResponse('哈哈哈哈哈')

from django.template import Template,Context
def html1(request):
    html='''
    <html>
    <head>
    </head>
    <body>
    <h1>这是个h1标签</h1>
    <a href='https://www.baidu.com/s?ie=UTF-8&wd=%E9%AB%98%E6%B8%85%E7%BE%8E%E5%A5%B3%E5%A4%A7%E5%9B%BE' title='高清美女大图'>
    <img src='https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1699766746,2799611360&fm=26&gp=0.jpg' title='高清美女大图'>
    </a>
    <p>{{name}}</p>
    </body>
    </html>
    '''
    template_obj=Template(html)
    parmas=dict(name='高清美女大图')
    context_obj=Context(parmas)
    result=template_obj.render(context_obj)
    return HttpResponse(result)
    # return HttpResponse(html)




from django.shortcuts import render
def mb(request):
    name="张颖"
    return render(request,'mb.html',{'name':name})


# from django.shortcuts import render_to_response
# def mb1(request):
#     name='张颖'
#     return render_to_response('abc.html',{'name':name})

from django.template.loader import get_template
def mb2(request):
    template=get_template('abc.html')
    name='张颖'
    result=template.render({'name':name})
    return HttpResponse(result)


def mb3(request,age):
    class Say():
        def say(self):
            return "hello"
    name='你好'
    age=int(age)
    gender='男'
    hobby=['女','吃','喝','玩']
    score={'math':99,'chinese':99,'english':99}
    say=Say()
    return render(request,'hello.html',locals())


def qxphb(request):
    rng=[{'name':'简自豪','img':'uzi.jpg','url':'https://baike.baidu.com/item/%E7%AE%80%E8%87%AA%E8%B1%AA/14190783?fromtitle=Uzi&fromid=20207029&fr=aladdin'},
        {'name':'李元浩','img':'xiaohu.jpg','url':'https://baike.baidu.com/item/%E6%9D%8E%E5%85%83%E6%B5%A9?fromtitle=xiaohu&fromid=20245928'},
        {'name':'刘世宇','img':'mlxg.jpg','url':'https://baike.baidu.com/item/%E5%88%98%E4%B8%96%E5%AE%87?fromtitle=mlxg&fromid=20273001'},
        {'name':'严君泽','img':'letme.jpg','url':'https://baike.baidu.com/item/%E4%B8%A5%E5%90%9B%E6%B3%BD?fromtitle=Letme&fromid=22598656'},
        {'name':'史森明','img':'ssm.jpg','url':'https://baike.baidu.com/item/%E5%8F%B2%E6%A3%AE%E6%98%8E'},
        ]
    return render(request,'qxphb.html',locals())