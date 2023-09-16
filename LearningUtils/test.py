import MathUtils
from MathUtils import MyCalCorr
import numpy as np

import tensorflow as tf

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    print("Testing correalation", MyCalCorr(x, y))
    print("np correlation", np.corrcoef(x, y))

    target1 = np.array([0.1, 0.2, 0.3, 0.4])
    target2 = np.array([0.2, 0.3, 0.4, 0.1])

    print("Testing cross entropy",
          MathUtils.MyCalCrossEntropyAfterSoftMax(target1, target2))
    # tens

    print("tf cross entropy",
          tf.keras.losses.categorical_crossentropy(target1, target2))

    # xor data
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
