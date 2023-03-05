import tensorflow as tf
#import matplotlib.pyplot as plt

#측정데이터
x = [3, 4.4, 6.2, 7.5, 9.3]
y = [2.1, 4.2, 5.9, 8.3, 9.8]

#plt.scatter(x, y, label="input data set")


class LinearModel:
    def __call__(self, x):
        return self.Weight * x + self.Bias

    def __init__(self):
        self.Weight = tf.Variable(0.)
        self.Bias = tf.Variable(0.)


# 오차(손실) 구하기 함수
def loss(y, pred):
    return tf.reduce_mean(tf.square(y - pred))


# 학습 함수
def train(linear_model, x, y, lr):
    with tf.GradientTape() as t:
        current_loss = loss(y, linear_model(x))

    lr_weight, lr_bias = t.gradient(current_loss, [linear_model.Weight, linear_model.Bias])
    linear_model.Weight.assign_sub(lr * lr_weight)
    linear_model.Bias.assign_sub(lr * lr_bias)


# 학습 진행
linear_model = LinearModel()
epochs = 10000000

for epoch_count in range(epochs + 1):
    real_loss = loss(y, linear_model(x))
    train(linear_model, x, y, lr=0.003)
    if epoch_count % 100 == 0:
        print(
            f"{epoch_count}:: W:{linear_model.Weight.numpy()} b:{linear_model.Bias.numpy()} Loss: {real_loss.numpy()} ")