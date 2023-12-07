import asyncio
import json
from include import data
from aiohttp import web

class Api:
    async def getConventionInfo(self, request):
        encrypted = data.EncryptInformation()
        return web.json_response(json.loads(encrypted.Decrypt()))

async def main():
    app = web.Application()

    app.router.add_get("/convention_info", Api().getConventionInfo)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "127.0.0.1", "1234")
    await site.start()

if __name__ ==  "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.create_task(main())
    loop.run_forever()