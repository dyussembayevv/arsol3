"""
URL configuration for Tennis_recruiting_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.http import HttpRequest, HttpResponse, BadHeaderError, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path
from django.core.mail import send_mail
from arsol.models import Application, University
from arsol.views import university_views, send_email


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        email = request.POST.get("email", "")
        fname = request.POST.get("first_name", "")
        lname = request.POST.get("last_name", "")
        age = request.POST.get("age", "")
        country = request.POST.get("country", "")
        city = request.POST.get("city", "")
        school = request.POST.get("school", "")
        grad_m = request.POST.get("graduation_m", "")
        grad_y = request.POST.get("graduation_y", "")
        budget = request.POST.get("budget", "")
        gpa = request.POST.get("gpa", "")
        utr = request.POST.get("utr", "")
        utr_link = request.POST.get("utr_link", "")

        from_email = email
        recipient_list = ['vdyussembayev@gmail.com']
        subject = "Tennis Recruiting"
        message = f'''
        Dear Coach,

        My name is {fname} {lname}. I am {age} old. My UTR is {utr}. You can check out 
        my profile here - {utr_link}.

        I study at {school} in {city}, {country}. I am graduating in {grad_m}, {grad_y}. My budget is {budget},
        and my gpa is {gpa}.

        I am very interested in your university and your tennis program, as I believe I may 
        be a great fit both academically and athletically. 

        Thank you for your consideration.

        Sincerely,
        {fname}
        '''
        send_mail(subject, message, from_email, recipient_list)

    context = {
        "universities": University.objects.all().values()
    }
    return render(request, "index.html", context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('universities', university_views),
    path('send_email/<int:id_>', send_email)
]
