import numpy as np
import pandas as pd
import os
import random
import tensorflow as tf

from typing import NoReturn

def setRandomSeed(seed: int) -> NoReturn:
    np.random.seed(seed)
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    tf.random.set_seed(seed)
    print("finish seeding")