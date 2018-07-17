# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import user.routing

# Định tuyến hướng websocket tới các app trong project
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            user.routing.websocket_urlpatterns,
        )
    ),
})
