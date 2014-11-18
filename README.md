
## Scrapy Playground

I created this repository to quickly get started with scrapy and scrapyd. I've included a Dockerfile to build a container with everything required to run a scrapyd instance with Image pipeline capabilities.

I've also included a really simple tutorial spider that can be sent to the scrapyd instance to crawl stuff.


### Running `scrapyd` in Docker

If you want to build your own container,

    docker build -t scrapyd .
    docker run -it -p 6800:6800 scrapyd

Otherwise, I have an automated build on Docker Hub that you can use,

    docker run -it -p 6800:6800 a5huynh/scrapyd

