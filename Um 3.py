from typing import Union, Any, List


def function_name(search: str, status: bool, *args: Any, **kwargs: Any) -> Union[List[int], str]:
    result = []
    result_2 = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f" {i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += (" Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")


# Примеры вызова функции
print(function_name("args", True, 1, 2, 3, 'a'))  # [1, 2, 3]
print(function_name("args", False, 1, 2, 3, 'a'))  # " 1 2 3 a"
print(function_name("kwargs", True, key1='value1',
                    key2='value2'))  # " Key: key1, Value: value1;  Key: key2, Value: value2; "
