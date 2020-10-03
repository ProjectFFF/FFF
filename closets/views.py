from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Newcloth
from .forms import NewclothPost

def new(request):
    return render(request, 'new.html')

def record(request):
    return render(request, 'record.html')

def mycloset(request):
    return render(request, 'mycloset.html')

def create(request): #입력 내용 데이터베이스에 넣어줌
    cloth= Newcloth()
    cloth.name= request.GET['cloth_name']
    cloth.shoulder= request.GET['shoulder']
    cloth.chest= request.GET['chest']
    cloth.arm= request.GET['arm']
    cloth.length= request.GET['total_length']
    cloth.image = request.GET['image']
    cloth.save() #데이터베이스에 저장해라
    return redirect('/cloth/'+str(cloth.id))

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