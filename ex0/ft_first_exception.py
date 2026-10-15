def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    return (temp_int)


def test_temperature(temp_str: str) -> None:
    try:
        input_temperature(temp_str)
        print(f"Temperature is now {input_temperature(temp_str)}°C")
    except ValueError as v_e:
        print(f"Caught input_temperature error: {v_e}")
    return


def main() -> None:
    test_a: str = "25"
    test_b: str = "abc"
    print("=== Garden Temperature ===\n")
    print(f"Input data is '{test_a}'")
    test_temperature(test_a)
    print()
    print(f"Input data is '{test_b}")
    test_temperature(test_b)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
