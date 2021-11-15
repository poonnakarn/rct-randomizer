from django.shortcuts import redirect, render
import csv, io
from .models import Sequence, Patient
from django.contrib import messages
from .forms import PatientForm
import logging


def home(request):

    template = "home.html"
    data = Sequence.objects.all()
    patient_form = PatientForm()

    context = {
        "welcome_text": "ยินดีต้อนรับสู่ CCEC RCT Registry",
        'sequences': data,
        'patient_form': patient_form,
    }

    # handling GET
    if request.method == "GET":
        return render(request, template, context)

    
    # handling POST
    if request.method == "POST":
        if 'addcsv' in request.POST:
            csv_file = request.FILES['file']

            if not csv_file.name.endswith('.csv'):
                messages.error(request, "Only CSV files are supported!")
                return redirect("home")

            data_set = csv_file.read().decode('UTF-8')

            io_string = io.StringIO(data_set)

            # skip the header
            next(io_string)

            for row in csv.reader(io_string, delimiter=','):
                p = Sequence.objects.create(
                    arm = row[1],
                    patient = None
                )

            messages.success(request, "Added random sequence!")

            return redirect("home")
        elif 'addpatient' in request.POST:

            all_sequences = Sequence.objects.all()
            form = PatientForm(request.POST or None)
            arm = None
            hn = None

            for sequence in all_sequences:
                logging.debug(sequence.patient)
                if not sequence.patient:
                    p = form.save()
                    sequence.patient = p
                    arm = sequence.arm
                    hn = p.hospital_number
                    sequence.save()
                    break
            
            messages.success(request, "Patient " + hn + " was enrolled to "+arm+" arm!")
            return redirect("home")


            



