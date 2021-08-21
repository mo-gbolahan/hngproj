from django.shortcuts import render
from .forms import InfoForm
from django.contrib import messages


def iForm(request):
    if request.method == 'POST':
        iform = InfoForm(request.POST or None)
        if iform.is_valid():
            messages.success(request, 'Contact info saved successfully')
            iform.save()
        else:
            messages.error(request, 'All fields on contact form are required')
    return render(request, 'form.html', {'form': InfoForm()})
