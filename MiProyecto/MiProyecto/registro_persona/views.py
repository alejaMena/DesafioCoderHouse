from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import reg_familia_form

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registro(request):
    if request.method =='GET':
        return render(request, 'registro.html', {
            'form':UserCreationForm
        })
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('familia')
                #return HttpResponse('Usuario registrado con éxito')  
            except:
                return render(request, 'registro.html', {
                    'form':UserCreationForm,
                    'error':'El usuario ya existe'
                    })
        return render(request, 'registro.html', {
            'form':UserCreationForm,
            'error':'los datos ingresados son errados'
        })

def familia(request):
    return render(request, 'familia.html')

def salir(request):
    logout(request)
    return redirect('home')

def reg_familia(request):
    if request.method== 'GET':
        return render(request, 'reg_familia.html', {
        'form':reg_familia_form
        })
    else:
        form=reg_familia_form(request.POST)
        new_reg=form.save(commit=False)
        new_reg.user=request.user
        new_reg.save()
        return redirect ('familia')

def ingresar(request):
    if request.method== 'GET':
        return render(request, 'ingresar.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'ingresar.html', {
            'form': AuthenticationForm,
            'error': 'Datos ingresados incorrectos'
             })
        else:
            login(request, user)
            return redirect('familia')