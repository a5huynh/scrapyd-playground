
## Scrapy Playground

I created this repository to quickly get started with scrapy and scrapyd. I've
included a Dockerfile to build a container with everything required to run a
scrapyd instance with image pipeline capabilities.

I've also included a really simple tutorial spider that can be sent to the
scrapyd instance to crawl stuff.


### Quickstart with [Fig.sh](http://fig.sh/)

To get up and running with the scrapy playground using fig
    
    fig up

This will build the Docker container and spin up two containers. One is a
persistent data container where spiders/logs/etc. will be stored. The second is
the scrapyd server. Skip to the `Deploying the tutorial spider` section to
start scraping!


### Running `scrapyd` in Docker w/o Fig

If you want to build your own container,

    docker build -t scrapyd .
    docker run -it -p 6800:6800 scrapyd

Otherwise, I have an automated build on Docker Hub that you can use,

    docker run -it -p 6800:6800 a5huynh/scrapyd


### Deploying the tutorial project

First, make sure the IP address to the container is correct in the `scrapy.cfg`
file. Then you can deploy the spider to the scrapyd container using,

    scrapyd-deploy docker -p test

Make sure you're in the root directory of the tutorial project, where the
`scrapy.cfg` resides. You can call the project anything you want, just be sure
to correctly refer to the project name when scheduling things.

You can check the status of the project/spiders and logs on the scrapyd web GUI
located at http://[docker host]:6800

### Scheduling the tutorial spider

To schedule the basic tutorial spider, use the scrapyd API:

    curl http://[docker host]:6800/schedule.json -d project=test -d spider=tutorial


### Scheduling the coverart spider

To schedule the more complex coverart spider:

    curl http://[docker host]:6800/schedule.json -d project=test -d spider=coverart

Cover art images will be stored on the 
