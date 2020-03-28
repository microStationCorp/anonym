from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse

# Create your views here.


def userlogin(request):
    if request.method == "POST" and request.is_ajax():
        usr = request.POST['usr']
        passw = request.POST['pass']

        user = authenticate(request, username=usr, password=passw)

        if user is not None:
            login(request, user)
            context = {
                'usr': True
            }
        else:
            context = {
                'usr': False
            }
        return JsonResponse(context)
    else:
        return HttpResponse('''<h1 style="border-bottom: 1px solid #aaa; padding: 10px" > Not Found(  # 404)</h1>
        <div class="alert alert-danger" >
            Page not found. </div >
        <p>
            The above error occurred while the Web server was processing your request.
        </p>
        <p>
            Please contact us if you think this is a server error. Thank you.
        </p>''')
