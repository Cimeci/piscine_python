def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """give_bmi(height: list[int | float], weight: list[int | float])
    -> list[int | float]

The function returns a list of BMIs calculated using the
formula Weight ÷ Height²."""

    if len(height) != len(weight):
        print("Error: Values aren't the same size")
        return []

    result = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            print("Error: Values aren't int or float")
            return []
        result.append(w / (h * h))
    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit(bmi: list[int | float], limit: int) -> list[bool]

The function returns a list of results indicating whether the IBM is above or
below the limit"""

    result = []
    for el in bmi:
        if not isinstance(el, (int, float)):
            print("Error: Values aren't int or float")
            return []
        result.append(el > limit)
    return result
