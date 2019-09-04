from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import Timestamp,User,Work,Subject
from django.utils import timezone
from datetime import datetime
from django.views.decorators.cache import cache_control
from django.db.models import Count
from django.db.models.functions import TruncDate
from collections import defaultdict

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.user.is_authenticated():
        return redirect('/home/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)
            if user :
                if user.is_active:
                    login(request,user)
                    try:
                        get=Timestamp.objects.get(Date=datetime.now(), userp=user)
                    except:
                        t=Timestamp()
                        t.Logintime = datetime.now()
                        t.Logouttime = datetime.now()
                        t.Date=datetime.now()
                        t.userp = user
                        t.save()

                    return redirect('/home/')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse("Invalid details")
        else:
            return render(request,'BBproj/login.html',)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def loggedin(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # ip= x_forwarded_for.split(',')[0]
    # ip1=ip.split('.')[0]
    # ip2=ip.split('.')[1]
    # ip=ip1+ip2
    # if ip =="" or ip =="122169" or ip == "4933":
    if request.user.is_superuser:
        return render(request,'BBproj/admin.html')
    else:
        return render(request,'BBproj/loggedin.html',)
    # else:
    #     return HttpResponse("Abe Office ke network se login kar")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def timestamp(request):

    if request.user.is_superuser:
        Timestamps1=Timestamp.objects.all()
        # Timestampss = Timestamp.objects.annotate(Count('userp'))
        # Timestamps = Timestamp.objects.annotate(date=TruncDate('Logintime')).values('date')
        Timestampss=Timestamp.objects.values('Date').annotate(dcount=Count('Date'))
        return render(request,'BBproj/timestamp.html',{'Timestamps1':Timestamps1,'Timestampss':Timestampss},)
    else:
        return render(request,'BBproj/loggedin.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def assignwork(request):
    users = User.objects.all()
    if request.method == 'POST':
        Userr = request.POST.getlist('userr')
        subject = request.POST.get('Subject')
        subwork = request.POST.get('subwork')
        deadline=request.POST.get('deadline')
        deadline=deadline.replace("/","-")
        # date= datetime.strptime(request.POST.get('deadline')[0:9], '%Y/%m/%d')
        # time = datetime.strptime(request.POST.get('deadline')[11:15], '%H:%M')

        try:
            Check=Subject.objects.get(Subject_name=subject)
        except Subject.DoesNotExist:
            S = Subject()
            S.Subject_name = subject
            S.save()

        W = Work()
        W.deadline = deadline
        W.Subject=Subject.objects.get(Subject_name=subject)
        W.text=subwork
        W.save()
        # Userrr = User.objects.get(User=Userr)
        for U in Userr:
         hello=User.objects.get(username=U)
         W.userpp.add(hello)

    # Subjectss=Subject.objects.all()[0]
    # SS=Subjectss.subworks.all()
    S=Subject.objects.all()
    return render(request, 'BBproj/assignwork.html',{'users':users,'Subjects':S})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def work(request):
    users = User.objects.all()
    if request.method == 'POST':
        Userr = request.POST.getlist('userr')
        subject = request.POST.get('Subject')
        subwork = request.POST.get('subwork')
        deadline = request.POST.get('deadline')
        deadline = deadline.replace("/", "-")
        # date= datetime.strptime(request.POST.get('deadline')[0:9], '%Y/%m/%d')
        # time = datetime.strptime(request.POST.get('deadline')[11:15], '%H:%M')

        try:
            Check = Subject.objects.get(Subject_name=subject)
        except Subject.DoesNotExist:
            S = Subject()
            S.Subject_name = subject
            S.save()

        W = Work()
        W.deadline = deadline
        W.Subject = Subject.objects.get(Subject_name=subject)
        W.text = subwork
        W.save()
        # Userrr = User.objects.get(User=Userr)
        for U in Userr:
            hello = User.objects.get(username=U)
            W.userpp.add(hello)

    # Subjectss=Subject.objects.all()[0]
    # SS=Subjectss.subworks.all()
    S = Subject.objects.all()
    return render(request, 'BBproj/work.html', {'users': users, 'Subjects': S})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def assignedwork(request):
    current_user=request.user
    Wor=Work.objects.filter(userpp=current_user)
    return render(request, 'BBproj/assigned_work.html',{'Work':Wor})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def loggout(request):
    t = Timestamp.objects.get(Date=datetime.now(), userp=request.user)
    t.Logouttime = datetime.now()
    t.save()
    logout(request)
    return HttpResponseRedirect('/')

# def text_append(request,text_id):
#     text=Work.objects.get(pk=text_id)
#     if request.method == 'POST':
#         text_appen=text_append()
#         text_appen.text=text.objects.get(pk=text_id)
#         text_appen.append=request.POST.get('text')
#         text_append.save()
#     else:
#         if (request.user in text.userpp):
#             return render(request, 'BBproj/text_append.html', {'text_id': text_id})
