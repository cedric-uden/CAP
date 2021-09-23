from watchdog.queries.AccessTokenUpdater import AccessTokenUpdater
import watchdog.logs.Logging as log

log.setup(stream_level=log.INFO)


AccessTokenUpdater().needs_to_be_updated()
