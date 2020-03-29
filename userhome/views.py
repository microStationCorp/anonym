from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from message.models import RecievedMessage
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url='../')
def userhome(request):
    msgs = RecievedMessage.objects.filter(reciever__id=request.user.id).order_by('-dateOfPost')
    context = {
        'msgs': msgs,
        'username': request.user.username,
        'fname': request.user.first_name,
        'lname': request.user.last_name,
    }
    return render(request, 'userhome/page.html', context)
