# Stream Transcoder

???

It's a simple server, that allows me to transcode Twitch streams into low quality, if streamer is not a Twitch Partner. It should be started on the remote server (obviously).  
Requires Python (asyncio), `aiohttp` and `streamlink` python packages, and ffmpeg for transcoding on the fly.  
This code is a one big bug, but it's ok, b/c when I want to watch a stream, I want to watch a stream, not to code smth. Mb I'll rewrite it later.

```
GET http://localhost:7777/stream?url=twitch.com%2Fninja&stream=480p
```
