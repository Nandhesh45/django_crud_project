from django.shortcuts import render, redirect

from new_app.forms import Furniture, FurnitureForm


def home(request):
    return render(request,'view.html')
def index(request):
    return render(request,'index.html')

def dash(request):
    return render(request,'dash.html')
def furniture(request):
    form =FurnitureForm()
    if request.method == 'POST':
        data = FurnitureForm(request.POST)
        if data.is_valid():
            data.save()
    # print(form)
    return render(request,'temp.html',{'form':form})

def furniture_view(request):
    data = Furniture.objects.all()
    return render(request,'view_data.html', {'data': data})

def furniture_delete(request,id):
    data = Furniture.objects.get(id=id)
    data.delete()
    return redirect("furniture_view")

def furniture_update(request,id):
    data = Furniture.objects.get(id=id)
    form = FurnitureForm(instance= data)
    if request.method == 'POST':
        data = FurnitureForm(request.POST,instance=data)
        if data.is_valid():
            data.save()
            return redirect("furniture_view")
    return render(request,'update.html',{'form':form})