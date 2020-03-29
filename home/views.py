from django.shortcuts import render, redirect

# Create your views here.


def homePage(request):
    if request.user.is_authenticated:
        return redirect('../user')
    return render(request, 'home/home.html')
