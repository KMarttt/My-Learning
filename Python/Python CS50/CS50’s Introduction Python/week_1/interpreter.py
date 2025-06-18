def main():
    x, y, z = input("Expression: ").split(" ")
    print(f"{computation(x, y, z):.1f}")


def computation(x, y, z):
    x = float(x)
    z = float(z)
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z



main()
