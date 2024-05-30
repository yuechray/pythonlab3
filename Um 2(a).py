from typing import List, Union

def multiply_list(elements: List[Union[int, float]], multiplier: Union[int, float] = 2) -> List[Union[int, float]]:
    return [element * multiplier for element in elements]

print(multiply_list([1, 2, 3])) # [2, 4, 6]
print(multiply_list([1, 2, 3], 3)) # [3, 6, 9]
