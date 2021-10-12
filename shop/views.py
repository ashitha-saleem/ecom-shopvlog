from django.shortcuts import render,get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=products.objects.filter(category=c_page,available=True)
    else:
        prodt=products.objects.all()
    cat=categ.objects.all()
    paginator=Paginator(prodt,4)
    pageno=int(request.GET.get('page','1'))
    try:
        pageobj=paginator.page(pageno)
    except:
        pageobj=paginator.page(paginator.num_pages)

    return render(request,'index.html',{'pr':pageobj.object_list,'paginator':paginator,'pno':pageobj.number,'ct':cat})
def prd_detail(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'details.html',{'pro':prod})
def searching(request,c_slug=None):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'pr': prod})

def categories(request):
    return {'catg':categ.objects.all()}




