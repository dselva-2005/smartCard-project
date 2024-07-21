from django.shortcuts import render,HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginRequiredMixin,View):
    def get(self,req):
        return HttpResponse('working')
    
