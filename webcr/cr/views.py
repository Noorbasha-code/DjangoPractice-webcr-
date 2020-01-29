from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest,HttpResponseServerError
import datetime
from django.core.mail import send_mail
from webcr import settings
from cr.form import Student_info
from cr.models import Student1


# Create your views here.


def hello(request):
    return HttpResponse("<h1> hellow world...!</h1>")
def time(request):
    now=datetime.datetime.now()
    html="<html><head><body><h2> NOW THE TIME IS: %s. </head></body></html>" %now
    return HttpResponse(html)
def mail(request):
    sub = "Greetings"
    msg = "congratualation for your success"
    to = "knoorbasha253@gmail.com"
    res=send_mail(sub,msg,settings.EMAIL_HOST,[to])
    if(res==1):
        msg="mail sent successfully "
    else:
        msg="mail couldnot sent"
    return HttpResponse(msg)

def method(request):
    return HttpResponse(request.path)

def signIn(request):
    return render(request,'cr/reg.html')

def index(request):
    if request.method == 'POST':
        form = Student_info(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    stu = Student_info()
    return render(request,'cr/sample.html',{'form': stu})

def show(request):
    data = Student1.objects.all()
    return render(request,'cr/show.html',{'data':data})

def delete(request,id):
    #return HttpResponse('<h2>'+str(id)+'</h2>')
    a= Student1.objects.get(id=id)
    Student1.delete(a)
    return redirect('show')
def update(request, id):
    data = Student1.objects.get(id=id)
    if request.method == 'POST':
        form = Student_info(request.POST,instance=data)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    return render(request, 'cr/update.html', {'data': data})


