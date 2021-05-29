from django.shortcuts import render
from account.forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

# Handle login
#@login_required
def login(request):
    if request.method == 'POST':
        mylogin = LogInForm(request.POST)
        if mylogin.is_valid():
            email = mylogin.cleaned_data['email']
            password = mylogin.cleaned_data['password']
            if email == 'feroxadmin@gmail.com' and password == 'feroxadmin':
                return render(request, 'View.html')
    else:
        mylogin = LogInForm()
    return render(request, 'Signin.html', {'form': LogInForm})
