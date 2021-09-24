from enum import Enum


class YouTubeVideoStates(Enum):
    # while processing
    NEW = "NEW"
    TO_BE_DOWNLOADED = "TO_BE_DOWNLOADED"
    DOWNLOADED_NOT_UPLOADED = "DOWNLOADED_NOT_UPLOADED"

    # final states
    UPLOADED = "UPLOADED"
    NOT_A_SERMON = "NOT A SERMON"
