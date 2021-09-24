import watchdog.logs.Logging as log
from watchdog.queries.CheckYouTubeVideoInspector import CheckYouTubeVideoInspector
from watchdog.queries.MostRecentYouTubeVideos import MostRecentYouTubeVideos

log.setup(stream_level=log.INFO)

print(str(CheckYouTubeVideoInspector().get_json_from_youtube_id('o2AagtlRFoE')))
print(str(MostRecentYouTubeVideos().get_json()))
