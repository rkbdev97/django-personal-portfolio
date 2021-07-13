from django.db import models

# Create your models here.
class About(models.Model):
    name=models.CharField(max_length=50,verbose_name="Your Name")
    age=models.IntegerField(verbose_name="Your Age")
    dob=models.DateField(verbose_name="Date Of Birth")
    mobile=models.CharField(max_length=15,verbose_name="Your Mobile")
    email=models.EmailField(max_length=75,verbose_name="your email")
    city=models.CharField(max_length=50, verbose_name="Your City")
    website=models.CharField(max_length=40,verbose_name="your website")
    degree=models.CharField(max_length=40,verbose_name="Your degree")
    profile=models.CharField(max_length=40,verbose_name="Your Profile")
    shor_desc=models.TextField(max_length=200,verbose_name="Your Short Description")
    desc=models.TextField(max_length=600,verbose_name="About U")
    pimg=models.ImageField(upload_to ="about",verbose_name="Upload image")
class Meta:
    db_table="about"


class Skills(models.Model):
    tech=models.CharField(max_length=20,verbose_name="Add Your Skill")
    rate=models.IntegerField(verbose_name="Rate your self in %")
    desc=models.TextField(max_length=200,verbose_name="Skill description")
    class Meta:
        db_table="Skills"
class Education(models.Model):
    degree=models.CharField(max_length=50,verbose_name="Degree")
    year=models.CharField(max_length=20,verbose_name="Duration of Degree")
    university=models.CharField(max_length=75,verbose_name="Univercity name")
    desc=models.TextField(max_length=200,verbose_name="Education description")
    class Meta:
        db_table="education"

class Experience(models.Model):
    profile = models.CharField(max_length=50,verbose_name="Profile ")
    year = models.CharField(max_length=20,verbose_name="Total Experience ")
    company_name = models.CharField(max_length=75,verbose_name="Company Name ")
    desc = models.TextField(max_length=300,verbose_name="Exprience Description ")

    class Meta:
        db_table = "experience"

class Portfolio(models.Model):
    title = models.CharField(max_length=70,verbose_name="Portfolio Title ")
    desc = models.TextField(max_length=500,verbose_name="Portfolio Description ")
    image = models.ImageField(upload_to ="portfolio",verbose_name="Portfolio Image ")

    class Meta :
        db_table = "portfolio"

class Service(models.Model) :
    title = models.CharField(max_length=70,verbose_name="Portfolio Title ")
    desc = models.TextField(max_length=500,verbose_name="Portfolio Description ")

    class Meta :
        db_table = "services"