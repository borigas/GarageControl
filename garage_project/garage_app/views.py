# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from garage_app.models.door import Door
from garage_app.models.status import Status

def index(request):
	door_list = Door.objects.all()
	for door in door_list:
		statuses = Status.objects.filter(door=door)
		if statuses.count() > 0:
			door.status = statuses.latest()
	context = {'door_list': door_list}
	return render(request, 'doors/index.html', context)

def update(request, door_id):
	print("Update")
	door = get_object_or_404(Door, pk=door_id)
	status = door.update_status()
	return redirect('index')

def open(request, door_id):
	print("Open")
	door = get_object_or_404(Door, pk=door_id)
	result = door.open()
	return HttpResponse(str(result))

def close(request, door_id):
	print("Close")
	door = get_object_or_404(Door, pk=door_id)
	result = door.close()
	return HttpResponse(str(result))
