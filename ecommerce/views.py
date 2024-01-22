from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from decouple import config


def index(request):
    return render(request, 'index.html')


def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''
    return HttpResponse('Welcome to 6410742198 Peerapat Supasri views!')


def ecommerce_product_view(request):
    '''This function render product page of ecommerce views'''
    return HttpResponse('This is product page of ecommerce views!')


def display_product_by_id(request, product_id):
    '''This function render product page of ecommerce views'''
    return HttpResponse('This is product page of ecommerce views! </br></br>' + str(product_id))
    # return with HTML


def item_view(request, item_id):
    my_value = ""
    try:
        my_value = config('MY_ENV_VARIABLE', default='Some Default Value')
        print(my_value)
    except:
        my_value = 'Some Default Value'
        print('Error')

    context_data = {
        "item_id": item_id,
        "SECRET_KEY": my_value,
    }

    return render(request, 'index.html', context=context_data)
