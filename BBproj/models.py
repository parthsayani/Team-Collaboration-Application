from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
# Create your models here.



class Timestamp(models.Model):
    Date = models.DateField(null=True)
    Logintime = models.TimeField()
    Logouttime = models.TimeField()
    userp = models.ForeignKey(User)




class Userprofile(models.Model):
    User=models.OneToOneField(User,related_name='profile')
    Designation = models.CharField(max_length=100, blank=True, null=True,choices=[('Intern', 'Intern'), ('Employee', 'Employee')])
    Salary = models.IntegerField(blank=True, default=0)

class Subject(models.Model):
    Subject_name=models.CharField(max_length=100)
    def __str__(self):
            return str(self.Subject_name)
    
class Work(models.Model):
    userpp=models.ManyToManyField(User,null=True,related_name='userpp')
    Subject = models.ForeignKey(Subject,max_length=100 ,related_name='subworks',on_delete=models.CASCADE)
    text = models.CharField(max_length=100,null=True)
    deadline = models.DateTimeField(null=True)
    def __str__(self):
        return str(self.text)

# class text_append(models.Model):
#     text=models.ForeignKey(Work,max_length=2000,related_name='textappend',null=True)
#     append=models.CharField(max_length=1000,null=True)

