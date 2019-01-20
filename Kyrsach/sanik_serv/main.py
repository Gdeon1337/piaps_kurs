import asyncio
from sanik_serv.app import create_app
from sanik_serv.app import register_extension


app = create_app()


if __name__ == "__main__":
    server = app.create_server(host="0.0.0.0", port=8000)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(server)
    asyncio.get_event_loop().run_until_complete(register_extension())
    loop.run_forever()
