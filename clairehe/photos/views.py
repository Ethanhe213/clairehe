from django.shortcuts import render,redirect
from. models import Category, Photo,Video,Category_video
from django.core.paginator import Paginator

def gallery(request):
    category=request.GET.get('category')
    items_per_page=9
  
    if category==None:
        photos=Photo.objects.all()
    else:
        photos=Photo.objects.filter(category__name=category)
    categories=Category.objects.all()
    context={'categories':categories,'photos':photos}
    return render(request,'photos/gallery.html',context)


def viewphoto(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photo':photo})
def deletephoto(request,pk):
    photo=Photo.objects.get(id=pk)
    photo.delete()
    return redirect('gallery')


def addPhoto(request):
    categories=Category.objects.all()
    if request.method=='POST':
        data=request.POST
        image=request.FILES.get('image')

        if data['category']!='none':
            category=Category.objects.get(id=data['category'])
        elif data['category_new']!='':
            category, created=Category.objects.get_or_create(name=data['category_new'])
        else: 
            category=None
        photo=Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,

        )
        return redirect('gallery')
    context={'categories':categories}
    return render(request,'photos/add.html',context)

def addVideo(request):
    categories=Category_video.objects.all()
    if request.method=='POST':
        data=request.POST
        video=request.FILES.get('video')

        if data['category']!='none':
            category=Category_video.objects.get(id=data['category'])
        elif data['category_new']!='':
            category, created=Category_video.objects.get_or_create(name=data['category_new'])
        else: 
            category=None
        video=Video.objects.create(
            category=category,
            description=data['description'],
            video=video,

        )
        return redirect('video-gallery')
    context={'categories':categories}
    return render(request,'photos/add_video.html',context)
def viewvideo(request,pk):
    video=Video.objects.get(id=pk)
    return render(request,'photos/video.html',{'video':video})
def gallery_video(request):
    category=request.GET.get('category')
    items_per_page=9
  
    if category==None:
        videos=Video.objects.all()
    else:
        videos=Video.objects.filter(category_video__name=category)
    categories=Category_video.objects.all()
    context={'categories':categories,'videos':videos}
    return render(request,'photos/gallery_video.html',context)

def deletevideo(request,pk):
    video=Video.objects.get(id=pk)
    video.delete()
    return redirect('video-gallery')
# Create your views here.
