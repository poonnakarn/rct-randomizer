from django.contrib import admin
from django.urls import path
from registry import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("screening/", views.screening, name="screening"),
    # path("enroll/", views.enroll, name="enroll"),
]
