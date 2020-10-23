from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Newcloth, Newcloth_closet
from .forms import NewclothPost

def new(request):
    return render(request, 'new.html')

def record(request):
    records = Newcloth.objects
    return render(request, 'record.html', {'records':records})

def mycloset(request):
    records_c = Newcloth_closet.objects
    return render(request, 'mycloset.html', {'records':records_c})

def detail(request, pk):
    cloth = get_object_or_404(Newcloth, pk=pk)
    form = NewclothPost(instance=cloth)
    return render(request, 'detail.html', {'cloth':cloth})

def create(request): #입력 내용 데이터베이스에 넣어줌
    cloth = Newcloth()
    cloth.cloth_name= request.POST['cloth_name']
    cloth.shoulder= request.POST['shoulder']
    cloth.chest= request.POST['chest']
    cloth.arm= request.POST['arm']
    cloth.total_length= request.POST['total_length']
    cloth.image= request.FILES['image']
    cloth.pub_date = timezone.datetime.now()
    cloth.save()
    return render(request, 'record.html')

def create_c(request): #입력 내용 데이터베이스에 넣어줌
    cloth = Newcloth_closet()
    cloth.cloth_name_c= request.POST['cloth_name_c']
    cloth.shoulder_c= request.POST['shoulder_c']
    cloth.chest_c= request.POST['chest_c']
    cloth.arm_c= request.POST['arm_c']
    cloth.total_length_c= request.POST['total_length_c']
    cloth.image_c= request.FILES['image_c']
    cloth.pub_date = timezone.datetime.now()
    cloth.shopping_link= request.POST['shopping_link']
    cloth.tag= request.POST['tag']
    cloth.review= request.POST['review']
    cloth.save()
    return render(request, 'mycloset.html')

def update(request, pk):
    cloth = get_object_or_404(Newcloth, pk=pk)
    form = NewclothPost(instance=cloth)
    return render(request, 'update.html', {'form':form, 'cloth':cloth})
   
def edit(request, pk):
    cloth = get_object_or_404(Newcloth, pk=pk)   
    if request.method == "POST":
        cloth.cloth_name= request.POST['cloth_name']
        cloth.shoulder=  request.POST['shoulder']
        cloth.chest= request.POST['chest']
        cloth.arm= request.POST['arm']
        cloth.total_length= request.POST['total_length']
        cloth.image= request.POST['image']
        cloth.save()
        return render(request, 'record.html')   
    else:
         return render(request, 'home.html')
    return render(request, 'record.html', {'cloth':cloth})
         
    

def delete(request, pk):
    cloth = get_object_or_404(Newcloth, pk=pk)
    cloth.delete()
    return redirect('home')

def compare(request, pk):
    cloth_compare = get_object_or_404(Newcloth, pk=pk)
    form = NewclothPost(instance=cloth_compare)
    return render(request, 'compare.html', {'record':cloth_compare, 'form':form})

def newcloth(request):
    #입력된 내용을 처리 기능 -> POST
    if request.method =='POST':
        form = NewclothPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    #빈 페이지를 띄워주는 기능 -> GET
    else:
        form = NewclothPost()
        return render(request, 'new.html', {'form':form})


    
    