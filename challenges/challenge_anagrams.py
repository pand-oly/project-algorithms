from typing import Tuple, List


def quick_sort(array_strings: List[str], start: int, end: int) -> None:
    if start < end:
        p = partition(array_strings, start, end)
        quick_sort(array_strings, start, p - 1)
        quick_sort(array_strings, p + 1, end)


def partition(array_strings: List[str], start: int, end: int) -> int:
    pivot = array_strings[end]
    delimiter = start - 1

    for i in range(start, end):
        if array_strings[i] <= pivot:
            delimiter = delimiter + 1
            array_strings[i], array_strings[delimiter] = (
                array_strings[delimiter],
                array_strings[i],
            )

    array_strings[delimiter + 1], array_strings[end] = (
        array_strings[end],
        array_strings[delimiter + 1],
    )

    return delimiter + 1


def is_anagram(first_string: str, second_string: str) -> Tuple[str, str, bool]:
    """Faça o código aqui."""
    list_string = list(first_string.lower())
    quick_sort(list_string, 0, len(list_string) - 1)
    order_first_string = "".join(list_string)

    list_string = list(second_string.lower())
    quick_sort(list_string, 0, len(list_string) - 1)
    order_second_string = "".join(list_string)

    if first_string == "" or second_string == "":
        return order_first_string, order_second_string, False

    return (
        order_first_string,
        order_second_string,
        (order_first_string == order_second_string),
    )
