class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def water_plant_error(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def watering_system(plants: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant_error(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def main() -> None:
    valid_plants: list[str] = ["Tomato", "Lettuce", "Carrots"]
    invalid_plants: list[str] = ["Tomato", "lettuce"]
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    watering_system(valid_plants)
    print()
    print("Testing invalid plants...")
    watering_system(invalid_plants)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
