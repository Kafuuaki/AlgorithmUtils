import numpy as np
import tensorflow as tf

import MathUtils


x: np.array= np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([0, 1, 1, 0], dtype=float)

# input 4 * 2
# output 4 * 1


# input layer width 2 neurons
# + activation function sigmoid

# alternative imple https://towardsdatascience.com/how-neural-networks-solve-the-xor-problem-59763136bdd7

# class XORNet(tf.keras.Model):
#     def __init__(self, input_dim, output_dim):
#         super(XORNet, self).__init__()
#         self.w = tf.Variable(tf.random.uniform([input_dim, output_dim]))
#         self.b = tf.Variable(tf.random.uniform([output_dim]))
#         self.out = tf.nn.sigmoid(tf.matmual())

#     def call(self, inputs):
#         out_layer1 = tf.matmul(inputs, self.w) + self.b
#         output_layer = tf.nn.sigmoid(out_layer1)

#         return output_layer

    # def loss(self, inputs, ouputs):
    #     return 

# class Trainer():
#     def __init__(self, model) -> None:
#         self.model = model

#     def train(self, input, output, epochs):
#         for epoch in range(epochs):
#             with tf.GradientTape() as tape:
#                 pred = self.model(input)
#                 loss = tf.reduce_mean(tf.square(pred - output))
#             grads = tape.gradient(loss, [self.model.w, self.model.b])
#             self.model.w.assign_sub(0.1 * grads[0])
#             self.model.b.assign_sub(0.1 * grads[1])
#             print("epoch %d loss %f" % (epoch, loss.numpy()))


# if __name__ == "__main__":
#     XORNet = XORNet(2, 1)
#     trainer = Trainer(XORNet)
#     trainer.train(x, y, 1000)
#     print(XORNet(x))

class XORNet(tf.keras.Model):
    def __init__(self, input, output):
        super(XORNet, self).__init__()
        
        # Input to Hidden Layer
        self.w1 = tf.Variable(tf.random.normal([2, 1]))
        self.b1 = tf.Variable(tf.random.normal([1]))
        
        # Hidden to Output Layer
        # self.w2 = tf.Variable(tf.random.normal([2, 1]))
        # self.b2 = tf.Variable(tf.random.normal([1]))

    def call(self, inputs):
        # First Layer (Hidden)
        z1 = tf.matmul(inputs, self.w1) + self.b1
        a1 = tf.nn.relu(z1)
        
        # Second Layer (Output)
        # z2 = tf.matmul(a1, self.w2) + self.b2
        # output = tf.nn.sigmoid(z2)
        
        return a1


class Trainer():
    def __init__(self, model) -> None:
        self.model = model

    def train(self, input, output, epochs):
        for epoch in range(epochs):
            with tf.GradientTape() as tape:
                pred = self.model(input)
                loss = tf.reduce_mean(tf.square(pred - output))
            
            grads = tape.gradient(loss, [self.model.w1, self.model.b1])
            # grads = tape.gradient(loss, [self.model.w1, self.model.b1, self.model.w2, self.model.b2])
            self.model.w1.assign_sub(0.1 * grads[0])
            self.model.b1.assign_sub(0.1 * grads[1])
            # self.model.w2.assign_sub(0.1 * grads[2])
            # self.model.b2.assign_sub(0.1 * grads[3])
            print("epoch %d loss %f" % (epoch, loss.numpy()))

# Sample training data for XOR problem
# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))


print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# strategy = tf.distribute.MirroredStrategy(devices=None)

# with strategy.scope():
inputs = tf.constant([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
outputs = tf.constant([[0.], [1.], [1.], [0.]])

model = XORNet(2, 1)
trainer = Trainer(model)
trainer.train(inputs, outputs, epochs=500)

print(model(inputs))
print(tf.config.list_physical_devices('GPU'))