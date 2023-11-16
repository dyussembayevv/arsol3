from django.core.mail import send_mail
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
from mailersend import emails



def university_views(request: HttpRequest) -> HttpResponse:
    context = {
        "universities": University.objects.all().values()
    }
    return render(request, "universities.html", context)


def send_email(request: HttpRequest, id_: int) -> HttpResponse:
    mail_body = {}
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

        subject = 'Tennis Recruiting'
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
        from_email = email  # Replace with your sender email
        recipient_list = ['vdyussembayev@gmail.com']  # Replace with the recipient's email address

        try:
            send_mail(subject, message, from_email, recipient_list)
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
                                      utr_link=utr_link
                                      ).save()
            return HttpResponse('Email sent successfully!')

        except Exception as e:
            return HttpResponse(f'Error sending email: {str(e)}')
        #################

        mail_from = {
            "name": f'{fname} {lname}',
            "email": email,
        }

        recipients = [
            {
                "name": "Valikhan Dyussembayev",
                "email": "vdyussembayev@gmail.com",
            }
        ]

        reply_to = [
            {
                "name": "Name",
                "email": "reply@domain.com",
            }
        ]
        mailer.set_mail_from(mail_from, mail_body)
        mailer.set_mail_to(recipients, mail_body)
        mailer.set_subject("Tennis Recruiting", mail_body)
        mailer.set_html_content("", mail_body)
        mailer.set_plaintext_content(f'''
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
                ''', mail_body)
        mailer.set_reply_to(reply_to, mail_body)

        mailer.send(mail_body)
        print(mailer.send(mail_body))
    context = {
        'university': University.objects.get(id__exact=id_)
    }
    return render(request, "universities.html", context)
