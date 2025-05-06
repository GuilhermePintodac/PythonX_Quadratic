import math


def solve_quadratic(a, b, c):
    """Résout l'équation ax² + bx + c = 0 et retourne les racines."""
    if a == 0:
        raise ValueError(
            "Ce n'est pas une équation quadratique (a ne peut pas être 0)."
        )

    delta = b**2 - 4 * a * c

    if delta < 0:
        return "Pas de solution réelle"
    elif delta == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)
