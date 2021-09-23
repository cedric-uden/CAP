from watchdog.queries.UpdateAccessToken import UpdateAccessToken
import watchdog.logs.Logging as log

log.setup(stream_level=log.INFO)


UpdateAccessToken().needs_to_be_updated()
