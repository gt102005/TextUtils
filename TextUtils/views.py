from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    uppercase=request.GET.get('Uppercase','off')
    lowercase=request.GET.get('Lowercase','off')
    
    if uppercase=='on':
        texts=request.GET.get('textarea','default')
        formatted_texts=texts.upper()
        output={'formatted_texts':formatted_texts}
        return render(request,'show.html',output)
    else:
        output={'formatted_texts':'Please select the operation and come again'}
        return render(request,'show.html',output)


