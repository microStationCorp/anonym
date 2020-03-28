from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='../')
def userhome(request):
    return render(request, 'userhome/page.html')
