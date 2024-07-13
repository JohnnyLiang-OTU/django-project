from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
import os, json
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.cache import cache_control

# Pagination Stuff
from django.core.paginator import Paginator

# Create your views here.

def delete_product(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        try:
            os.remove('base'+product.image.url)
        except OSError:
            print(OSError)
            pass
        product.delete()
        return redirect('catalogo')
    else:
        return redirect('catalogo')

def home(request):
    return render(request, 'base/home.html')

def home_front(request):
    return render(request, 'index.html')

def catalog(request):
    # product_set = Product.objects.all()

    paginator = Paginator(Product.objects.all().order_by('id'), 15)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    # context = {'product_set' : product_set,}
    
    context = {'products' : products}
    return render(request, 'base/catalogo.html', context)

def recommend(request):
    return render(request, 'base/recommend.html')

def success(request):
    return render(request, 'base/success.html')

def handle_404(request, exception):
    return render(request, '404.html', {})

import logging
logger = logging.getLogger('django')

def handle_500(request):
    logger.error("A server error occurred", exc_info=True)
    return render(request, '500.html', status=500)

def test_error_email(request):
    try:
        raise Exception("Test error email")
    except Exception as e:
        logger.error("Test error occurred", exc_info=True)
        raise

# <------- Admin Views (Delete, Edit, ...) ------>

@staff_member_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def administrador(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request, 'admin/admin_list.html', context)

@staff_member_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def product_form(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if 'submit_add_another' in request.POST:
                return redirect('add_product')
            else:
                return redirect('catalogo')
    else:
        form = ProductForm()
    
    context = {"product_form": form}
    return render(request, 'base/productform.html', context)

@staff_member_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit_form(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("administrador")
    else:
        form = ProductForm(instance=product)
    context = {'product_form':form}
    return render(request, 'base/editform.html', context)

@require_POST
@staff_member_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_models(request):
    try:
        data = json.loads(request.body)
        ids = data.get('ids', [])
        if ids:
            for e in ids:
                Product.objects.get(pk=e).delete()
            return JsonResponse({'status':'success'}, status=200)
        else:
            return JsonResponse({'status':'error',
                                 'message':'No IDs provided'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error',
                             'message': str(e)}, status=500)
                             