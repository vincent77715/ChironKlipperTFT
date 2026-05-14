class VirtualSD:
    def __init__(self):
        self.files = []

    async def refresh(self, moonraker):
        await moonraker.send(
            "server.files.list",
            {
                "root": "gcodes"
            }
        )
