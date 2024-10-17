# This file is craete fir the views
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','OFF')
    uppercaps = request.POST.get('uppercaps' , 'OFF')
    newlineremover = request.POST.get('newlineremover' , 'OFF')
    extraspaceremover = request.POST.get('extraspaceremover' , 'OFF')
    
    if removepunc == "on":
         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_+-*'''
         analyzed_text = ""
         for char in djtext:
           if char not in punctuations:
              analyzed_text = analyzed_text + char
         params = {'purpose':'Remove Punctuations','analyze_text':analyzed_text}
         return render(request,'analyze.html',params) 
    elif(uppercaps == 'on'):
        analyzed_text=''
        for char in djtext:
            analyzed_text = analyzed_text + char .upper()
        params = {'purpose':'CAPITALISED TEXT','analyze_text':analyzed_text}
        return render(request,'analyze.html',params) 
    
    elif(newlineremover == "on"):
        analyzed_text = ""
        for char in djtext:
            if char != '/n':
                analyzed_text = analyzed_text + char
        params = {'purpose':'Nw line remover','analyze_text':analyzed_text}
        return render(request,'analyze.html',params)
    
    elif(extraspaceremover == "on"):
        analyzed_text = ""
        for index,char in enumerate(djtext):
            if not djtext[index]==" " and djtext[index+1] == " ":
                analyzed_text = analyzed_text + char
        params = {'purpose':'Extra line Remover','analyze_text':analyzed_text}
        return render(request,'analyze.html',params)
    

    else:
        return HttpResponse("Erro")


   
   
