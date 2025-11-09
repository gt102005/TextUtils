from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def show(request):
    texts=request.POST.get('textarea')
    uppercase=request.POST.get('uppercase','off')
    lowercase=request.POST.get('lowercase','off')
    puncuations=request.POST.get('puncuations','off')
    newlines=request.POST.get('newlines','off')
    space_remove=request.POST.get('space_remove','off')
    
    # Checking Empty TextArea 
    if texts=='':
        dic={'output':'You Have Not Yet Entered Anything In The Box To Analyze '}
        return render(request,'show.html',dic)

    
    # Conversion in Uppercase
    if uppercase=='on':
        texts=texts.upper()
        # dic={'output':output}
        # return render(request,'show.html',dic)
    
    # Conversion in Lowercase
    if lowercase=='on':
        texts=texts.lower()
        # dic={'output':output}
        # return render(request,'show.html',dic)
    
    # Removing Punctuations form the Texts
    if puncuations=='on':
        output=''
        punc=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        for i in texts:
            if i not in punc:
                output+=i
        texts=output
        # dic={'output':output}
        # return render(request,'show.html',dic)
    
    # Removing Newlines for the Texts
    if newlines=='on':
        output=''
        for i in texts and texts!="/r":
            if i!="\n":
                output+=i
        texts=output
        # dic={'output':output}
        # return render(request,'show.html',dic)

    
    # removing Space from the Texts
    if space_remove=='on':
        output=''
        texts=texts.split(' ')
        for i in texts:
            output+=i+" "
        texts=output
        # dic={'output':output}
        # return render(request,'show.html',dic)
    if uppercase=='on'or lowercase=="on" or puncuations=="on" or newlines=="on" or space_remove=="on":
        dic={'output':texts}
        return render(request,'show.html',dic)
    else:
        dic={'output':'You Have Not Selected Anything To Analyze Please Select Something First ..',"error":True}
        return render(request,"show.html",dic)
    