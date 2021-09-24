import src.logs.Logging as log
from src.business.YouTubeInformation import YouTubeInformation

log.setup(stream_level=log.INFO)

YouTubeInformation().update()
