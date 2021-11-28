from django.db import models

# Create your models here.
class student3(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    def __str__(self):
        return str(self.pk)+" "+self.fname+" "+self.lname