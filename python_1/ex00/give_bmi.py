import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """give_bmi(height: list[int | float], weight: list[int | float])
    -> list[int | float]

The function returns a list of BMIs calculated using the
formula Weight ÷ Height²."""

    if len(height) != len(weight):
        print("Error: Values aren't the same size")
        return []

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            print("Error: Values aren't int or float")
            return []
    #     result.append(w / (h * h))

    heights = np.array(height)
    weights = np.array(weight)
    bmi = weights / (heights ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit(bmi: list[int | float], limit: int) -> list[bool]

The function returns a list of results indicating whether the IBM is above or
below the limit"""

    for el in bmi:
        if not isinstance(el, (int, float)):
            print("Error: Values aren't int or float")
            return []
        # result.append(el > limit)
    bmis = np.array(bmi)
    result = bmis > limit
    return result.tolist()
