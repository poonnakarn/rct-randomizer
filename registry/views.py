from django.shortcuts import redirect, render
import csv
import io
from .models import Sequence, Patient
from django.contrib import messages
from .forms import PatientForm
import datetime


def screening(request):

    template = "screening.html"
    # data = Sequence.objects.all().order_by('id')
    patient_form = PatientForm()

    context = {
        "welcome_text": "ยินดีต้อนรับสู่ CCEC RCT Screening",
        # 'sequences': data,
        'patient_form': patient_form,
    }

    # handling GET
    if request.method == "GET":
        return render(request, template, context)

    # handling POST
    if request.method == "POST":

        # all_sequences = Sequence.objects.all()
        form = PatientForm(request.POST or None)
        # arm = None
        # hn = None
        if form.is_valid():
            if len(form.instance.inclusion) == 3 and len(form.instance.exclusion) == 0:
                form.instance.eligible = True
                messages.success(request, 'ผู้ป่วย ' +
                                 form.instance.hospital_number + ' ผ่านการ Screening (Success)')
            else:
                form.instance.eligible = False
                messages.error(request, 'ผู้ป่วย ' +
                               form.instance.hospital_number + ' ไม่ผ่านการ Screening (Failed)')

            form.save()

        # for sequence in all_sequences:
        #     if not sequence.patient:
        #         p = form.save()
        #         sequence.patient = p
        #         arm = sequence.arm
        #         hn = p.hospital_number
        #         sequence.save()
        #         break

        return redirect("screening")


def enroll_list(request):

    template = "enroll_list.html"
    data = Sequence.objects.all().order_by('id')

    context = {
        "welcome_text": "ตารางการ Randomization",
        'sequences': data,
    }

    # handling GET
    if request.method == "GET":
        return render(request, template, context)

    # handling POST
    if request.method == "POST":

        csv_file = request.FILES.get('file', False)

        if not csv_file:
            messages.error(request, "Please upload CSV file!")
            return redirect("enroll_list")

        if not csv_file.name.endswith('.csv'):
            messages.error(request, "Only CSV files are supported!")
            return redirect("enroll_list")

        data_set = csv_file.read().decode('UTF-8')

        io_string = io.StringIO(data_set)

        # skip the header
        next(io_string)

        for row in csv.reader(io_string, delimiter=','):
            p = Sequence.objects.create(
                arm=row[1],
                patient=None
            )

        messages.success(request, "Random sequence added!")

        return redirect("enroll_list")


def screened(request):
    template = "screened.html"
    data = Patient.objects.order_by('-eligible', 'enrolled', '-time')

    context = {
        "welcome_text": "รายชื่อผู้ป่วยที่ผ่านการคัดกรอง",
        'patients': data,
    }

    # handling GET
    return render(request, template, context)


def enroll_patient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)

    all_sequences = Sequence.objects.all().order_by('id')

    for sequence in all_sequences:
        if not sequence.patient:
            sequence.patient = patient
            sequence.time = datetime.datetime.now()
            arm = sequence.arm
            hn = patient.hospital_number
            sequence.save()

            patient.enrolled = True
            patient.save()

            messages.success(request, 'ผู้ป่วย ' + hn +
                             ' ถูกจัดเข้ากลุ่ม ' + arm)

            break

    return redirect("screened")
