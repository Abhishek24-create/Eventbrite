from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
# from Webapp.models import Student_Data
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session

# Create your views here.
def Event_Page(request):
    return render(request,"MyApp/event.html")