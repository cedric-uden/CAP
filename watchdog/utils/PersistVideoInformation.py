import pickle
from watchdog.constants.ConstantsPaths import video_information_pickle_path
import watchdog.logs.Logging as log


class PersistVideoInformation:

    _logger = log.get_logger(__name__)

    def __init__(self):
        pass

    def store_video_information(self, dictionary):
        file = open(video_information_pickle_path, 'wb')
        pickle.dump(dictionary, file)
        file.close()
        self._logger.debug("Wrote video information pickle file.")

    def get_video_information(self):
        file = open(video_information_pickle_path, 'rb')
        dictionary = {}
        try:
            dictionary = pickle.load(file)
        except EOFError:
            self._logger.warn("Pickle file has not been created.")

        file.close()
        self._logger.debug("Loaded the video information pickle file.")
        return dictionary
