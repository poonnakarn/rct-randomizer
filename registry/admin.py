from django.contrib import admin
from .models import Sequence, Patient

class EnrollTime(admin.ModelAdmin):
    readonly_fields = ('time',)

admin.site.register(Sequence)
admin.site.register(Patient, EnrollTime)
# admin.site.register(Patient)
