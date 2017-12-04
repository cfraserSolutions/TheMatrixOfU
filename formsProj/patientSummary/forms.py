from django import forms

class SignupForm(forms.Form):
	firstname = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

class ImageUploadForm(forms.Form): 
	image = forms.ImageField(); 

class PatientSummaryForm(forms.Form):
    name = forms.CharField(max_length = 55)
    dob = forms.DateField(auto_now=False, auto_now_add=False) #date of birth
    age = forms.Integerfield()
    homeContact = forms.Integerfield(max_value=99999999999,min_value=10000000000)
    cellContact = forms.Integerfield(max_value=99999999999,min_value=10000000000)
    bloodType = forms.CharField(max_length=3)
    #Registration numbers by clinics
    healthCentre = forms.CharField(max_length = 12)
    sandreGrande = forms.CharField(max_length =12)
    posGeneral = forms.CharField(max_length = 12)
    mountHope = forms.CharField(max_length = 12)
    scarbrough = forms.CharField(max_length = 12)
    sanFernando = forms.CharField(max_length = 12)
    #Diagnosed illness
    #promt user to enter in the form of  " asthma, diabetes, cancer"
    diagnosedIllness =forms.CharField(max_length= 300)
    nextOfKinName = forms.CharField(max_length = 55)
    relationship = forms.CharField(max_length = 15)
    address = forms.CharField(max_length = 90)
    kinHomeContact = forms.Integerfield(max_value=99999999999,min_value=10000000000)
    kinCellContact = forms.Integerfield(max_value=99999999999,min_value=10000000000)

class DiagnosisHistoryForm(forms.Form):
    date = forms.DateField(auto_now=False, auto_now_add=False)
    symptomsDescription = forms.CharField(max_length = 500)
    diagnosis = forms.CharField(max_length=30)
    doctorclinic(max_length=70)

class DangerousMedicationForm(forms.Form):
    date = forms.DateField(auto_now=False, auto_now_add=False)
    medicationName = forms.CharField(max_length=50)
    effects = forms.CharField(max_length=500)

class AllergyForm(forms.Form):
    date = forms.DateField(auto_now=False, auto_now_add=False)
    allergyTrigger = forms.CharField(max_length=50) #food ingredient or environmental trigger to your allergy
    effects = forms.CharField(max_length=500)
    medicationUsed = forms.CharField(max_length=50)

class MedicationJournalForm(forms.form):
    date = forms.DateField(auto_now=False, auto_now_add=False)
    medicationName = forms.CharField(max_length=50)    
    dosage = forms.CharField(max_length=15)  
    givenBy = forms.CharField(max_length=30)# doctor who prescribed it
    startDate =  forms.DateField(auto_now=False, auto_now_add=False) # when you started taking
    StopDate =  forms.DateField(auto_now=False, auto_now_add=False) # when you stopped taking
    
class EmergenyVisitsForm(forms.Form):
    date = forms.DateField(auto_now=False, auto_now_add=False)
    doctorName = forms.CharField(max_length=30)
    clinicName = forms.CharField(max_length=50)
    comments = forms.CharField(max_length=500)
    dischargeDate = forms.DateField(auto_now=False, auto_now_add=False)

class FollowUpSheetForm(forms.Form):
    date = forms.DateField(auto_now=False, auto_now_add=False)
    notes = forms.CharField(max_length=500)

class BloodPressureLogForm(forms.Form):
    date = forms.DateField(auto_now=False, auto_now_add=False)
    time = forms.TimeField()
    reading = forms.CharField(max_length=30)  
    heartRate = forms.CharField(max_length=20)
    pulse = forms.CharField(max_length=20)

class Asthmaform(forms.Form):
    date = forms.DateField(auto_now=False, auto_now_add=False)
    attackType = forms.CharField(max_length=30)
    treatment = forms.CharField(max_length=200)
    nurseName = forms.CharField(max_length=50)

class DentalRecordsForm(forms.Form):
    date = forms.DateField(auto_now=False, auto_now_add=False)
    dentistName = forms.CharField(max_length=50)
    procedureDone = forms.CharField(max_length=50)
    comments = forms.CharField(max_length=300)

class SurgeriesForm(forms.Form):
    date = forms.DateField(auto_now=False, auto_now_add=False)
    surgeonName = forms.CharField(max_length=60)
    surgeryType = forms.CharField(max_length=30)
    comments = forms.CharField(max_length=600)
