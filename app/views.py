from django.shortcuts import render

# Create your views here.
def hai(request):
    return render(request,'hai.html')
def bootstrap(request):
    return render(request,'bootstrap.html')
def bootstrap2(request):
    return render(request,'bootstrap2.html')