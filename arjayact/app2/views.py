from django.shortcuts import render

def home(request):
    return render(request, 'app2/home.html')

def services(request):
    return render(request, 'app2/services.html')

def portfolio(request):
    return render(request, 'app2/portfolio.html')
