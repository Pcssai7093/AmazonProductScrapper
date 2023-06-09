from random import randint
# ignore if there is any error in the below line 
from fake_useragent import UserAgent
ua=UserAgent()
referers = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.amazon.com",
    "https://www.netflix.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.linkedin.com",
    "https://www.reddit.com",
    "https://www.wikipedia.org",
    "https://www.yahoo.com",
    "https://www.twitch.tv",
    "https://www.microsoft.com",
    "https://www.apple.com",
    "https://www.spotify.com",
    "https://www.pinterest.com",
    "https://www.dropbox.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.medium.com",
    "https://www.quora.com",
    "https://www.tumblr.com",
    "https://www.netflix.com",
    "https://www.nytimes.com",
    "https://www.bbc.co.uk",
    "https://www.cnn.com",
    "https://www.nationalgeographic.com",
    "https://www.nasa.gov",
    "https://www.wikipedia.org",
    "https://www.imdb.com",
    "https://www.pexels.com",
    "https://www.unsplash.com",
    "https://www.dribbble.com",
    "https://www.behance.net",
    "https://www.etsy.com",
    "https://www.aliexpress.com",
    "https://www.walmart.com",
    "https://www.ebay.com",
    "https://www.target.com",
    "https://www.bestbuy.com",
    "https://www.homedepot.com",
    "https://www.lowes.com",
    "https://www.airbnb.com",
    "https://www.booking.com",
    "https://www.expedia.com",
    "https://www.tripadvisor.com",
    "https://www.kayak.com",
    "https://www.uber.com",
    "https://www.lyft.com",
    "https://www.doordash.com",
    "https://www.grubhub.com",
    "https://www.postmates.com",
    "https://www.netflix.com",
    "https://www.hulu.com",
    "https://www.disneyplus.com",
    "https://www.apple.com/music",
    "https://www.spotify.com",
    "https://www.soundcloud.com",
    "https://www.twitch.tv",
    "https://www.microsoft.com",
    "https://www.adobe.com",
    "https://www.ibm.com",
    "https://www.oracle.com",
    "https://www.salesforce.com",
    "https://www.intel.com",
    "https://www.amd.com",
    "https://www.nvidia.com",
    "https://www.android.com",
    "https://www.apple.com/iphone",
    "https://www.samsung.com",
    "https://www.huawei.com",
    "https://www.oneplus.com",
    "https://www.xiaomi.com",
    "https://www.vivo.com",
    "https://www.lg.com",
    "https://www.sony.com",
    "https://www.nintendo.com",
    "https://www.playstation.com",
    "https://www.xbox.com",
    "https://www.steampowered.com",
    "https://www.epicgames.com",
    "https://www.unity.com",
    "https://www.blender.org",
    "https://www.github.com",
    "https://www.gitlab.com",
    "https://www.bitbucket.org",
    "https://www.docker.com",
    "https://www.kubernetes.io",
    "https://www.stackoverflow.com",
    "https://www.medium.com",
    "https://www.dev.to",
    "https://www.freecodecamp.org",
    "https://www.codecademy.com",
    "https://www.w3schools.com",
    "https://www.udemy.com",
    "https://www.coursera.org",
    "https://www.edx.org",
    "https://www.khanacademy.org",
    "https://www.linkedin.com/learning",
    "https://www.alison.com",
    "https://www.instructables.com",
    "https://www.arduino.cc",
    "https://www.raspberrypi.org",
    "https://www.python.org",
    "https://www.java.com",
    "https://www.javascript.com",
    "https://www.php.net",
    "https://www.ruby-lang.org",
    "https://www.cplusplus.com",
    "https://www.go.dev",
    "https://www.kotlinlang.org",
    "https://www.scala-lang.org",
    "https://www.swiftdocs.org",
    "https://www.rust-lang.org",
    "https://www.typescriptlang.org",
    "https://www.angular.io",
    "https://www.reactjs.org",
    "https://www.vuejs.org",
    "https://www.django-rest-framework.org",
    "https://www.flask.pocoo.org",
    "https://www.nodejs.org",
    "https://www.expressjs.com",
    "https://www.databases.com",
    "https://www.mongodb.com",
    "https://www.postgresql.org",
    "https://www.mysql.com",
    "https://www.oracle.com/database",
    "https://www.redis.io",
    "https://www.elasticsearch.com"
]

def createHeader():
    return {'User-Agent':ua.random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
        "Referer":referers[randint(0,99)]}
