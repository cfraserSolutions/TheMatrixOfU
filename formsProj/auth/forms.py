from django import forms  
from django.forms import ModelForm

from .models import * 

import datetime

class SignupForm(forms.Form):
	firstname = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

class ImageUploadForm(forms.Form): 
	image = forms.ImageField(); 

class BloodPressureLogForm(forms.ModelForm):
	class Meta:
		model = BloodPressureLogModel 
		fields = ['date' , 'reading', 'heartRate' , 'pulse' ,]
		widgets =  {
		    	'date': forms.DateInput(attrs={'placeholder': datetime.date.today ,'class':'form_input'}),
			'reading': forms.TextInput(attrs={'placeholder': 'Blood Pressure Reading','class':'form_input'}),
			'heartRate': forms.TextInput(attrs={'placeholder': 'Heart Rate','class':'form_input'}),
			'pulse': forms.TextInput(attrs={'placeholder': 'Pulse','class':'form_input'}),
       		}

class PatientSummaryForm(forms.ModelForm):
	class Meta:
		model = PatientSummaryModel 
		fields =['dob' , 'homeContact' , 'cellContact' , 'bloodType' , 'healthCentre' , 'sandreGrande' , 'posGeneral' , 'mountHope' , 'scarborough'  , 'sanFernando' , 
				'nextOfKinName' , 'relationship' , 'address', 'kinHomeContact' , 'kinCellContact']
		widgets = {
			'dob': forms.DateInput(attrs={'placeholder': 'Birth Date' ,'class':'form_input'}),
			'homeContact': forms.TextInput(attrs={'placeholder': 'Home Number','class':'form_input'}),
			'cellContact': forms.TextInput(attrs={'placeholder': 'Cell Number','class':'form_input'}),
			'bloodType': forms.TextInput(attrs={'placeholder': 'Blood Type','class':'form_input'}),
			#need reg no. heading
			'healthCentre': forms.TextInput(attrs={'placeholder': 'Health Centre' ,'class':'form_input'}),
			'sangreGrande': forms.TextInput(attrs={'placeholder': 'Sangre Grande','class':'form_input'}),
			'posGeneral': forms.TextInput(attrs={'placeholder': 'Pos General','class':'form_input'}),
			'mountHope': forms.TextInput(attrs={'placeholder': 'Mount Hope','class':'form_input'}),
			'scarborough': forms.TextInput(attrs={'placeholder': 'Scarborough' ,'class':'form_input'}),
			'sanfernando': forms.TextInput(attrs={'placeholder': 'San Fernando','class':'form_input'}),
			# Need next of kin heading 
			
			'nextOfKinName': forms.TextInput(attrs={'placeholder': 'Next Of Kin Name','class':'form_input'}),
			'relationship': forms.TextInput(attrs={'placeholder': 'Relationship','class':'form_input'}),
			'address': forms.TextInput(attrs={'placeholder': 'Address' ,'class':'form_input'}),
			'KinHomeContact': forms.TextInput(attrs={'placeholder': 'Home Number','class':'form_input'}),
			'KinCellContact': forms.TextInput(attrs={'placeholder': 'Cell Number','class':'form_input'}),
		}



class DiagnosisHistoryForm(forms.ModelForm):
	class Meta:
		model= DiagnosisHistoryModel
		fields= ['date' , 'symptomsDescription' , 'diagnosis' , 'clinic' ,]
		widgets = {
			'date': forms.DateInput(attrs={'placeholder': 'Date' ,'class':'form_input'}),

			#change this to text area 
			'symptomsDescription': forms.TextInput(attrs={'placeholder': 'Description of Symptoms','class':'form_input'}),
			'diagnosis': forms.TextInput(attrs={'placeholder': 'Diagnosis','class':'form_input'}),
			'clinic': forms.TextInput(attrs={'placeholder': 'Clinic','class':'form_input'}),
			
		}

class AsthmaForm(forms.ModelForm):
	class Meta:
		model = AsthmaModel
		fields = ['date', 'attackType' , 'treatment', 'nurseName']
		
		widgets = {
			'date': forms.DateInput(attrs={'placeholder': 'Date' ,'class':'form_input'} ), 
			'attackType': forms.TextInput(attrs={'placeholder': 'Type of attack','class':'form_input'}),
			'treatment': forms.TextInput(attrs={'placeholder': 'What treatment was done','class':'form_input'}),
			'nurseName': forms.TextInput(attrs={'placeholder': 'Name of attending nurse','class':'form_input'}),
			
		}

class SurgeriesForm(forms.ModelForm):
	class Meta:
		model = SurgeriesModel
		fields = ['date', 'surgeonName' , 'surgeryType', 'comments']
		widgets = {
			'date': forms.DateInput(attrs={'placeholder': 'Date' ,'class':'form_input'}),
			'surgeonName': forms.TextInput(attrs={'placeholder': 'Type of attack','class':'form_input'}),
			'surgeryType': forms.TextInput(attrs={'placeholder': 'What treatment was done','class':'form_input'}),
			'comments': forms.TextInput(attrs={'placeholder': 'Name of attending nurse','class':'form_input'}),
			
		}  

class DangerousMedicationForm(forms.Form):
	class Meta:
		model = DangerousMedicationModel
		fields = ['date', 'medicationName' , 'effects', 'clinic']
		widgets = {
			'date': forms.DateInput(attrs={'placeholder': 'Date' ,'class':'form_input'}),
			'medicationName': forms.TextInput(attrs={'placeholder': 'Name of medication','class':'form_input'}),
			'effects': forms.TextInput(attrs={'placeholder': 'How you were affected','class':'form_input'}),
			'clinic': forms.TextInput(attrs={'placeholder': 'Clinic','class':'form_input'}),
			
		}  
   








 


