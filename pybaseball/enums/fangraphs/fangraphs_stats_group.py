from enum import unique, Enum


@unique
class FangraphsStatsGroup(Enum):
    PLAYER = 0
    TEAM = 1
    LEAGUE = 2

