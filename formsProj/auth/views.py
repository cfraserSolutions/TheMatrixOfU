# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
#from forms import SignupForm

from django.contrib.auth import login , authenticate , models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import *
from .models import *

def signup(request):
	if request.method == 'GET' :
		form = UserCreationForm()
		return render(request , "signup.html" , {"form" : form})
	else:
		form  = UserCreationForm(request.POST)
	
		if form.is_valid():
			form.save()
			firstname = form.cleaned_data.get("username")
			raw_password = form.cleaned_data.get("password1")
			user = authenticate(username=firstname , password=raw_password)
			
			login(request , user)
			return redirect("/home")
		else:
			form = UserCreationForm()
			return render(request , "signup.html" , {"christians_form" : form})



def home(request):
	if request.user.is_authenticated():
		upload_form = ImageUploadForm()	
		
		images = ImageModel.objects.filter(owner=request.user)
		paths = []
		for image in images :
			p = image.image.path ; 
			sub = p[p.find("/static"):]  # !!!!!!!!!!!This is a TEMPORARY hack  do the right thing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
			paths.append(sub) ;  

		return render(request , "index.html" , {"name" : request.user.id, "form": upload_form, "image_paths": paths})
	else : 
		return HttpResponse(
			"you are not logged in , <a href='login'>Login</a> or <a href='signup'>Signup</a>"
		)
		


def upload(request): 
	form = ImageUploadForm(request.POST, request.FILES) ;
	if form.is_valid() : 
		image = ImageModel(image=form.cleaned_data["image"], owner = request.user); 
		image.save(); 
	
	return HttpResponse("Success") ; 


def JournalAddCategories(request):
	return render(request, "categories.html" , {} ) ; 

def JournalAddGeneral(request) : 
	return render(request , "new_general.html" , {})

#PATIENT SUMMARY !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def JournalAddPatientSummary(request):
	if request.user.is_authenticated():
		if request.method == 'GET' :
			patient_form = BloodPressureLogForm()
			return render(request , "new_bp.html" , {"form" : bp_form})
		else:
			patient_form  = PatientSummaryForm(request.POST)


			if patient_form.is_valid():
				entry = BloodPressureLogModel(date=bp_form.cleaned_data["date"] , time=bp_form.cleaned_data["time"] , heartRate=bp_form.cleaned_data["heartRate"] ,pulse=bp_form.cleaned_data["pulse"] , owner=request.user) ; 	
				entry.save(); 
			
				return HttpResponse("Success"); 
			else:
				bp_form = BloodPressureLogForm()
				return render(request , "new_bp.html" , {"form" : bp_form})
	else:
		return HttpResponse("Not authenticated"); 	

#BLOOD PRESSURE !!!!!!!!!!!!!!!!!!!!!!!!!!!
def JournalAddBP(request) :
	if request.user.is_authenticated():
		if request.method == 'GET' :
			bp_form = BloodPressureLogForm()
			return render(request , "new_bp.html" , {"form" : bp_form})
		else:
			bp_form  = BloodPressureLogForm(request.POST)


			if bp_form.is_valid():
				entry = BloodPressureLogModel(date=bp_form.cleaned_data["date"] , heartRate=bp_form.cleaned_data["heartRate"] ,pulse=bp_form.cleaned_data["pulse"] , owner=request.user) ; 	
				entry.save(); 
			
				return HttpResponse("Success"); 
			else:
				bp_form = BloodPressureLogForm()
				return render(request , "new_bp.html" , {"form" : bp_form})
	
	else:
		return HttpResponse("Not authenticated"); 

def JournalViewBP(request):
	#get all blood pressure logs from the database 
	logs = BloodPressureLogModel.objects.filter(owner=request.user); 
	class dateID():	
		date =""
		id= ""
		def __init__(self,date,id):
			self.date = date
			self.id= id
		
	inst = [] 
	for log in logs : 
		temp = dateID(log.date,log.id)
		inst.append(temp) ; 
	
	return render(request , "list.html" , {"dateid":inst, "category": "bp"}) ; 

def JournalViewBPDetails(request , id):
	log = BloodPressureLogModel.objects.get(id=id , owner=request.user); 

	class TableEntry : 
		field=""
		value = "" ; 
		def __init__(self , field , value ): 
			self.field = field 
			self.value = value  

	table = []

	for f in BloodPressureLogModel._meta.get_fields() : 
		table.append(TableEntry(f.name , getattr(log , f.name)));

		

	return render(request , "details.html" , {"table" : table}) 


def JournalAddAsthma(request) :
	if request.user.is_authenticated():
		if request.method == 'GET' :
			asthma_form = AsthmaForm()
			return render(request , "new_form.html" , {"form" : asthma_form})
		else:
			asthma_form  = AsthmaForm(request.POST)


			if asthma_form.is_valid():
				entry = AsthmaModel(date=asthma_form.cleaned_data["date"] , attackType=asthma_form.cleaned_data["attackType"] ,treatment=asthma_form.cleaned_data["treatment"] , owner=request.user) ; 	
				entry.save(); 
			
				return HttpResponse("Success"); 
			else:
				asthma_form = AsthmaForm()
				return render(request , "new_form.html" , {"form" : asthma_form})
	
	else:
		return HttpResponse("Not authenticated");

def JournalViewAsthma(request):
	#get all blood pressure logs from the database 
	logs = AsthmaModel.objects.filter(owner=request.user); 
	class dateID():	
		date =""
		id= ""
		def __init__(self,date,id):
			self.date = date
			self.id= id
		
	inst = [] 
	for log in logs : 
		temp = dateID(log.date,log.id)
		inst.append(temp) ; 
	
	return render(request , "list.html" , {"dateid":inst, "category": "asthma"}) ;

def JournalViewAsthmaDetails(request , id):
	log = AsthmaModel.objects.get(id=id , owner=request.user); 

	class TableEntry : 
		field=""
		value = "" ; 
		def __init__(self , field , value ): 
			self.field = field 
			self.value = value  

	table = []

	for f in AsthmaModel._meta.get_fields() : 
		table.append(TableEntry(f.name , getattr(log , f.name)));

		

	return render(request , "details.html" , {"table" : table}) 

 

#SURGERIES !!!!!!!!!!!!!!!!!!
def JournalAddSurgeries(request) :
	if request.user.is_authenticated():
		if request.method == 'GET' :
			surgeries_form = SurgeriesForm()
			return render(request , "new_form.html" , {"form" : surgeries_form})
		else:
			surgeries_form  = SurgeriesForm(request.POST)


			if surgeries_form.is_valid():
				entry = SurgeriesModel(date=surgeries_form.cleaned_data["date"] , surgeonName=surgeries_form.cleaned_data["surgeonName"] ,surgeryType=surgeries_form.cleaned_data["surgeryType"] ,comments=surgeries_form.cleaned_data["comments"] , owner=request.user) ; 	
				entry.save(); 
			
				return HttpResponse("Success"); 
			else:
				surgeries_form = SurgeriesForm()
				return render(request , "new_form.html" , {"form" : surgeries_form})
	
	else:
		return HttpResponse("Not authenticated");

#DIAGNOSIS HISTORY !!!!!!!!!!!!!!!!!!!!!!!!!!	
def JournalAddDiagnosisHistory(request) :
	if request.user.is_authenticated():
		if request.method == 'GET' :
			diagnosis_history_form = DiagnosisHistoryForm()
			return render(request , "new_form.html" , {"form" : diagnosis_history_form})
		else:
			diagnosis_history_form  = DiagnosisHistoryForm(request.POST)


			if diagnosis_history_form.is_valid():
				entry = DiagnosisHistoryModel(date=diagnosis_history_form.cleaned_data["date"] , symptomsDescription=diagnosis_history_form.cleaned_data["surgeonName"] ,diagnosis=diagnosis_history_form.cleaned_data["surgeryType"] ,clinic=diagnosis_history_form.cleaned_data["comments"] , owner=request.user) ; 	
				entry.save(); 
			
				return HttpResponse("Success"); 
			else:
				diagnosis_history_form = DiagnosisHistoryForm()
				return render(request , "new_form.html" , {"form" : diagnosis_history_form})
	
	else:
		return HttpResponse("Not authenticated");

def JournalViewDiagnosisHistory(request):
	logs = DiagnosisHistoryModel.objects.filter(owner=request.user); 
	class dateID():	
		date =""
		id= ""
		def __init__(self,date,id):
			self.date = date
			self.id= id
		
	inst = [] 
	for log in logs : 
		temp = dateID(log.date,log.id)
		inst.append(temp) ; 
	
	return render(request , "list.html" , {"dateid":inst, "category": "diagnosisHistory"}) ;


#DANGEROUS MEDICATION !!!!!!!!!!!!!!!!
def JournalAddDangerousMedication(request):
	if request.user.is_authenticated():
		if request.method == 'GET' :
			dangerous_medication_form = DiagnosisHistoryForm()
			return render(request , "new_form.html" , {"form" : dangerous_medication_form})
		else:
			dangerous_medication_form  = DangerousMedicationForm(request.POST)


			if dangerous_medication_form.is_valid():
				entry = DangerousMedicationModel(date=dangerous_medication_form.cleaned_data["date"] , medicationName=dangerous_medication_form.cleaned_data["medicationName"] ,effects=dangerous_medication_form.cleaned_data["effects"] ,clinic=dangerous_medication_form.cleaned_data["comments"] , owner=request.user) ; 	
				entry.save(); 
			
				return HttpResponse("Success"); 
			else:
				dangerous_medication_form = DangerousMedicationForm()
				return render(request , "new_form.html" , {"form" : dangerous_medication_form})
	
	else:
		return HttpResponse("Not authenticated");

def JournalAddDental(request) : 
	return render(request , "new_entry.html" , {})

def JournalView(request) : 
	return render(request , "categories.html" , {}) ;  



