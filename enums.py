from enum import Enum

class CarBrand(Enum):
    TOYOTA = "Toyota"
    HONDA = "Honda"
    MITSUBISHI = "Mitsubishi"
    NISSAN = "Nissan"
    FORD = "Ford"
    HYUNDAI = "Hyundai"
    SUZUKI = "Suzuki"
    KIA = "Kia"
    ISUZU = "Isuzu"
    MG = "MG"

class CarModel(Enum):
    # Toyota
    VIOS = "Vios"
    WIGO = "Wigo"
    INNOVA = "Innova"
    FORTUNER = "Fortuner"
    HILUX = "Hilux"
    AVANZA = "Avanza"

    # Honda
    CIVIC = "Civic"
    CITY = "City"
    BRIO = "Brio"
    BRV = "BR-V"
    CRV = "CR-V"

    # Mitsubishi
    MIRAGE = "Mirage"
    XPANDER = "Xpander"
    MONTERO_SPORT = "Montero Sport"
    L300 = "L300"

    # Nissan
    ALMERA = "Almera"
    TERRA = "Terra"
    NAVARA = "Navara"
    URVAN = "Urvan"

    # Ford
    RANGER = "Ranger"
    EVEREST = "Everest"
    ECOSPORT = "EcoSport"
    MUSTANG = "Mustang"

    # Hyundai
    ACCENT = "Accent"
    REINA = "Reina"
    TUCSON = "Tucson"
    STARGAZER = "Stargazer"

    # Suzuki
    SWIFT = "Swift"
    ERTIGA = "Ertiga"
    DZIRE = "Dzire"
    JIMNY = "Jimny"

    # Kia
    SOLUTO = "Soluto"
    SPORTAGE = "Sportage"
    PICANTO = "Picanto"

    # Isuzu
    DMAX = "D-Max"
    MU_X = "mu-X"
    TRAVIZ = "Traviz"

    # MG
    MG5 = "MG 5"
    ZS = "ZS"