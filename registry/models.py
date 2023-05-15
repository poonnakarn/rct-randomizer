from django.db import models
from multiselectfield import MultiSelectField

INCLUSION_CHOICES = [
    ('in_age_more_than_18', '1)	Age ≥ 18 years'),
    ('in_drug_resistant_epilepsy',
     '2) Drug-resistant epilepsy'),
    ('in_stable_asm_1_month', '3) Stable dose of ASMs at least 1 month'),
]

EXCLUSION_CHOICES = [
    ('ex_refuse', '1) Refuse to participate'),
    ('ex_unable_eeg',
     '2) Unable to perform EEG recording e.g., due to skull defects'),
    ('ex_hearing_problem', '3) Hearing problem'),
    ('ex_progressive_neurological_disease',
     '4) Progressive neurological diseases e.g., Rasmussen encephalitis, mitochondrial disorders, inborn error of metabolisms, autoimmune-associated epilepsy'),
    ('ex_unable_songs', '5) Unable to tolerate listening to the songs e.g., intellectual disability, behavioral problems'),
    ('ex_interictal_discharge_less_than_4_hours',
     '6) Interictal epileptiform discharges less than 10 during 4-hour baseline period'),
    ('ex_atrial_fibrillation', '7) History of atrial fibrillation'),
    ('ex_pacemaker', '8) With pacemaker placement'),
]


class Patient(models.Model):
    hospital_number = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length=20, blank=False)
    time = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=10, blank=False)

    inclusion = MultiSelectField(choices=INCLUSION_CHOICES, blank=True)
    exclusion = MultiSelectField(choices=EXCLUSION_CHOICES, blank=True)

    eligible = models.BooleanField(default=False)
    proficient = models.BooleanField(null=True, default=None)
    enrolled = models.BooleanField(default=False)

    def __str__(self):
        return self.hospital_number


class Sequence(models.Model):
    arm = models.CharField(max_length=10)
    patient = models.OneToOneField(
        Patient, null=True, default=None, on_delete=models.CASCADE, related_name='sequence', blank=True)
    time = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        return self.arm
