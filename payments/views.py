from django.shortcuts import render
from intasend import APIService
import json
from django.http import Jsonresponse
from decouple import config


token=config('token')
publishable_key=config('publishable_key')
service= APIService(token=token,publishable_key=publishable_key,test=True)


def generate_checkout(request):
    if request.method == 'POST':
        try :
            data= json.loads(request.body)

            payload = {
                'amount': data.get('amount'),
                'currency': data.get('currency'),
                'email': data.get('email'),
                'phone_number': data.get('phone_number'),
                'first_name': data.get('first_name'),
                'last_name': data.get('last_name'),
                'api_ref': data.get('api_ref'),
                'redirect_url': data.get('redirect_url')
            }
            checkout = service.checkout.create(data=payload)

            if checkout['status'] == 'success':
                return Jsonresponse({'checkout_url' : checkout['data']['url']})
            
            else:
                return Jsonresponse({'error' : checkout.get('message', 'Failed')})
        except Exception as e:
            return Jsonresponse({'error': str(e)},status =400)
    return Jsonresponse({'error': 'Invalid'}, status=405)
