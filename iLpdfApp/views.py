from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Home/home.html')

def mergepdf(request):
    return render(request,'PdfConvert/merge_pdf.html')

def devices(request):
    return render(request,'Devices/desktop.html')
