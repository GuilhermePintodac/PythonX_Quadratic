import argparse
from quadratic.solver import solve_quadratic


def main():
    parser = argparse.ArgumentParser(description="Résoudre une équation quadratique.")
    parser.add_argument("a", type=float, help="coefficient a")
    parser.add_argument("b", type=float, help="coefficient b")
    parser.add_argument("c", type=float, help="coefficient c")
    args = parser.parse_args()

    result = solve_quadratic(args.a, args.b, args.c)
    print("Résultat:", result)


if __name__ == "__main__":
    main()
