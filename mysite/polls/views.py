#from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def index(request):
    print("Received: ", request, " request")
    # Print contents of request body
    print(request.body)
    r =  JsonResponse({'message': 'Received POST request'})
    r.status_code = 200
    print(r.content)
    return r

