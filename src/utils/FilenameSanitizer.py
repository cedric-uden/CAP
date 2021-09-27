import src.logs.Logging as log
import os


class FilenameSanitizer:
    _logger = log.get_logger(__name__)

    def clean_filename(self, name):
        new_name = self.replace_whitespace(name)
        new_name = self.replace_pipe(new_name)
        new_name = self.replace_forwardslash(new_name)
        new_name = self.replace_backslash(new_name)
        new_name = self.replace_lt(new_name)
        new_name = self.replace_gt(new_name)
        new_name = self.replace_hashtag(new_name)
        if name != new_name:
            self._logger.debug(f"Suggesting {new_name} instead of {name}")
            return new_name

    def replace_forwardslash(self, filepath):
        while "/" in filepath:
            filepath = filepath.replace("/", "-")
        return filepath

    def replace_backslash(self, filepath):
        while "\\" in filepath:
            filepath = filepath.replace("\\", "-")
        return filepath

    def replace_lt(self, filepath):
        while "<" in filepath:
            filepath = filepath.replace("<", "-")
        return filepath

    def replace_gt(self, filepath):
        while ">" in filepath:
            filepath = filepath.replace(">", "-")
        return filepath

    def replace_hashtag(self, filepath):
        while "#" in filepath:
            filepath = filepath.replace("#", "_")
        return filepath

    def replace_pipe(self, filepath):
        while "|" in filepath:
            filepath = filepath.replace("|", "-")
        return filepath

    def replace_whitespace(self, filepath):
        while " " in filepath:
            filepath = filepath.replace(" ", "_")
        return filepath
