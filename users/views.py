from django.views import View
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from . import forms

# Create your views here.


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    # urls will be not called, so uses "lazy"
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)
            return redirect(reverse("core:home"))

        return super().form_valid(form)


# difference of this custom-view and loginview
# : loginview authenticates with 'username'.
# : but custom view from below authenticates with 'email'.
""" class LoginView(View):
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
 """


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


""" as in FBV, it'll be like this below """

""" def login_view(request):
    if request.method == "GET":
        pass
    elif request.method == 'POST':
        pass """


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    # urls will be not called, so uses "lazy"
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)

        user.verify_email()

        return super().form_valid(form)
