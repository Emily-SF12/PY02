class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def try_errors() -> None:
    print("Testing PlantError...")
    try:
        raise_plant_error()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print("\nTesting WaterError...")
    try:
        raise_water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print("\nTesting catching all garden errors...")
    try:
        raise_plant_error()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        raise_water_error()
    except GardenError as error:
        print(f"Caught GardenError: {error}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    try_errors()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
