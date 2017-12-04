from django.shortcuts import render

# Create your views here.
def PatientSummaryFormView(request): 
	form  = PatientSummaryForm(request.POST)
	
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get("username")
			raw_password = form.cleaned_data.get("password1")
			user = authenticate(username=firstname , password=raw_password)
			login(request , user)
			return redirect("/home")
		else:
			form = PatientSummaryForm()
			return render(request , "patientSummary.html" , {"form" : form})
 