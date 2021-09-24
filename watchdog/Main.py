import watchdog.logs.Logging as log
from watchdog.queries.MostRecentYouTubeVideos import MostRecentYouTubeVideos

log.setup(stream_level=log.INFO)

print(MostRecentYouTubeVideos().get_json())
