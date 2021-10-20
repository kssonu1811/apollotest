from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def dashboard(request):
    return render(request,'account/dashboard.html')
def empdashboard(request):
    return render(request,'account/empdashboard.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            return(user_form.errors)
    else:
        user_form = UserForm()
    data = {
        'user_form': user_form,
        'registered': registered,
    }

    return render(request,'account/register.html', data,)

def login(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('empdashboard')
    else:
        form =AuthenticationForm()
    return render(request, 'account/login.html',{'form':form})

@login_required(login_url = 'account:login')
def empdashboard(request):
    return render(request,'account/empdashboard.html')