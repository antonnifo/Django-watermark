from django.shortcuts import render, redirect
from .forms import WatermarkForm

def add_watermark(request):

    if request.method == 'POST':
        form = WatermarkForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            watermarkz = form.save(commit=False)
            watermarkz.added_by = request.user
            watermarkz.save()
            return redirect('dashboard')
    else:
        form = WatermarkForm() 

    return render (request, 'images/add_watermark.html' ,{'form':form,})

