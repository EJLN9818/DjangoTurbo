from .models import Message, Room

from turbo import decorators
from turbo import classes

@decorators.register(Message)
class MessageBroadcast(classes.ModelBroadcast): 

    def on_save(self, message, created, *args, **kwargs):
        if created:
            message.room.turbo.render(
                'chat/components/message.html',
                {'message': message}
            ).append(id='messages')
            
    def on_delete(self, message, *args, **kwargs):
        message.room.turbo.remove(id=f"message-{message.id}")