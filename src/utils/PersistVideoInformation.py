import pickle
from src.constants.ConstantsPaths import video_states_pickle_path
import src.logs.Logging as log


class PersistVideoInformation:

    _logger = log.get_logger(__name__)

    def __init__(self):
        pass

    def store_video_state(self, dictionary):
        file = open(video_states_pickle_path, 'wb')
        pickle.dump(dictionary, file)
        file.close()
        self._logger.debug("Wrote video information pickle file.")

    def get_video_state(self):
        file = open(video_states_pickle_path, 'rb')
        dictionary = {}
        try:
            dictionary = pickle.load(file)
        except EOFError:
            self._logger.warn("Pickle file has not been created.")

        file.close()
        self._logger.debug("Loaded the video information pickle file.")
        return dictionary

    def update_video_state(self, key, value):
        self._logger.debug(f"Updating key: '{key}' to value [{value}]")
        video_information = self.get_video_state()
        video_information[key] = value
        self.store_video_state(video_information)
