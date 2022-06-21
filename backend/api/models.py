from typing_extensions import Self
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
        dietdata1 = [
        ['1 CUP OATS','10','54', '5'],
        ['1/2 APPLE','0','14', '0'],
        ['5 BOILED EGG WHITES','20','0', '0'],
        ['1 WHOLE EGG','6','1', '5'],
        ['TOTAL CALORIES = 510','36g','69g', '10g']
    ]
        dietdata2 = [
      ['3 BREAD','6','45', '4'],
      ['1SP PEANUT BUTTER','4','4', '7'],
      ['0.8 scoop WHEY PROTEIN','20','1', '1'],
      ['WATER 240ML','0','0', '0'],
      ['TOTAL CALORIES = 428','30g','50g', '12g']
    ]
        dietdata3 = [
    ['240g BLACK CHANNA','16','44', '3'],
    ['1/2CUP RICE','4','20', '0'],
    ['COOKED IN1/2SP COCONUT OIL','0','0', '7'],
    ['MIX SALAD','0','0', '0'],
    ['TOTAL CALORIES = 426','20g','64g', '10g']
    ]
        data = {
        "dietdata1": dietdata1, 
        "dietdata2": dietdata2,
        "dietdata3": dietdata3
        }
        return data
    diet_plan = property(_get_diet_plan)

    def _get_exercise_plan(self):
        monday_data = [
        ['Superset','WARM UP 1. DB CURLS + DB KICK BACK DOWN (LIGHT WEIGHT)','2', '20-25', '0'],
        ['Superset','2A. CABLE CURLS 2B. TRICEPS PRESS DOWN','3-3', '12-10-8', '2MIN'],
        ['Superset','3A. PREACHER CURL 3B. OVERHEAD DB EXTENSION','5-5', '12-10-8', '2MIN'],
        ['Superset','4A. HIGH ANGLE CABLE CURL 4B. SINGLE HAND TRICEP EXT','5-5', '12-10-8', '2MIN'],
        ['Superset','5A. SINGLE HAND INWARD CURL 5B. TRICEP PUSHDOWN','2', '20-20', '2MIN']
    ]
        tuesday_data = [
        ['Superset','WARM UP 1. DB CURLS + DB KICK BACK DOWN (LIGHT WEIGHT)','2', '20-25', '0'],
        ['Superset','2A. CABLE CURLS 2B. TRICEPS PRESS DOWN','3-3', '12-10-8', '2MIN'],
        ['Superset','3A. PREACHER CURL 3B. OVERHEAD DB EXTENSION','5-5', '12-10-8', '2MIN'],
        ['Superset','4A. HIGH ANGLE CABLE CURL 4B. SINGLE HAND TRICEP EXT','5-5', '12-10-8', '2MIN'],
        ['Superset','5A. SINGLE HAND INWARD CURL 5B. TRICEP PUSHDOWN','2', '20-20', '2MIN']
    ]
        data = {
        "monday_data": monday_data,
        "tuesday_data":tuesday_data
        }
        return data

    if (bmi_status!= "Under weight"):
        exercise_plan = property(_get_exercise_plan)
    else:
        exercise_plan="none"




    def __str__(self):
        return self.name

