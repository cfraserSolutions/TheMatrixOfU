from django.conf.urls import url 

from django.contrib.auth import views as auth_views
from . import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r"^signup/", views.signup, name="signup"),
	url(r"^$" , views.home , name="index"), 
	url(r"^home" , views.home),
	url(r"^login/" , auth_views.login , name="login"),
	url(r"^logout/" , auth_views.logout , name="login"),
	url(r"^upload/", views.upload, name="upload"), 

	url(r'^journal/edit/patientSummary/$' , views.JournalAddBP , name="bp"),	
	
	#Add urls
	url(r'^journal/add/bp/$' , views.JournalAddBP , name="bp"),
	url(r'^journal/add/diagnosisHistory/$' , views.JournalAddDiagnosisHistory , name="diagnoses"),
	url(r'^journal/add/surgeries/$' , views.JournalAddSurgeries , name="surgeries"),
	url(r'^journal/add/asthma/$' , views.JournalAddAsthma , name="asthma"),
	url(r'^journal/add/dangerousMedication/$' , views.JournalAddDangerousMedication , name="DangerousMedication"),
	url(r'^journal/add/$', views.JournalAddCategories , name="add"), 
	
	#View urls
	url(r'^journal/view/diagnosisHistory/$' , views.JournalViewDiagnosisHistory , name="vdiagnoseshistory"),
	url(r'^journal/view/dangerousMedication/$' , views.JournalViewDangerousMedication , name="vdangerousmedication"),	
	url(r'^journal/view/bp/$' , views.JournalViewBP , name="vbp"),
	url(r'^journal/view/asthma/$' , views.JournalViewAsthma , name="vasthma"),
	url(r'^journal/view/surgeries/$' , views.JournalViewSurgeries , name="vsurgeries"),

	#Detail view urls
	url(r'^journal/view/diagnosisHistory/(?P<id>[0-9]+)$' , views.JournalViewDiagnosisHistoryDetails , name="vdiagnosishistoryd"),
	url(r'^journal/view/dangerousMedication/(?P<id>[0-9]+)$' , views.JournalViewDangerousMedicationDetails , name="vdangerousmedicationd"),
	url(r'^journal/view/bp/(?P<id>[0-9]+)/$' , views.JournalViewBPDetails , name="vbp"),	
	url(r'^journal/view/asthma/(?P<id>[0-9]+)$' , views.JournalViewAsthmaDetails , name="vasthmad"),
	url(r'^journal/view/surgeries/(?P<id>[0-9]+)$' , views.JournalViewSurgeriesDetails , name="vsurgeriesd"),
	url(r'^journal/view/$' , views.JournalView, name="view"), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

