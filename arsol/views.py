from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from os import link
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
import csv
import json
from arsol.models import University, Application


def university_views(request: HttpRequest) -> HttpResponse:
    context = {
        "universities": University.objects.all().values()
    }
    return render(request, "universities.html", context)


def send_email(request: HttpRequest, id_: int) -> HttpResponse:
    if request.method == "POST":
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
        university = University.objects.get(id__exact=id_)
        uni_name = university.name
        coach_email = university.coach_email
        uni_region = university.region
        uni_wtn = university.wtn
        uni_team = university.team

        application = Application(email=email,
                                  fname=fname,
                                  lname=lname,
                                  age=age,
                                  country=country,
                                  city=city,
                                  school=school,
                                  grad_m=grad_m,
                                  grad_y=grad_y,
                                  budget=budget,
                                  gpa=gpa,
                                  utr=utr,
                                  utr_link=utr_link,
                                  uni_name=uni_name,
                                  coach_email=coach_email,
                                  uni_region=uni_region,
                                  uni_wtn=uni_wtn,
                                  uni_team=uni_team
                                  ).save()

    context = {
        'university': University.objects.get(id__exact=id_)
    }
    return render(request, "universities.html", context)
