import one

def main():
    name = "Alice"
    print(one.greet(name))

    result = one.add_numbers(10, 5)
    print(f"Sum: {result}")

    number = 8
    if one.is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

if __name__ == "__main__":
    main()
