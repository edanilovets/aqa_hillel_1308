from dataclasses import dataclass

@dataclass
class Car:
    """Car object for garage page"""
    brand: str = "Audi"
    model: str = "TT"
    mileage: int = 1000
