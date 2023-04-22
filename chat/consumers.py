from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json


class ChatRoomConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # creates consumer group ?
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name 
        )

        # needs to have something to accept connection. Accept before sending messages.
        await self.accept()

        # sends message to group name, with JSON
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type' : 'tester_message',
                'tester' : 'ciao',
            }
        )

    async def tester_message(self, event):
        tester = event['tester']
        await self.send(text_data=json.dumps({
            'tester' : tester,
        }))


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
            
    pass
