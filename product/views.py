from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.http import JsonResponse
from django.db.models import Sum

# Create your views here.


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/product')
    else:
        return redirect('/sign-in')


def product(request):
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            products = Product.objects.all().values('code', 'kind', 'quantity')
            total = products.aggregate(Sum('quantity'))['quantity__sum'] or 0
            context = {"products": list(products), "total": total}
            return render(request, 'product/home.html', context)
        else:
            return redirect('/sign-in')



def add_product(request):
    if request.method == "POST":
        kind = request.POST.get("kind")
        if kind == "hoodie_s":
            code = "HDS"
        elif kind == "hoodie_m":
            code = "HDM"
        elif kind == "hoodie_l":
            code = "HDL"
        elif kind == "jeans_free":
            code = "JNF"
        elif kind =="socks_free":
            code == "SOK"
        elif kind =="hat_free":
            code = "HAT"
        else:
            message = "잘못된 상품 코드입니다. 다시 입력해주세요."
            context = {"message": message}
            return render(request, "product/home.html", context)

        quantity = request.POST.get("quantity")
        if not quantity:
            message = "수량을 입력해주세요."
            context = {"message": message}
            return render(request, "product/home.html", context)

        product = Product(code=code, kind=kind, quantity=quantity, author=request.user)
        product.save()
        message = f"{product} 상품이 등록되었습니다."
        context = {"message": message}
        return render(request, "product/home.html", context)
    else:
        return render(request, "product/home.html")





    
@csrf_exempt
def add_quantity(request):
    if request.method == "POST":
        kind = request.POST.get("kind")
        quantity = int(request.POST.get("quantity"))
        if kind == "hoodie_s":
            code = "HDS"
        elif kind == "hoodie_m":
            code = "HDM"
        elif kind == "hoodie_l":
            code = "HDL"
        elif kind == "jeans_free":
            code = "JNF"
        elif kind =="socks_free":
            code == "SOK"
        elif kind =="hat_free":
            code = "HAT"
        else:
            message = "잘못된 상품 코드입니다. 다시 입력해주세요."
            context = {"message": message}
            print(kind)
            return render(request, "product/home.html", context)

        product, created = Product.objects.get_or_create(code=code, defaults={"kind": kind, "author": request.user})
        product.quantity += quantity
        product.save()
        message = f"{product} 상품에 {quantity}개가 입고되었습니다."
        context = {"message": message}
        return render(request, "product/home.html", context)
    else:
        return render(request, "product/home.html")




def remove_quantity(request):
    if request.method == "POST":
        kind = request.POST.get("kind")
        quantity = int(request.POST.get("quantity"))

        if kind == "hoodie_s":
            code = "HDS"
        elif kind == "hoodie_m":
            code = "HDM"
        elif kind == "hoodie_l":
            code = "HDL"
        elif kind == "jeans_free":
            code = "JNF"
        elif kind =="socks_free":
            code == "SOK"
        elif kind =="hat_free":
            code = "HAT"
        else:
            message = "잘못된 상품 코드입니다. 다시 입력해주세요."
            context = {"message": message}
            return render(request, "product/home.html", context)

        product = Product.objects.get(code=code)
        if product.quantity >= quantity:
            product.quantity -= quantity
            product.save()
            message = f"{product} 상품에 {quantity}개가 출고되었습니다."
        else:
            message = f"{product} 상품의 재고가 부족합니다."
        context = {"message": message}
        return render(request, "product/home.html", context)
    else:
        return render(request, "product/home.html")



def total_quantity(request):
    total = Product.objects.aggregate(Sum("quantity"))["quantity__sum"]
    if total is None:
        total = 0
    return JsonResponse({"total": total})




def product_list(request):
    products = Product.objects.all().values('code', 'kind', 'quantity')
    total = products.aggregate(Sum('quantity'))['quantity__sum'] or 0
    context = {"products": list(products), "total": total}
    return render(request, "product/home.html", context)



