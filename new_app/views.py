from django.shortcuts import render

from new_app.forms import Furniture


def home(request):
    return render(request,'view.html')
def index(request):
    return render(request,'index.html')

def dash(request):
    return render(request,'dash.html')
def furniture(request):
    form =Furniture()
    # print(form)
    return render(request,'temp.html',{'form':form})