from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from .models import Product


def homepage(request):
  context = {
    "product_list": Product.objects.all(),
  }
  return render(request, 'pmi/homepage.html', context=context)



def about(request):
  return render(request, 'pmi/about.html')



def product_detail(request,id):
  context={
    "id": id,
    "product": get_object_or_404(Product, pk=id),
  }
  return render(request, 'pmi/product_detail.html', context=context)

