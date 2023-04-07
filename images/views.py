from django.shortcuts import render, redirect
from .forms import WatermarkForm, ImageAddForm
from django.contrib.auth.decorators import login_required
from .models import Image


@login_required
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

@login_required
def watermark_images(request):
    if request.method == 'POST':
        form = ImageAddForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.added_by = request.user
            image.save()
            return redirect('dashboard')
    else:
        images = Image.objects.all()
        form = ImageAddForm()

    return render(request, 'images/watermark_image.html', {'form': form,
                                                            'images':images, })
