def test_error_types(op_num: int) -> None:
    if op_num == 0:
        int("abc")
    elif op_num == 1:
        1/0
    elif op_num == 2:
        open("/non/existent/file")
    elif op_num == 3:
        "a" + 1
    elif op_num == 4:
        1 + 3


def error_messages() -> None:
    for ops in range(0, 5):
        print(f"Testing operation {ops}...")
        try:
            test_error_types(ops)
            print("Operation completed successfully")
        except ValueError as v_e:
            print(f"Caught ValueError: {v_e}")
        except ZeroDivisionError as z_d_e:
            print(f"Caught ZeroDivisionError: {z_d_e}")
        except FileNotFoundError as f_n_f:
            print(f"Caught FileNotFoundError: {f_n_f}")
        except TypeError as t_e:
            print(f"Caught TypeError: {t_e}")
    print("\nAll error types tested successfully!")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    error_messages()


if __name__ == "__main__":
    main()
