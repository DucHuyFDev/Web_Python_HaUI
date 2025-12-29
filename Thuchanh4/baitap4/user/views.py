from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def user_form_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            gioitinh_text = data["gioitinh"]
            gioitinh_choose = dict(form.fields["gioitinh"].choices)[gioitinh_text]
            choices_sothich = dict(form.fields["sothich"].choices)
            sothich_choose = ", ".join(choices_sothich[x] for x in data["sothich"])
            return render(request, "success.html", {"data": data, "gioitinh": gioitinh_choose, "sothich": sothich_choose})
    else:
        form = UserForm()
    return render(request, "survey.html", {"form": form})

