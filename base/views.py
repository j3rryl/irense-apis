from django.shortcuts import render
from django.http import HttpResponse
from .forms import RoomForm
from .models import Room


# Create your views here.

def home(request):
    return HttpResponse("Welcome to iRense APIs.")

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')
    #     request.POST.get('name)
    context = {'form': form}
    return render(request, 'base/form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'base/form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
    return render(request, 'base/delete.html', {'obj':room})