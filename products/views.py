from django.shortcuts import render
from .models import product

# Create your views here.
def producT (request):
    return render(request,'products\product.html')

def products (request):
    pro = product.objects.all()
    # هنا فلتر با السعر اكبر من :
    x = {'pro':pro.filter(price__gt=500)}

    # هنا ترتيب با السعر :
    # x = {'pro':pro.order_by('-price')} 

    # استثناء بعض الاوبجيكت:
    # x = {'pro':pro.exclude(price__lt=750)} 

    # other ex:
    # x = {'pro':pro.exclude(Category='PC')} 


    return render(request,'products\products.html',x)

