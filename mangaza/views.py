from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse("Hello There")

#homePage
def test(request):
    return render(request,"test.html")

# page0
def home(request):
    return render(request,"index.html")

# page1
def about(request):
    return render(request,"vacation.html")

# page2
def blog(request):
    return render(request,"blog.html")

# page3
def booking(request):
    return render(request,"booking.html")

# page4
def contact(request):
    return render(request,"contact.html")

# page5
def feature(request):
    return render(request,"feature.html")

# page6
def menu(request):
    return render(request,"menu.html")

# page7
def single(request):
    return render(request,"single.html")

# page8
def team(request):
    return render(request,"team.html")

# page9
def team0(request):
    return render(request,"team0.html")

# Page 10
def kings(request):
    return render(request,"stay.html")