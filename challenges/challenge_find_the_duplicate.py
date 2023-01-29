from typing import List, Union


def find_duplicate(nums: List[int]) -> Union[int, bool]:
    """Faça o código aqui."""
    if nums is None or len(nums) < 2:
        return False

    nums.sort()
    for i in range(len(nums) - 1):
        if type(nums[i]) is not int or nums[i] <= 0:
            return False

        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
