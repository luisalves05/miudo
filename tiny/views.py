from django.shortcuts import render

# Create your views here.

def init(request):
    return render(request, "tiny/index.html", {})
