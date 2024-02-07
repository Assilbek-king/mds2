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
    cats = Category.objects.filter(status=1)
    products = Tovar.objects.filter(cat__status=1)
    st = 1

    return render(request, 'shop-right-sidebar.html', {
        'cats': cats,
        'products': products,
        'st': st,

    })

def KvartiraHandler(request):
    cats = Category.objects.filter(status=2)
    products = Tovar.objects.filter(cat__status=2)
    st = 2

    return render(request, 'shop-right-sidebar.html', {
        'cats': cats,
        'products': products,
        'st': st,


    })

def FurniturHandler(request):
    cats = Category.objects.filter(status=3)
    products = Tovar.objects.filter(cat__status=3)
    st = 3

    return render(request, 'shop-right-sidebar.html', {
        'cats': cats,
        'products': products,
        'st': st,

    })


def ProductDetailHandler(request,pr_id):
    product = Tovar.objects.get(id=pr_id)

    return render(request, 'product-details.html', {
        'product': product,

    })