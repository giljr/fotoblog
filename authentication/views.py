from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from authentication import forms

from django.views.generic import View


## Class-based view implementation##############


# class LoginPage(View):
#     # a couple of variables which will be used between the two methods
#     # form_class = forms.LoginForm() <- do not exec here!
#     form_class = forms.LoginForm
#     template_name = 'authentication/login.html'

#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request, self.template_name, context={'form': form, 'message': message})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         message = ''
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#             # message = f'You are logged in as {user.username}'
#         else:
#             message = 'Login failed!'
#         return render(request, self.template_name, context={'form': form, 'message': message})


################################################

# 1) It handles the Get part of the request
# 2) We grab that login form
# 3) and we display it in the template by passing it into the context;
# 4) if the form is valid we authenticate and log in the user in.
# 5) What authenticate does is it returns the user if the credentials are valid
#    or none if not.


def logout_user(request):
    logout(request)
    return redirect('login')


# def login_page(request):
#     form = forms.LoginForm()
#     message = ''
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#             # message = f'You are logged in as {user.username}'
#         else:
#             message = 'Login failed!'
#     return render(request, 'authentication/login.html', context={'form': form, 'message': message})


# Create a Sign up Page (https://openclassrooms.com/en/courses/7107341-intermediate-django/7263818-create-a-sign-up-page#/id/r-7263642)


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # We then want to redirect to the home page after a successful signup
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})
