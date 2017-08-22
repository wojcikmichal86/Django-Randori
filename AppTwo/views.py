from django.shortcuts import render
from AppTwo.models import User

def index(request):
    return render(request, 'AppTwo/index.html')

def help(request):
    my_dict= {'task':"Help Page"}
    return render(request, 'AppTwo/help.html', context=my_dict)

def users(request):
    users_list=User.objects.all()
    users_dict={'users': users_list}
    return render(request, 'AppTwo/users.html', context=users_dict)



# Create your views here.
