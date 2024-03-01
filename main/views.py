from math import ceil

from main.models import *
# Create your views here.
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render



def indexHandler(request):
    slide = Slider.objects.all()
    examples = Example.objects.all()
    # services = Service.objects.all()
    # tovars = Tovar.objects.all()
    # partners = Partner.objects.all()
    # otzivs = Otziv.objects.all()
    # feeds = Feedback.objects.all()
    # foto = ''
    # try:
    #     foto = Fon.objects.get(id=1)
    # except Fon.DoesNotExist:
    #     pass
    # contact = ''
    # try:
    #     contact = Contact.objects.get(id=1)
    # except Contact.DoesNotExist:
    #     pass
    #
    if request.POST:
        feed = Feedback()
        feed.name = request.POST.get('name', '')
        feed.phone = request.POST.get('phone', '')
        if request.POST.get('message'):
            feed.message = request.POST.get('message')
        feed.save()
        from django.shortcuts import redirect
        return redirect('/')





    return render(request, 'index.html', {
            'slide': slide,
            'examples': examples,
            # 'cats': cats,
            # 'tovars': tovars,
            # 'partners': partners,
            # 'services': services,
            # 'feeds': feeds,
            # 'otzivs': otzivs,
            # 'foto': foto,
    })


def aboutHandler(request):
    partners = Partner.objects.all()
    #

    if request.POST:
        feed = Feedback()
        feed.name = request.POST.get('name', '')
        feed.phone = request.POST.get('phone', '')
        if request.POST.get('message'):
            feed.message = request.POST.get('message')
        feed.save()
        from django.shortcuts import redirect
        return redirect('/')






    return render(request, 'about.html', {
            'partners': partners,
            # 'examples': examples,
    })



def contactHandler(request):

    if request.POST:
        feed = Feedback()
        feed.name = request.POST.get('name', '')
        feed.phone = request.POST.get('phone', '')
        if request.POST.get('message'):
            feed.message = request.POST.get('message')
        feed.save()
        from django.shortcuts import redirect
        return redirect('/')





    return render(request, 'contact.html', {

    })

def VhodnoyHandler(request):
    if request.POST:
        feed = Feedback()
        feed.name = request.POST.get('name', '')
        feed.phone = request.POST.get('phone', '')
        if request.POST.get('message'):
            feed.message = request.POST.get('message')
        feed.save()
        from django.shortcuts import redirect
        return redirect('/')

    cats = Category.objects.filter(status=1)
    products = Tovar.objects.filter(cat__status=1)
    st = 1

    active_cats = request.GET.getlist('active_cat', [])
    print('*****'*100)
    print(active_cats)
    active_cats = [int(i) for i in active_cats]
    if active_cats:
        new_goods = []
        for g in products:
            if g.cat.id in active_cats:
                new_goods.append(g)
        products = new_goods


    total = len(products)
    limit = 12
    current_page = int(request.GET.get('page', 1))
    pages_count = ceil(total / limit)
    pages = range(1, pages_count + 1)
    stop = current_page * limit
    start = stop - limit

    prev_page = current_page - 1
    next_page = None
    if current_page < pages_count:
        next_page = current_page + 1

    return render(request, 'shop-right-sidebar.html', {
        'cats': cats,
        'products': products[start:stop],
        'st': st,
        'pages': pages,
        'current_page': current_page,
        'stop': stop,
        'start': start,
        'total': total,
        'prev_page': prev_page,
        'next_page': next_page,
        'active_cats': active_cats,

    })

def KvartiraHandler(request):
    if request.POST:
        feed = Feedback()
        feed.name = request.POST.get('name', '')
        feed.phone = request.POST.get('phone', '')
        if request.POST.get('message'):
            feed.message = request.POST.get('message')
        feed.save()
        from django.shortcuts import redirect
        return redirect('/')


    cats = Category.objects.filter(status=2)
    products = Tovar.objects.filter(cat__status=2)
    st = 2

    active_cats = request.GET.getlist('active_cat', [])
    print('*****' * 100)
    print(active_cats)
    active_cats = [int(i) for i in active_cats]
    if active_cats:
        new_goods = []
        for g in products:
            if g.cat.id in active_cats:
                new_goods.append(g)
        products = new_goods

    total = len(products)
    limit = 12
    current_page = int(request.GET.get('page', 1))
    pages_count = ceil(total / limit)
    pages = range(1, pages_count + 1)
    stop = current_page * limit
    start = stop - limit

    prev_page = current_page - 1
    next_page = None
    if current_page < pages_count:
        next_page = current_page + 1

    return render(request, 'shop-right-sidebar.html', {
        'cats': cats,
        'products': products[start:stop],
        'st': st,
        'pages': pages,
        'current_page': current_page,
        'stop': stop,
        'start': start,
        'total': total,
        'prev_page': prev_page,
        'next_page': next_page,
        'active_cats': active_cats,


    })

def FurniturHandler(request):
    if request.POST:
        feed = Feedback()
        feed.name = request.POST.get('name', '')
        feed.phone = request.POST.get('phone', '')
        if request.POST.get('message'):
            feed.message = request.POST.get('message')
        feed.save()
        from django.shortcuts import redirect
        return redirect('/')


    cats = Category.objects.filter(status=3)
    products = Tovar.objects.filter(cat__status=3)
    st = 3

    active_cats = request.GET.getlist('active_cat', [])
    print('*****' * 100)
    print(active_cats)
    active_cats = [int(i) for i in active_cats]
    if active_cats:
        new_goods = []
        for g in products:
            if g.cat.id in active_cats:
                new_goods.append(g)
        products = new_goods

    total = len(products)
    limit = 12
    current_page = int(request.GET.get('page', 1))
    pages_count = ceil(total / limit)
    pages = range(1, pages_count + 1)
    stop = current_page * limit
    start = stop - limit

    prev_page = current_page - 1
    next_page = None
    if current_page < pages_count:
        next_page = current_page + 1

    return render(request, 'shop-right-sidebar.html', {
        'cats': cats,
        'products': products,
        'st': st,
        'pages': pages,
        'current_page': current_page,
        'stop': stop,
        'start': start,
        'total': total,
        'prev_page': prev_page,
        'next_page': next_page,
        'active_cats': active_cats,

    })


def ProductDetailHandler(request,pr_id):
    if request.POST:
        feed = Feedback()
        feed.name = request.POST.get('name', '')
        feed.phone = request.POST.get('phone', '')
        if request.POST.get('message'):
            feed.message = request.POST.get('message')
        feed.save()
        from django.shortcuts import redirect
        return redirect('/')


    product = Tovar.objects.get(id=pr_id)

    return render(request, 'product-details.html', {
        'product': product,

    })