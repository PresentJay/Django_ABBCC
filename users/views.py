from django.views import View
from django.shortcuts import render
from . import forms

# Create your views here.


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form,})

    def post(self, request):
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            # cleaned_data is result of cleaning on methods.
            # if clean-methods have not return, it removes data on result of cleaning

        return render(request, "users/login.html", {"form": form,})


""" as in FBV, it'll be like this below """

""" def login_view(request):
    if request.method == "GET":
        pass
    elif request.method == 'POST':
        pass """
