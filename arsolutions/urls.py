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
from django.contrib import admin
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse, BadHeaderError, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path

from arsol.models import Application, University
from arsol.views import university_views, send_email


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        email = request.POST.get("email", "")
        fname = request.POST.get("first_name", "")
        lname = request.POST.get("last_name", "")
        age = request.POST.get("age", "")
        country = request.POST.get("country", "")
        achievements = request.POST.get("achievements", "")

        application = Application(email=email, fname=fname, lname=lname, age=age, country=country, achievements=achievements).save()

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
