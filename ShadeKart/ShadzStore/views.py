from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Complaint, OrderDetail, OrderUpdate, UserAccount
import json

paramsOrderID = {}
# Create your views here.


def index(request):
    """returns the ShadzStore's homepage"""
    allProds = []
    # Fetching products according to category with ids
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}  # set comprehension

    #  ===== arranging products category-wise =====
    for cat in cats:
        prods = Product.objects.filter(category=cat)
        # calculating no. of slides for each category of products
        n = len(prods)
        nSlides = ceil(n / 4)
        allProds.append([prods, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'ShadzStore/siteIndex.html', params)


def searchMatch(query, item: Product) -> bool:
    """returns True the match of products if found else False"""
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.category.lower():
        return True
    return False


def search(request):
    """fetches the product according to the query given by user on the search bar"""
    query = request.GET.get('search')
    allProds = []
    # Fetching products according to category with ids
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}  # dict comprehension

    #  ===== arranging products category-wise =====
    for cat in cats:
        prodsResults = Product.objects.filter(category=cat)
        prods = [item for item in prodsResults if searchMatch(query, item)]
        n = len(prods)
        nSlides = ceil(n / 4)
        if n != 0:
            allProds.append([prods, range(1, nSlides), nSlides])

    params = {'allProds': allProds, 'msg': "Search results - not found!"}
    return render(request, 'ShadzStore/search.html', params)


def signUp(request):
    """user sign up page"""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        password = request.POST.get('passwd')

        account = UserAccount(name=username, email=email, phone=phone, password=password)
        account.save()

    return render(request, 'ShadzStore/signup.html')


def login(request):
    """Login page"""
    response = dict()
    if request.method == 'POST':
        email = request.POST.get('inputEmail', '')
        password = request.POST.get('inputPassword', '')

        # Checking for user from the database
        userAccountMatch = UserAccount.objects.filter(email=email, password=password)
        return render(request, 'ShadzStore/userHomepage.html', {'username': userAccountMatch[0]})

    return render(request, 'ShadzStore/login.html')


def about(request):
    """Information about the company"""
    return render(request, 'ShadzStore/about.html')


def contact(request):
    """Help and Support page"""
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone_num = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')

        if name != '' and email != '' and phone_num != '' and desc != '':
            contactInfo = Complaint(name=name, email=email, phone=phone_num, desc=desc)
            contactInfo.save()

    return render(request, 'ShadzStore/contact.html')


def productView(request, my_id):
    """View products page"""
    # Using product id to fetch product
    product = Product.objects.filter(id=my_id)
    return render(request, 'ShadzStore/productView.html', {'product': product})


def tracker(request):
    """Page for tracking user's orders"""
    if request.method == 'POST':
        orderID = request.POST.get('orderID', False)
        email = request.POST.get('email', False)
        try:
            order = OrderDetail.objects.filter(order_id=int(orderID), email_address=email)

            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderID)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})

                response = json.dumps(updates, default=str)
                return HttpResponse(response)

            else:
                return HttpResponse(json.dumps([]))

        except Exception as e:
            return HttpResponse(f'Exception: {e}')

    return render(request, 'ShadzStore/track.html')


def checkout(request):
    """Page where user can check out the cart items"""
    global paramsOrderID
    paramsOrderID.clear()

    if request.method == 'POST':
        amount = request.POST.get('amount', 0)
        fullName = request.POST.get('name', 'NA')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        address3 = request.POST.get('address3', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        zipcode = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')

        if fullName != '' and address1 != '' and state != '' and city != '' and zipcode != '' and phone != '' and email != '':
            order = OrderDetail(amount=float(amount), full_name=fullName, address1=address1, address2=address2,
                                address3=address3,
                                state=state, city=city, zipcode=zipcode, contact_number=phone, email_address=email)
            order.save()

            # make an order update when checkout is done
            update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
            update.save()

            paramsOrderID = {'orderIDNumber': order.order_id}

    return render(request, 'ShadzStore/checkout.html', paramsOrderID)


def orderConfirmation(request, orders: dict):
    """order confirmation page"""
    return render(request, 'ShadzStore/orderConfirm.html', orders)
