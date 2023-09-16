import numpy as np
import pandas as pd


def mySigmod(x: np.ndarray) -> np.ndarray:
    """
    Calculate the sigmod of x

    :param x: np.ndarray
    :return: np.ndarray

    """

    return 1 / (1 + np.exp(-x))


def MyCalCorr(x: np.ndarray, y: np.ndarray, rd=5) -> float:
    """
    Calculate the correlation coefficient between x and y

    r = n * Σ(xy) - Σx * Σy / sqrt(n * Σx^2 - (Σx)^2) * sqrt(n * Σy^2 - (Σy)^2)

    :param x: np.ndarray
    :param y: np.ndarray
    :return: float

    """

    assert len(x) == len(y)
    n = len(x)

    # numerator: float =
    sum_xy: list = [x_i * y_i for x_i, y_i in zip(x, y)]
    numerator: float = n * sum(sum_xy) - sum(x) * sum(y)
    denominator: float = np.sqrt(n * sum([x_i ** 2 for x_i in x]) - sum(x) ** 2) \
        * np.sqrt(n * sum([y_i ** 2 for y_i in y]) - sum(y) ** 2)

    return round(numerator / denominator, rd)


def MyCalCrossEntropyAfterSoftMax(x: np.array, y: np.array) -> float:
    """
    Calculate the cross entropy between x and y

    H(x, y) = - Σx * log(y)

    :param x: np.array, probability of each class
    :param y: np.array, probability of each class
    :return: float

    """

    assert len(x) == len(y)

    return - sum([x_i * np.log(y_i) for x_i, y_i in zip(x, y)])
