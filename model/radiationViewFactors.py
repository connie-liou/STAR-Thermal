import math


class RadiationViewFactors:
    @staticmethod
    def parallelSquarePlates(sideLength: float, separation: float) -> float:
        L = sideLength
        H = separation
        w = L / H
        x = math.sqrt(1 + pow(w, 2))
        y = x * math.atan(w / x) - math.atan(w)
        return (math.log(pow(x, 4) / (1 + 2 * pow(w, 2))) + 4 * w * y) / (
                math.pi * pow(w, 2)
        )

    @staticmethod
    def squarePlatesAtRightAngle():
        h1 = math.sqrt(2)
        h2 = pow(h1, 4) / 3
        return 1 / 4 + (math.atan(1) - h1 * math.atan(1 / h1) - 1 / 4 * math.log(h2)) / math.pi
