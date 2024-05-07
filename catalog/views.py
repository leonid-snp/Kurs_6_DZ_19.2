from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Contact, Category


def home(request):
    context = {
        "title": 'Главная страница'
    }
    return render(request, "catalog/home.html", context)


def contacts(request):
    contact_list = Contact.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        Contact.objects.create(name=name, phone=phone, message=message)

        print(f"\n\nИмя - {name}\n" f"Телефон - {phone}\n" f"Сообщение - {message}\n\n")

    context = {
        'object_list': contact_list[len(contact_list) - 3 :],
        "title": 'Контакты'
    }

    return render(request, "catalog/catalog.html", context)


def detail_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product,
        'title': product.name
    }
    return render(request, "catalog/detail_product.html", context)


def add_product(request):
    category_list = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        photo = request.POST.get("photo")
        category = request.POST.get("category")
        price = request.POST.get("price")
        created_at = request.POST.get("created_at")
        updated_at = request.POST.get("updated_at")

        # Product.objects.create(
        #     name=name,
        #     description=description,
        #     photo=photo,
        #     category=category,
        #     price=price,
        #     created_at=created_at,
        #     updated_at=updated_at
        # )
        print(request.POST)
        print(name, description, photo, category, price, created_at, updated_at)
        print(category_list[0])
    context = {
        'object_list': category_list,
        'title': 'Добавить продукт'
    }
    return render(request, 'catalog/add_product.html', context)


def home_1(request):
    product_list = Product.objects.all()
    latest_five_products = product_list[:4]
    context = {
        "object_list": latest_five_products,
        "title": 'Вторая страница'
    }
    print(latest_five_products)
    return render(request, "catalog/home_2.html", context)


def home_2(request):
    product_list = Product.objects.all()
    latest_five_products = product_list[4:]
    context = {
        "object_list": latest_five_products,
        "title": 'Вторая страница'
    }
    print(latest_five_products)
    return render(request, "catalog/home_2.html", context)
