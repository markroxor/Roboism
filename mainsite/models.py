from django.db import models
from django.utils import timezone
import os
from django.utils.translation import ugettext_lazy as _
from datetime import date

from django import template
register = template.Library()

class Member(models.Model):
    year_choice = (
        ('First Year','First Year'),
        ('Second Year','Second Year'),
        ('Third Year','Third Year'),
        ('Final Year','Final Year'),
        ('Alumni','Alumni'),
    )
    pic = models.ImageField(upload_to='./mainsite/static/',blank=True)
    username = models.CharField(default="Username", max_length=20)
    name = models.CharField(default="Name", max_length=50, blank=True)
    email = models.EmailField()
    branch = models.CharField(default='Branch', blank=True, max_length=50)
    work = models.CharField(default="Company/University", max_length=50,blank=True)
    DOB = models.DateField(_("Date"), default=date.today)
    year = models.CharField(choices=year_choice, default="First Year", max_length=11)
    bio = models.TextField(default="Lorem ipsum sit dolot fuck this shit !",blank=True)
    linkedin = models.URLField(blank=True)
    resume = models.FileField(blank=True,upload_to='./mainsite/static')
    active = models.BooleanField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

    @property
    def resumeFilename(self,):
        return  os.path.basename(self.resume.name)

    @property
    def picFilename(self,):
        return  os.path.basename(self.pic.name)


class Project(models.Model):
    pic = models.ImageField(blank=True)
    name = models.CharField(default="Name", max_length=50)
    description = models.TextField(default="Shitty Project")
    github = models.URLField(blank=True)
    completed = models.BooleanField()
    contributers = models.CharField(max_length=100, default='dev')

    def __str__(self):
        return self.name

    def publish(self):
        self.save()

    @property
    def picFilename(self,):
        return  os.path.basename(self.pic.name)


class ExpoProject(models.Model):
    project1 = models.BooleanField()
    project2 = models.BooleanField()
    project3 = models.BooleanField()
    project4 = models.BooleanField()
