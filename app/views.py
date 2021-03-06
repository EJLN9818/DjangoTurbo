from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView

from app.models import Room, Message
from turbo.classes import Turbo


class RoomList(ListView):
    model = Room
    context_object_name = 'rooms'


class RoomDetail(DetailView):
    model = Room
    context_object_name = 'room'


class MessageCreate(CreateView):
    model = Message
    fields = ['text']
    template_name = 'app/room_form.html'

    def get_success_url(self):
        # Redirect to the empty form
        return reverse('room_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        room = get_object_or_404(Room, pk=self.kwargs['pk'])
        form.instance.room = room
        return super().form_valid(form)


def message_delete(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    message.delete()
    return HttpResponse()

def send_broadcast(request):

    Turbo('broadcast_name').render_from_string(
        f'{datetime.now()}: This is a broadcast.'
    ).update(id='broadcast_box')

    return HttpResponse('Sent a Broadcast')