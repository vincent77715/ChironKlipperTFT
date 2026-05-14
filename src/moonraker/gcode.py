async def run_gcode(client, script):
    await client.send(
        "printer.gcode.script",
        {
            "script": script
        }
    )
