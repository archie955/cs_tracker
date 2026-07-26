from enum import StrEnum


class Maps(StrEnum):
    AGENCY = "cs_agency"
    ITALY = "cs_italy"
    OFFICE = "cs_office"
    ANCIENT = "de_ancient"
    ANUBIS = "de_anubis"
    CACHE = "de_cache"
    DUST2 = "de_dust2"
    GOLDEN = "de_golden"
    INFERNO = "de_inferno"
    MIRAGE = "de_mirage"
    NUKE = "de_nuke"
    OVERPASS = "de_overpass"
    PALACIO = "de_palacio"
    TRAIN = "de_train"
    VERTIGO = "de_vertigo"
    ROOFTOP = "de_rooftop"


class MatchTypes(StrEnum):
    PREMIER = "Premier"
    FACEIT = "FACEIT"
    COMP = "Competitive"
    WINGMAN = "Wingman"


class Weapon(StrEnum):  # fill out all weapons
    KNIFE = "Knife"
