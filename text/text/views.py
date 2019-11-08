# I HAVE CRETED THIS PAGE
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse('''<h1>Django</h1> <a href="https://www.linkedin.com/in/md-dilshad-54b926171/">Linkedin_profile</a>''')
def analyze(request):
    #GET The Text
    djtext=request.GET.get('text','default')
    remove_punc = request.GET.get('removepunc', 'off')
    print(remove_punc)
    print(djtext)
    if remove_punc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Your Desire Text','Analyzed':analyzed}
        return render(request,'analyze.html', params)
    else:
        return HttpResponse("Please click on the remove punc")






