from django.db import models

# Create your models here.
class patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class doctor(models.Model):
    name=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name
    
    
class hospital (models.Model):
    pname=models.ForeignKey(patient,on_delete=models.CASCADE)
    dname=models.ForeignKey(doctor,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()        
    