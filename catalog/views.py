from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    product_list = Product.objects.all()
    latest_five_products = product_list[len(product_list) - 5 :]
    context = {"object_list": latest_five_products}
    print(latest_five_products)
    return render(request, "catalog/home.html", context)


def contacts(request):
    contact_list = Contact.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        Contact.objects.create(name=name, phone=phone, message=message)

        print(f"\n\nИмя - {name}\n" f"Телефон - {phone}\n" f"Сообщение - {message}\n\n")

    context = {'object_list': contact_list[len(contact_list) - 3 :]}

    return render(request, "catalog/catalog.html", context)
