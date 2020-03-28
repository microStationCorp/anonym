from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    if request.method == "POST" and request.is_ajax():
        usr = request.POST['usr']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']

        if User.objects.filter(username=usr).exists():
            msg = 'username already exists'
        else:
            User.objects.create_user(
                username=usr, password=pass1, first_name=fname, last_name=lname)
            msg = 'All done, please remember your username and password'
        context = {
            'msg': msg
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
