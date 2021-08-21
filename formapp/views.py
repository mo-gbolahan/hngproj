from django.shortcuts import render
from .forms import InfoForm
# Create your views here.



def iForm(request):

    iform = InfoForm(request.POST or None)
    print(request.POST)
    if iform.is_valid():
        iform.save()
        iform = InfoForm()
        
    context = {
        'form':iform
    }
    
    return render(request,'form.html',context)