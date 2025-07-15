from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms  import SignUpForm

def frontpage(req):
    return render(req, 'frontpage.html')

def signup(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST)

        if form.is_valid():
            user =form.save()

            login(req, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(req, 'signup.html',{'form':form})