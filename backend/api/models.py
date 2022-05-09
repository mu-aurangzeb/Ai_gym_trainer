from unicodedata import name
from django.db import models
from jsonfield import JSONField

# Create your models here.
   # list =(id,'name','age','gender','weight','height','created_on','username','password')


class User_info (models.Model):
    id = models.AutoField(primary_key=True)
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight= models.PositiveIntegerField()
    height= models.PositiveIntegerField()
    created_on=models.DateTimeField("created on",auto_now_add=True)
    #username=models.CharField(max_length=50,unique=True)
    #password = models.CharField(max_length=8)
    #plan=JSONField(max_length=1000 ,null=True)
    #exercise_plan=JSONField(max_length=1000 ,null=True)

    def _get_bmi(self):
        weight_kg=self.weight
        height_cm=self.height
        bmi=round((weight_kg/(height_cm)**2)*10000,1)
        return bmi
    bmi = property(_get_bmi)

    def _get_bmi_status(self):
        bmi_status="Undefined"
        if (self.bmi<18.5):
            bmi_status="Under weight"
            return(bmi_status)
        elif((self.bmi>=18.5) and (self.bmi <=24.9)):
            bmi_status="normal"
            return(bmi_status)
        elif(self.bmi>=25.0 and self.bmi <=29.9):
            bmi_status="over weight"
            return(bmi_status)
        else:
            bmi_status="obese"
            return(bmi_status)
        #return bmi_status
    bmi_status = property(_get_bmi_status)


    def _get_diet_plan(self):
        data = {"age": self.age,
        "weight": self.weight,
        "height": self.height,
        "gender": self.gender}
        "Returns the person's full name."
        return data
    diet_plan = property(_get_diet_plan)

    def _get_exercise_plan(self):
        data = {"age": self.age,
        "weight": self.weight,
        "height": self.height,
        "gender": self.gender}
        "Returns the person's full name."
        return data
    exercise_plan = property(_get_exercise_plan)




    def __str__(self):
        return self.name

