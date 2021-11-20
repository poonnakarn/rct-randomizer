from django.db import models
from multiselectfield import MultiSelectField

INCLUSION_CHOICES = [
    ('in_epilepsy', '1)	ผู้ป่วยที่ได้รับการวินิจฉัยโรคลมชักและ/หรือญาติผู้ดูแลผู้ป่วยใกล้ชิด'),
    ('in_freq_morethan_one',
     '2) มีความถี่ในการชักมากกว่าหรือเท่ากับ 1 ครั้งต่อเดือนในช่วง 1 เดือนที่ผ่านมา'),
    ('in_age_morethan_eighteen', '3) อายุตั้งแต่ 18 ปีขึ้นไป'),
]

EXCLUSION_CHOICES = [
    ('ex_medical_condition', '1) ผู้ป่วยที่มีระดับสติปัญญาบกพร่องรุนแรงหรือมีพัฒนาการช้า, ผู้ป่วยที่มีโรคทางจิตเวชรุนแรง (psychosis), PNES, ผู้ป่วยที่มีโรคประจำตัวรุนแรง (เช่นเนื้องอก, กระดูกหัก), ผู้ป่วยที่ไม่สามารถดูแลตนเองได้'),
    ('ex_not_android',
     '2) ไม่ได้ใช้ Android'),
]


class Patient(models.Model):
    hospital_number = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length=20, blank=False)
    time = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=10, blank=False)

    inclusion = MultiSelectField(choices=INCLUSION_CHOICES, blank=True)
    exclusion = MultiSelectField(choices=EXCLUSION_CHOICES, blank=True)

    eligible = models.BooleanField()

    def __str__(self):
        return self.hospital_number


class Sequence(models.Model):
    arm = models.CharField(max_length=10)
    patient = models.OneToOneField(
        Patient, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.arm
