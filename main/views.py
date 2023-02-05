from django.views.generic import TemplateView
from django.shortcuts import render 

class HomePageView(TemplateView):
    template_name = 'main/index.html'

def TomePageView(request):
    post=request.GET['fname']
    return render(request,'main/about.html',{'post':post})
