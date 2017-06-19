from channels.routing import route
from .consumers import online_connect, online_disconnect, online_receive


channel_routing = [
    route("websocket.connect", online_connect,
          path=r'^/online/$'),
    route("websocket.receive", online_receive,
          path=r'^/online/$'),
    route("websocket.disconnect", online_disconnect,
          path=r'^/online/$'),
]
