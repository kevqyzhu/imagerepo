from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import ImageRepository, Image
from .forms import uploadImage

# Create your views here.

def index(response, id):
    imRepo = ImageRepository.objects.get(id=id)
    return render(response, "main/images.html", {"imRepo":imRepo})


@login_required(login_url='/login/')
def home(response):
    imRepo = ImageRepository.objects.filter(user=response.user)
    if not imRepo:
        ir = ImageRepository(name=response.user.username)
        ir.save()
        response.user.imagerepository.add(ir)
    imRepo = ImageRepository.objects.get(user=response.user)
    
    return render(response, "main/home.html", {"imRepo":imRepo})

def delete_image(request, id, loc):
    image = Image.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse(loc))

@login_required(login_url='/login/')
def search(request):
    imRepo = ImageRepository.objects.filter(user=request.user)
    if not imRepo:
        ir = ImageRepository(name=request.user.username)
        ir.save()
        response.user.imagerepository.add(ir)
    imRepo = ImageRepository.objects.get(user=request.user)
    
    query = request.GET.get('q','')
    if query:
            queryset = (Q(description__icontains=query))
            results = imRepo.image_set.all().filter(queryset).distinct()
    else:
       results = []
    return render(request, 'main/search.html', {'results':results, 'query':query})

@login_required(login_url='/login/')
def upload(response):
    imRepo = ImageRepository.objects.filter(user=response.user)
    if not imRepo:
        ir = ImageRepository(name=response.user.username)
        ir.save()
        response.user.imagerepository.add(ir)
    imRepo = ImageRepository.objects.get(user=response.user)

    if response.method == "POST":
        form = uploadImage(response.POST, response.FILES)
        if form.is_valid():
            d=form.cleaned_data.get("description")
            i=form.cleaned_data.get("image")
            imRepo.image_set.create(description=d, image=i)

        return HttpResponseRedirect("/")


    else:
        form = uploadImage()
    return render(response, "main/upload.html", {"form":form})