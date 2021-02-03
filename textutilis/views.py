from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,"index.html")

def ex(request):
    return render(request,"navigator.html")



def analyze(request):
    djtext=request.POST.get("text","default")
    removepunc=request.POST.get("removepunc","off")
    capfirst = request.POST.get("capfirst", "off")
    newlineremover=request.POST.get("newlineremover", "off")
    extraspaceremover=request.POST.get("extraspaceremover", "off")

    print(djtext)
    print(removepunc)
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    punctext=""
    params = {}
    if removepunc=="on":
         for char in djtext:
              if char not in punctuations:
                 punctext=punctext+char

         remove_punc={"purpose":"removed punctuations","analyzed_text":punctext}
         params.update({"removepunctuations":remove_punc})
         djtext=punctext
        # return render(request,"analyze.html",params)
    if capfirst == "on":
        captext=""
        for char in djtext:
            captext = captext + char.capitalize()
        uppercase={"purpose": "changed to uppercase", "analyzed_text": captext}
        params.update( {"uppercase":uppercase})
        djtext=captext
        #return render(request, "analyze.html", params)
    if newlineremover == "on":
        newlinetext=""
        for char in djtext:
              if char!="\n" and char!="\r":
                  newlinetext = newlinetext + char.capitalize()
        newline_remover={"purpose": "newlineremover", "analyzed_text": newlinetext}
        params.update({"newlineremover":newline_remover})
        djtext=newlinetext
        #return render(request, "analyze.html", params)
    if extraspaceremover == "on":
        extraspacetext=""
        for  index,char in enumerate(djtext):
              if not(index==len(djtext)-1):
                  if not(djtext[index] ==" " and djtext[index+1] == " "):
                      extraspacetext = extraspacetext + char
              else:
                  extraspacetext = extraspacetext + char
        space_remover={"purpose":"spaceremover","analyzed_text":extraspacetext}
        params.update({"extraspaceremover":space_remover})
        djtext=extraspacetext
        #return render(request, "analyze.html", params)
    return render(request,"analyze.html",params)












"""def capfirst(request):
    djtext=request.GET.get("text","default")
    capfirst=request.GET.get("capfirst","off")
    print(djtext)
    caps=""
    if capfirst == "on" :
        for char in djtext :
            caps=caps+char.capitalize()
            


    return HttpResponse(caps)
    """
"""def newlineremove(request):
    return HttpResponse("newlineremover <a href='/removepunc/'> back </a>")
def spaceremove(request):
    return HttpResponse("spaceremover")
def charcount(request):
    return HttpResponse("charcount")

"""