from django.shortcuts import render,redirect
from. models import Category, Photo,Video,Category_video
from django.core.paginator import Paginator
from PIL import Image
from PIL.ExifTags import TAGS
import datetime
def gallery(request):
    category=request.GET.get('category')
    if category==None:
        photos=Photo.objects.all()
    else:
        photos=Photo.objects.filter(category__name=category)
    # order = request.GET.get('order')
    default_order = '-created_at'
    # if order:
    #     # If 'order' parameter is provided in the query string, use it for ordering
    #     photos= photos.order_by(order)
    # else:
    #     # Use the default ordering if 'order' parameter is not provided
    photos= photos.order_by(default_order)
    
    paginator=Paginator(photos,12)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    categories=Category.objects.all()
    context={'categories':categories,'photos':photos,'page':page}
    return render(request,'photos/gallery.html',context)


def viewphoto(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photo':photo})
def deletephoto(request,pk):
    photo=Photo.objects.get(id=pk)
    photo.delete()
    return redirect('gallery')

def extract_creation_date(image):
    try:
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag)

                if tag_name in ('DateTimeOriginal', 'DateTimeDigitized', 'CreateDate',):
                    value = value.strip('“"” ')
                    print(value)
                    try:
                        creation_date = datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                        return creation_date
                    except ValueError:
                        pass
    except Exception as e:
        pass
    
    return None
def addPhoto(request):
    categories=Category.objects.all()
    if request.method=='POST':
        data=request.POST
        images=request.FILES.getlist('images')
        
        if data['category']!='none':
            category=Category.objects.get(id=data['category'])
        elif data['category_new']!='':
            category, created=Category.objects.get_or_create(name=data['category_new'])
        else: 
            category=None

        for image in images:
            img=Image.open(image)
   
            creation_date=extract_creation_date(img)
                    
                
            photo=Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
                created_at=creation_date,
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
    order = request.GET.get('order')
    if category==None:
        videos=Video.objects.all()
    else:
        videos=Video.objects.filter(category_video__name=category)

    default_order = '-created_at'
    if order:
        # If 'order' parameter is provided in the query string, use it for ordering
        videos = videos.order_by(order)
    else:
        # Use the default ordering if 'order' parameter is not provided
        videos = videos.order_by(default_order)
    paginator=Paginator(videos,12)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    categories=Category.objects.all()
    categories=Category_video.objects.all()
    context={'categories':categories,'videos':videos,'page':page}
    return render(request,'photos/gallery_video.html',context)

def deletevideo(request,pk):
    video=Video.objects.get(id=pk)
    video.delete()
    return redirect('video-gallery')
# Create your views here.
