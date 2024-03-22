from django.shortcuts import render,  get_object_or_404, redirect
from . models import Products, ItemsDelivery
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Sum
from . forms import ItemsDeliveryForm

# def add_to_cart(request,product_id):
#     total = 0
#     nothing = Products.objects.filter(id=product_id)
#     for i in nothing:
#         item_category = i.category
#         quantity = i.quantity
#         price = i.price
    
#     quantity = quantity+1
#     total = quantity*price
#     nothing.update(cart=True, quantity=quantity, total=total)
#     return redirect("pastry_store:home", category=item_category)


def update_cart(request,myid,operator):
    product = Products.objects.filter(id=myid)

    for i in product:
        category = i.category
        quantity = i.quantity
        total = i.total
        price = i.price


        if operator == "minus":
            quantity = quantity-1
            if quantity == 0:
                product.update(quantity=0, total=0, cart=False)
            total = quantity * price 
            product.update(quantity=quantity, total=total)
        else:
            quantity = quantity+1
            total = quantity * price
            product.update(quantity=quantity, total=total)

        return redirect("pastry_store:item_detail", category=category)



def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    category = product.category
    
    product.cart = True
    product.quantity += 1
    product.total = product.quantity * product.price
    product.save()

    return redirect(reverse("pastry_store:item_detail", kwargs={'category': category}))



    

# Create your views here.
def home(request):
    return render(request, "pastry_store/home.html")


# def item_detail(request,category):
#     # products = Products.objects.get(category=category)
#     product = get_object_or_404(Products, category=category)
#     # product = {'products': products}
#     # print(products)
#     return render(request, "pastry_store/item_detail.html", {'product':product})


def item_detail(request, category):
    products = Products.objects.filter(category=category)
    return render(request, "pastry_store/item_detail.html", {'products': products, 'category': category})

# def my_cart(request):
#     quant = 0
#     total = 0
#     items = ""
#     boom = ""
#     query = Products.objects.filter(quantity__gt=0)
#     for i in query:
#         quant = i.quantity
#         items = i.product_name
#         boom = boom + items + str(quant) + ""
#     for i in query:
#         total = i + total
#     return render(request, "pastry_store/my_cart.html", {'query':query,'total':total})




def my_cart(request):
    if request.method == "POST":
        form = ItemsDeliveryForm(request.POST)
        if form.is_valid():
            print("form is valid")

            items_delivery = form.save()

            return redirect('pastry_store:payment')
        else:
            print("its not valid")
    else:
        form = ItemsDeliveryForm()
        cart_items = Products.objects.filter(cart=True)
        total = sum(item.total for item in cart_items)


        total_price = cart_items.aggregate(total_price=Sum('total'))['total_price']

        if total_price is None:
            total_price = 0

        context = {
            'cart_items': cart_items,
            'total': total,
            'total_price': total_price,
            "comment": form,
        }
        # print(ItemsDeliveryForm())
        return render(request, "pastry_store/my_cart.html", context)

def payment(request):
    cart_items = Products.objects.filter(cart=True)
    total = sum(item.total for item in cart_items)
    total_price = cart_items.aggregate(total_price=Sum('total'))['total_price']
    return render(request,"pastry_store/payment.html",{'totalprice':total_price})



def thankyou(request):
    return render(request,"pastry_store/thankyou.html")