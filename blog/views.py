from typing import Any

from django.shortcuts import render, redirect
from . import views
from .models import Post
from .forms import CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Company,Contact,Services


def home(request):
    data = {
        'posts': Post.objects.all(),
        'Company': Company.objects.all()
    }
    return render(request, 'sample.html', data)


def postdetail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'postdetail.html', {'post': post})


def cong(request):
    return render(request, "cong.html")


def login(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Address = request.POST['Address']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        Contact(Name=Name, Address=Address, Email=Email, phone=Phone).save()
        msg = "you are registered"
        return render(request, "sample.html", {'msg': msg})
    else:
        return HttpResponse("<h1>404-not found</h1>")


def about(request):
   return render(request, "about.html")


def services(request):
    data={
        'services': Services.objects.all()
    }
    return render(request, "services.html",data)