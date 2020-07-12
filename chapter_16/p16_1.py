def swap_in_place(a, b):
    b = a ^ b  # After this "b" = a^b  "a" = a
    a = b ^ a  # After this "b" = a^b  "a" = a^b^a = b
    b = b ^ a  # After this "b" = a^b^b=a "a" =b
    # Or just do a,b = b,a
    return a, b


if __name__ == "__main__":
    a, b = -2, 3
    print(f"Swapping {a} and {b} is {swap_in_place(a,b)}")
