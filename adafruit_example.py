from Adafruit_IO import Client

aio = Client("ADAFRUIT_AIO_USERNAME", "ADAFRUIT_AIO_KEY ")
feed = aio.feeds("FEED_KEY")

aio.send_data(feed.key, "DATA")
