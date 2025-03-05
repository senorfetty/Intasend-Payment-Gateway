from django.shortcuts import render


# from intasend import APIService
# import json
# from django.http import Jsonresponse
from decouple import config


# token=config('token')
# publishable_key=config('publishable_key')
# service= APIService(token=token,publishable_key=publishable_key,test=True)

def index(request):
    publicAPIKey = config('publishable_key')
    return render(request, 'index.html', {'publicAPIKey': publicAPIKey})
