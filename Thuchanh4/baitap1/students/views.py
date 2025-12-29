from django.shortcuts import render
from . import forms

# Create your views here.
def student_form_view(request):
    if request.method == "POST":
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            khoa_choose = data["khoa"]
            khoa_text = dict(form.fields["khoa"].choices)[khoa_choose]
            return render(request, "success.html", {"data": data, "khoa": khoa_text})
    else:
        form = forms.StudentForm()
    return render(request, "input.html", {"form": form})
