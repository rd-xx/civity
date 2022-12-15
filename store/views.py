from django.shortcuts import get_object_or_404, render

from store.models import Product

# Create your views here.
def index(request):
	products = Product.objects.all()
	return render(request, 'store/index.html', context={'products': products})

def product_details(request, slug):
	product = get_object_or_404(Product, slug=slug)
	return render(request, 'store/details.html', context={'product': product})