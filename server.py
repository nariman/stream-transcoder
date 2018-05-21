"""
I need any comment on the top
"""

import asyncio
import asyncio.subprocess
import os
import sys

import streamlink
from aiohttp import web


# Application instance

app = web.Application()


# Server options

host = os.environ.get("HOST", "localhost")
port = int(os.environ.get("PORT", "7777"))


# Index handler, for stream options

async def index(request):
    return web.Response(text="Hello, World!")


# Stream handler, for streaming data

async def stream(request):
    # Get the list of streams by given url
    streams = streamlink.streams(request.query["url"])

    # Get the chosen stream URL
    url = streams[request.query["stream"]].url

    # Prepare response streaming
    response = web.StreamResponse()
    await response.prepare(request)

    # Run the ffmpeg
    process = await asyncio.create_subprocess_shell(
        f"C:\\Users\\woofi\\Desktop\\ffmpeg-20180521-2c2d689-win64-static\\bin\\ffmpeg -i {url} -filter:v scale=480:-1 -f hls -",
        stdin=None,
        stdout=asyncio.subprocess.PIPE,
        stderr=None)

    # Get the transcoded output and push it to the response stream
    # Do it forever...
    while True:
        data = await process.stdout.read(1024)
        await response.write(data)

    # Close response streaming
    response.write_eof()

    return response


# Register handlers

app.add_routes([
    web.get("/", index),
    web.get("/stream", stream)
])


# Run the server, if called directly

if __name__ == "__main__":
    # Windows lifehacks
    if sys.platform == "win32":
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)

    web.run_app(app,
                host=host,
                port=port)
