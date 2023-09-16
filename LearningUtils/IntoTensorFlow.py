import tensorflow as tf
import numpy as np


# load dataset
# construct model
# run model
# eval model

def normalize_dataset(dataset: np.ndarray):
        dataset /= 255.0

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)


if __name__ == "__main__":
    mnist = tf.keras.datasets.mnist
    # load dataset
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    print(type(x_train))
    # print(tf.config.list_physical_devices('GPU'))
    # normalize_dataset(x_train), normalize_dataset(x_test)
    x_train = x_train / 255.0
    x_test = x_test / 255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])


    model.compile(optimizer="adam",
                  loss=loss_fn,
                  metrics=["accuracy"])

    model.fit(x_train, y_train, epochs=5)

    model.evaluate(x_test, y_test, verbose=2)