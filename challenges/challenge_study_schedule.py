from typing import List, Tuple, Union


def study_schedule(permanence_period: List[Tuple], target_time: int) -> Union[int, None]:
    """Faça o código aqui."""
    if target_time is None:
        return None

    count = 0
    for n1, n2 in permanence_period:
        if (type(n1) is not int) or (type(n2) is not int):
            return None
        elif n1 <= target_time <= n2:
            count += 1

    return count
