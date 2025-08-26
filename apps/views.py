from django.shortcuts import render

def index(request):
    return render(request, "components/index.html")


def navigation(request):
    return render(request, "layouts/navigation.html")


# Create your views here.
