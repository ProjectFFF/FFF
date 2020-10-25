from django.shortcuts import render, redirect, get_object_or_404
from closets.models import Newcloth, Newcloth_closet

def othersclosets(request):
    
    records_c = Newcloth_closet.objects.exclude(writer_c=request.user.username)
    return render(request, 'othersclosets.html', {'records':records_c})

def subchoice(request):
    qs = Newcloth_closet.objects.all()

    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs = qs.filter(subcategory_c=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        
    return render(request, 'othersclosets_t.html', {
        'records' : qs,
        'q' : q,
    })

def parchoice(request):
    qs = Newcloth_closet.objects.all()

    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs = qs.filter(parent_category_c=q) # 제목에 q가 포함되어 있는 레코드만 필터링
        
    return render(request, 'othersclosets_t.html', {
        'records' : qs,
        'q' : q,
    })