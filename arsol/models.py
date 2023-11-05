from django.db import models

# Create your models here.


class Application(models.Model):
    email = models.EmailField(max_length=255, blank=False, null=False, default="")
    fname = models.CharField(max_length=255, blank=False, null=False, default="")
    lname = models.CharField(max_length=255, blank=False, null=False, default="")
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=255, blank=False, null=False, default="")
    city = models.CharField(max_length=255, blank=False, null=False, default="")
    school = models.CharField(max_length=255, blank=False, null=False, default="")
    grad_m = models.CharField(max_length=255, blank=False, null=False, default="")
    grad_y = models.CharField(max_length=255, blank=False, null=False, default="")
    budget = models.IntegerField(default=0)
    gpa = models.CharField(max_length=255, blank=False, null=False, default="")
    utr = models.CharField(max_length=255, blank=False, null=False, default="")
    utr_link = models.URLField(max_length=255, blank=False, null=False, default="")
    uni_name = models.CharField(max_length=255, blank=False, null=False, default="")
    coach_email = models.EmailField(max_length=255, blank=False, null=False, default="")
    uni_region = models.CharField(max_length=255, blank=False, null=False, default="")
    uni_wtn = models.CharField(max_length=255, blank=False, null=False, default="")
    uni_team = models.CharField(max_length=255, blank=False, null=False, default="")

    def __str__(self):
        return f"{self.fname} {self.lname}, age: {self.age}, country: {self.country}"


class University(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, default="")
    logo = models.CharField(max_length=1000, blank=False, null=False, default="")
    team = models.CharField(max_length=1000, blank=False, null=False, default="")
    division = models.CharField(max_length=255, blank=False, null=False, default="")
    conference = models.CharField(max_length=255, blank=False, null=False, default="")
    region = models.CharField(max_length=255, blank=False, null=False, default="")
    wtn = models.CharField(max_length=255, blank=False, null=False, default="")
    coach_name = models.CharField(max_length=255, blank=False, null=False, default="")
    coach_email = models.EmailField(max_length=255, blank=False, null=False, default="")

    def __str__(self):
        return f"{self.name}, Division: {self.division}, WTN: {self.wtn}"