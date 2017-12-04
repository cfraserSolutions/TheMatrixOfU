# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import models as m 

# Create your models here.

class ImageModel(models.Model):
	image = models.ImageField(upload_to = 'auth/static/usr_images') 
	owner = models.ForeignKey(m.User , on_delete=models.CASCADE) 
	

class BloodPressureLogModel(models.Model):
	date = models.DateField()
	reading = models.CharField(max_length=30 )  	
	heartRate = models.CharField(max_length=20)
	pulse = models.CharField(max_length=20)
	owner = models.ForeignKey(m.User , on_delete=models.CASCADE) 
	
class PatientSummaryModel(models.Model):
    name = models.CharField(max_length = 55)
    dob = models.DateField() #date of birth
    homeContact = models.IntegerField()
    cellContact = models.IntegerField()
    bloodType = models.CharField(max_length=3)
    #Registration numbers by clinics
    healthCentre = models.CharField(max_length = 12)
    sandreGrande = models.CharField(max_length =12)
    posGeneral = models.CharField(max_length = 12)
    mountHope = models.CharField(max_length = 12)
    scarborough = models.CharField(max_length = 12)
    sanFernando = models.CharField(max_length = 12)
    #Diagnosed illness
    #promt user to enter in the form of  " asthma, diabetes, cancer"
    diagnosedIllness =models.CharField(max_length= 300)
    nextOfKinName = models.CharField(max_length = 55)
    relationship = models.CharField(max_length = 15)
    address = models.CharField(max_length = 90)
    kinHomeContact = models.IntegerField()
    kinCellContact = models.IntegerField()
    owner = models.ForeignKey(m.User , on_delete=models.CASCADE)


class DiagnosisHistoryModel(models.Model):
    date = models.DateField()
    symptomsDescription = models.CharField(max_length = 500)
    diagnosis = models.CharField(max_length=30)
    clinic = models.CharField(max_length=25)
    owner = models.ForeignKey(m.User  , on_delete=models.CASCADE)	

class DangerousMedicationModel(models.Model):
    date = models.DateField()
    medicationName = models.CharField(max_length=50)
    effects = models.CharField(max_length=500)
    clinic = models.CharField(max_length=25)
    owner = models.ForeignKey(m.User , on_delete=models.CASCADE)

class AsthmaModel(models.Model):
    date = models.DateField()
    attackType = models.CharField(max_length=30)
    treatment = models.CharField(max_length=200)
    nurseName = models.CharField(max_length=50)
    clinic = models.CharField(max_length=25)
    owner = models.ForeignKey(m.User , on_delete=models.CASCADE)

class SurgeriesModel(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    surgeonName = models.CharField(max_length=60)
    surgeryType = models.CharField(max_length=30)
    comments = models.CharField(max_length=600)
    clinic = models.CharField(max_length=25)
    owner = models.ForeignKey(m.User , on_delete=models.CASCADE)




