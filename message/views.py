from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .models import RecievedMessage

# Create your views here.


def messagePage(request, username):
    if request.method == 'GET':
        if User.objects.filter(username=username).exists():
            context = {
                'username': User.objects.get(username=username)
            }
            return render(request, 'message/message.html', context)
        else:
            return HttpResponse(status=404)
    elif request.method == 'POST':
        context = {
            'username': User.objects.get(username=username)
        }
        msg = RecievedMessage(
            reciever_id=context['username'].id, message=request.POST['message'])
        msg.save()
        messages.success(request, 'message sent to ' +
                         context['username'].first_name)
        return redirect('../message/'+username)
    else:
        return HttpResponse(status=404)
