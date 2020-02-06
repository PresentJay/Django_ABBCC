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


""" as in FBV, it'll be like this below """

""" def login_view(request):
    if request.method == "GET":
        pass
    elif request.method == 'POST':
        pass """
