from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from blog import forms, models


@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        photo = form.save(commit=False)
        photo.uploader = request.user
        # now we can save
        photo.save()
        return redirect('home')
    return render(request, 'blog/photo_upload.html', context={'form': form})


@login_required
def home(request):
    # return render(request, 'blog/home.html')
    photos = models.Photo.objects.all()
    return render(request, 'blog/home.html', context={'photos': photos})
