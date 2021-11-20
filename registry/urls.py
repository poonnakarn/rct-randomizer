from django.urls import path
from registry import views

urlpatterns = [
    path("", views.screening, name="screening"),
    path("enroll_list/", views.enroll_list, name="enroll_list"),
    path("screened/", views.screened, name="screened"),
    path("enroll/<patient_id>", views.enroll_patient, name="enroll_patient"),
]
