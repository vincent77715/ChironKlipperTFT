import websockets
import orjson


class MoonrakerClient:
    def __init__(self, url):
        self.url = url
        self.ws = None
        self.msg_id = 0

    async def connect(self):
        self.ws = await websockets.connect(self.url)

    async def send(self, method, params=None):
        self.msg_id += 1

        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "id": self.msg_id,
        }

        if params:
            payload["params"] = params

        await self.ws.send(orjson.dumps(payload))
