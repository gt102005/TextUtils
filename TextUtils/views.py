from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def show(request):
    texts=request.GET.get('textarea')
    uppercase=request.GET.get('uppercase','off')
    lowercase=request.GET.get('lowercase','off')
    puncuations=request.GET.get('puncuations','off')
    newlines=request.GET.get('newlines','off')
    space_remove=request.GET.get('space_remove','off')
    
    # Checking Empty TextArea 
    if texts=='':
        dic={'output':'You Have Not Yet Entered Anything In The Box To Analyze '}
        return render(request,'show.html',dic)

    output=''
    # Conversion in Uppercase
    if uppercase=='on':
        output=texts.upper()
        dic={'output':output}
        return render(request,'show.html',dic)
    
    # Conversion in Lowercase
    elif lowercase=='on':
        output=texts.lower()
        dic={'output':output}
        return render(request,'show.html',dic)
    
    # Removing Punctuations form the Texts
    elif puncuations=='on':
        punc=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        for i in texts:
            if i not in punc:
                output+=i
        dic={'output':output}
        return render(request,'show.html',dic)
    
    # Removing Newlines for the Texts
    elif newlines=='on':
        for i in texts:
            if i!="\n":
                output+=i
        dic={'output':output}
        return render(request,'show.html',dic)

    
    # removing Space from the Texts
    elif space_remove=='on':
        texts=texts.split(' ')
        for i in texts:
            output+=i+" "
        dic={'output':output}
        return render(request,'show.html',dic)
    
    else:
        output={'output':'Error ! you did Something Wrong...'}
        return render(request,'show.html',)

    