'''
Author info:
    Guorui Shen, guorui233@outlook.com
    
In order to determine the unknown parameters (W1, W2, b) of a single-hidden-layer neural network, the non-convex problem    
    min ||relu(X*W1 + b)*W2 - Y||_2^2,
is considered, where X and Y are given with the shaple of (m, dx) and (x, dy), respectively.

We will manually design and construct the matrix Z
    Z = relu(X*W1 + b),
in which a single column represents a basis.
'''

import numpy as np

def basis(t, a, b, n_hidden_nodes, i):
    '''
    input:
        t: a vector consisted of equally distributed points from an interval.
        a, b: the start and end point of the interval [a, b].
        n_hidden_nodes: the number of hidden nodes, or the number of columns of Z.
        i: the ith basis.
    output:
        slope_i: slope of the ith basis.
        values: values of the ith basis at discrete points contained within t.
    '''
    slope_i = n_hidden_nodes/(i*(a-b)) # i = 1, 2, \cdots, n
    conds = [t < a + i*(b-a)/n_hidden_nodes, t >= a + i*(b-a)/n_hidden_nodes] # conditions
    funcs = [lambda t: slope_i * t + 1, lambda t: 0]
    values = np.piecewise(t, conds, funcs)
    return slope_i, values

def constructZ(t, a, b, n_hidden_nodes):
    '''
    input:
        t: a vector consisted of equally distributed points from an interval.
        a, b: the start and end point of the interval [a, b].
        n_hidden_nodes: the number of hidden nodes, or the number of columns of Z.
    output:
        slope: 
        Z:
    '''
    len_t = len(t)
    slope = []
    Z = np.zeros((len_t, n_hidden_nodes), dtype = np.float32)
    for i in range(1, n_hidden_nodes+1):
        temp = basis(t, a, b, n_hidden_nodes, i)
        slope.append(temp[0])
        Z[:, i-1] = temp[1]
    return slope, Z

class neuralnetwork:
    """
    Return a Relu activated single hidden neural network:
        Y = relu(X*W1 + b)*W2.
    """
    def __init__(self):
        self.weights_hidden = None
        self.weights_out = None
        self.bias = None
    
    def assign(self, weights_hidden, weights_out, bias):
        self.weights_hidden = weights_hidden,
        self.weights_out = weights_out,
        self.bias = bias
    
    def predict(self, x):
        layer_hidden = np.maximum(np.matmul(x, self.weights_hidden)+self.bias, 0)
        return np.matmul(layer_hidden, self.weights_out)