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

BRAND_MODELS = {
    CarBrand.TOYOTA: [
        "Vios", "Wigo", "Innova", "Fortuner", "Hilux", "Avanza"
    ],

    CarBrand.HONDA: [
        "Civic", "City", "Brio", "BR-V", "CR-V"
    ],

    CarBrand.MITSUBISHI: [
        "Mirage", "Xpander", "Montero Sport", "L300"
    ],

    CarBrand.NISSAN: [
        "Almera", "Terra", "Navara", "Urvan"
    ],

    CarBrand.FORD: [
        "Ranger", "Everest", "EcoSport", "Mustang"
    ],

    CarBrand.HYUNDAI: [
        "Accent", "Reina", "Tucson", "Stargazer"
    ],

    CarBrand.SUZUKI: [
        "Swift", "Ertiga", "Dzire", "Jimny"
    ],

    CarBrand.KIA: [
        "Soluto", "Sportage", "Picanto"
    ],

    CarBrand.ISUZU: [
        "D-Max", "mu-X", "Traviz"
    ],

    CarBrand.MG: [
        "MG 5", "ZS"
    ]
}
