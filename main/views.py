from django.shortcuts import render

def mainPage(request):
    return render(request, 'main/wrapper.html')
