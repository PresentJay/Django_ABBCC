from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form,})

    def post(self, request):
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
            # cleaned_data is result of cleaning on methods.
            # if clean-methods have not return, it removes data on result of cleaning
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))

        return render(request, "users/login.html", {"form": form,})


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


""" as in FBV, it'll be like this below """

""" def login_view(request):
    if request.method == "GET":
        pass
    elif request.method == 'POST':
        pass """
