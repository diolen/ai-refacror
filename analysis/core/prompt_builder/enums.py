from enum import Enum


class TaskType(Enum):
    DEBUG = "debug"
    REFACTOR = "refactor"
    FEATURE = "feature"