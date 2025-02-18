from django.shortcuts import render
from intasend import APIService
import os
from decouple import config

token=config('token')
publishable_key=config('publishable_key')
service= APIService(token=token,publishable_key=publishable_key,test=True)

payload = {
    'amount':'',
    'currency':'',
    'email':'',
    'phone_number':'',
    'first_name':'',
    'last_name':'',
    'api_ref':'',
    'redirect_url':''
}

checkout = service.checkout.create(data=payload)

if checkout['status'] == 'success':
    checkout_url = checkout['data']['url']
    print(checkout_url)

else:
    print(checkout)

def index(request):
    return render(request, 'index.html')