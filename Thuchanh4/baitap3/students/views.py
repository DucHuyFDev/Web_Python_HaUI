from django.shortcuts import render
from . import forms

# Create your views here.
def student_form_view(request):
    if request.method == "POST":
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=True)
            avg = (student.maths + student.physics + student.chemistry)/3
            return render(request, "success.html", {"student": student, "avg": avg})
    else:
        form = forms.StudentForm()

    return render(request, "input.html", {"form": form}) 