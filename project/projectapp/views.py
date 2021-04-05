from django.shortcuts import render, get_object_or_404

from projectapp.models import category, product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def allProdcat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(category, slug=c_slug)
        products_list = product.objects.filter(Category=c_page)
    else:
        products_list = product.objects.all()
        paginator = Paginator(products_list, 3)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        try:
            products_list = paginator.page(page)
        except (EmptyPage, InvalidPage):
            products_list = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'category': c_page, 'products': products_list})


def catdetail(request, c_slug, product_slug):
    try:
        pro = product.objects.get(Category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'pro': pro})






