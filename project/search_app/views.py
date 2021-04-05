from django.shortcuts import render
from projectapp.models import product
from django.db.models import Q

def searchResult(request):
    query=request.GET.get('q')
    if query is not None:
        products=product.objects.filter(Q(name__contains=query))
        return render(request,"search.html",{'query':query, 'products':products})