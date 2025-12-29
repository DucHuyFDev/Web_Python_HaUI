from django.http import JsonResponse
from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.

def student_form_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return JsonResponse(data)
    else:
        form = SignUpForm()
    return render(request, "infor.html", {"form": form})
