import watchdog.logs.Logging as log
from watchdog.business.YouTubeInformation import YouTubeInformation

log.setup(stream_level=log.INFO)

YouTubeInformation().update()
