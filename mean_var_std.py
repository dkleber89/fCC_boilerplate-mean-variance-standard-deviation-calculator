"""Module to calculate some statistics"""
import numpy as np

def calculate(input_list: list[int]):
    """Calculate statistics

    Args:
        input_list (list[int]):
            Need to be a list of 9 Elements to calculate statistics in an a 3x3 Matrix

    Raises:
        ValueError: Raise when the length of the Value list is not exactly 9

    Returns:
        _type_: Dict of Statistics
    """
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    np_array = np.reshape(input_list,(3,3))

    calculations = {
        "mean": [np_array.mean(axis=0).tolist(), np_array.mean(axis=1).tolist(), np_array.mean()],
        "variance": [np_array.var(axis=0).tolist(), np_array.var(axis=1).tolist(), np_array.var()],
        "standard deviation": [
            np_array.std(axis=0).tolist(),
            np_array.std(axis=1).tolist(),
            np_array.std()
            ],
        "max": [np_array.max(axis=0).tolist(), np_array.max(axis=1).tolist(), np_array.max()],
        "min": [np_array.min(axis=0).tolist(), np_array.min(axis=1).tolist(), np_array.min()],
        "sum": [np_array.sum(axis=0).tolist(), np_array.sum(axis=1).tolist(), np_array.sum()]
    }

    print(calculations)

    return calculations
