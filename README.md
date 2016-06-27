# Masters Dissertation Early Deliverable

This repository contains submission material for the CO880 Early Deliverable.

&copy; Matt Weeks 2016 (matt@weeks.codes)

## Directory Structure
```
/
|-- docs
|   |-- risks.md
|   |-- specification.md
|-- old-src
|-- |-- mjw77-early
|-- |-- |-- css
|-- |-- |-- libs
|-- src
|-- |-- vagrant
|-- |-- |-- dEarly
|-- |-- |-- |-- templates
|-- .gitignore
|-- README.md
```

docs - contains all the documentation beyond this README.

old-src - contains the original version of the project, designed to work on Google App Engine, due to their setup the application cannot be run using only GAE, but some of the files could still be useful whilst developing the project.

src - contains all of the source code for the application in its current state.

## App URL

This application is currently not available to view publically currently, a video is running at the following URL:

https://youtu.be/xFTwe-9_g_Y

The video shows the number of tweets created in the last 60 seconds that contain the phrase "GameofThrones". This video was recorded the morning that the final episode of season 6 of Game of Thrones was originally aired, roughly 2 hours after it finished.

## Libraries Currently Being Used

* Twitter API ([GET statuses/sample] (https://dev.twitter.com/streaming/reference/get/statuses/sample))
* Tweepy - twitter python library
* Chartjs - javascript graphing library
* JQuery
