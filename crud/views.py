from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from crud.models import student3
from django.core import serializers


def index(request):
    return render(request, 'index.html')


def form(request):
    show = student3.objects.all()
    context={"profile":show}
    return render(request, 'stuform.html',context)


def send(request):
    if(request.method == "POST"):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        student3(fname=fname, lname=lname, email=email, phone=phone).save()
        title = {'title': 'Send', 'msg': 'Success'}
        # return render(request, 'stuform.html', title)
        # show = student3.objects.all().json()
        # show = serializers.serialize("json", student3.objects.all())
        return JsonResponse({"title":"success"})
    else:
        return JsonResponse({"title":"Something is wrong"})


def show(request):
    show = student3.objects.all()
    title = {'title': 'show', 'profile': show}
    return render(request, 'show.html', title)


def edit(request):
    id = request.GET['id']
    for data in student3.objects.filter(id=id):
        fname = data.fname
        lname = data.lname
        email = data.email
        phone = data.phone
    title = {'id': id, 'title': 'show', 'fname': fname,
             'lname': lname, 'email': email, 'phone': phone}
    return render(request, 'edit.html', title)


def update(request):
    if(request.method == "POST"):
        id = request.POST.get('id')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        student3.objects.filter(id=id).update(
            fname=fname, lname=lname, email=email, phone=phone)
        title = {'title': 'show', 'msg': 'Successfully Update'}
        return HttpResponseRedirect('show', title)
    else:
        return HttpResponse('Error-404')


def profile(request):
    id = request.GET['id']
    for data in student3.objects.filter(id=id):
        fname = data.fname
        lname = data.lname
        email = data.email
        phone = data.phone
    title = {'title': 'show', 'fname': fname,
             'lname': lname, 'email': email, 'phone': phone}
    return render(request, 'profile2.html', title)
