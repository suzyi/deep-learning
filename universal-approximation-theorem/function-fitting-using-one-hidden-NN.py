'''
# Function fitting using neural network

For understanding the potential mechanism.

Sep 3, 2018.

Guorui Shen, guorui233@outlook.com

In this notebook, we consider the task of function fitting, particularly the one-dimensional function $$y=sin(t),$$ was adopted to illustrate the basic idea.
'''
import tensorflow as tf
import numpy as np
from designBasis import *
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

# Just enable only one of them!
# sine
ff = lambda t: np.sin(t)

# # piecewise function
# def ff(x):
#     conds = [x < 1, (x >= 1) & (x <= 2), x > 2]
#     funcs = [lambda x: x, lambda x: 1, lambda x: -2*x + 5.]
#     return np.piecewise(x, conds, funcs)

# # step function
# def ff(x):
#     conds = [x < 1, x >= 1]
#     funcs = [lambda x: 0, lambda x: 2.]
#     return np.piecewise(x, conds, funcs)

# Parameter settings.
[a, b] = [0.0, 2.0*np.pi]  # interval
n_hidden_nodes = 3  # the number of basis
n_examples = 100    # the number of examples

t_train = np.linspace(a, b, n_examples, dtype = np.float32)
f_train = ff(t_train)
t_basis = np.linspace(a, b, 8, dtype = np.float32)

## Function Fitting using Designed Method
slope, Z = constructZ(t_train, a, b, n_hidden_nodes)
plt.figure()
for i in range(n_hidden_nodes):
    plt.plot(t_train, Z[:, i],'--', markersize = 0.01)
    
w1 = np.reshape(slope, (1,-1), np.float32)
b1 = np.ones((1, n_hidden_nodes))
temp2 = np.dot(np.linalg.pinv(Z), f_train)
w2 = temp2.reshape(-1, 1)

# Loss of the designed method
print np.linalg.norm(np.matmul(Z, w2) - f_train.reshape(-1, 1), 'f')

## Make Prediction
num_input = 1
num_output = 1

inputs = t_train.reshape(-1, 1)
outputs = f_train.reshape(-1, 1)

# Store layers weight & bias
weights = {
    'h1': tf.constant(w1, tf.float32),
    'out': tf.constant(w2, tf.float32)
}
biases = {
    'b1': tf.constant(b1, tf.float32)
}

# tf Graph input
In = tf.placeholder("float", [None, num_input])
Out = tf.placeholder("float", [None, num_output])

def neural_net(x):
    layer_1 = tf.nn.relu(tf.add(tf.matmul(x, weights['h1']), biases['b1']))
    return tf.matmul(layer_1, weights['out'])

predictor = neural_net(In)
error_op = tf.norm(predictor - Out, 2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    pred = sess.run(predictor, feed_dict={In: inputs})
    print('The fitting error over the training data set is {:.5f}'.\
         format(sess.run(error_op, feed_dict={In: inputs, Out: outputs})))
    
### Visualization
fig, ax = plt.subplots()
ax.plot(t_train, f_train, 'k-', t_train, pred, 'r--', markersize = 1)

axins = zoomed_inset_axes(ax, 2.5, loc=1)
# sub region of the original image
x1, x2, y1, y2 = 3.6, 4.3, -.9, -.525
axins.plot(t_train, f_train, 'k-', t_train, pred, 'r--', markersize = 1)
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

plt.xticks(visible=False)
plt.yticks(visible=False)

# draw a bbox of the region of the inset axes in the parent axes and
# connecting lines between the bbox and the inset axes area
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.6")

ax.legend(['true', 'approximated'], loc=3, ncol=1)
plt.savefig(str(n_hidden_nodes)+'-nodes.pdf', transparent=True)

plt.draw()
plt.show()