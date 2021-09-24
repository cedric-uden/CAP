import src.logs.Logging as log
from src.business.YouTubeInformation import YouTubeInformation
from src.mp3download.MP3Downloader import MP3Downloader

log.setup(stream_level=log.INFO)

# YouTubeInformation().update()
MP3Downloader()
