from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,"generator/home.html")

def praveen(request):
    return HttpResponse("<h1>Vanakam Bro!!!</h1>")

def password(request):
    thepassword=""
    characters=list("abcdefghijklmnopqrstuvwxyz")
    length=int(request.GET.get('Length',12))

    if request.GET.get("Uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("Numbers"):
        characters.extend(list("0123456789"))

    if request.GET.get("Special Characters"):
        characters.extend(list("!@#$%&"))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request,"generator/password.html",{"password":thepassword})

def about(request):
    return render(request,"generator/about.html")
