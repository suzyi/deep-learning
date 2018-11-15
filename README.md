# deep-learning
## Recommendation
### deep learning courses
+ [EPFL course](https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/#information). This is a deep learning course provided by senior researcher FRANÇOIS FLEURET [(His homepage)](https://www.idiap.ch/~fleuret/), who is now an adjunct faculty in the School of Engineering of the École Polytechnique Fédérale de Lausanne.

#### scholars studying the theory of deep learning
+ [Shiyu Liang](https://www.shiyu-liang.com/), university of Illinois at Urbana-Champaign. Selected publications: [Why Deep Neural Network For Function Approximation? - ICLR 2017](https://arxiv.org/abs/1610.04161)
+ [Raman Arora](http://www.cs.jhu.edu/~raman/Home.html), assistant prof in John Hopkin univ. Selected papers: [Understanding deep neural networks with rectified linear units - ICLR 2018](https://arxiv.org/abs/1611.01491).
+ [Ruoyu Sun](https://sites.google.com/site/ruoyusun88/home), assistant professor in UIUC, was a postdoctoral scholar with Prof. Yinyu Ye.
+ [Yuandong Tian](http://www.yuandong-tian.com/), a Facebook AI researcher, got his phd from CMU. There're many practical interesting applications (including "A Reimplementation of AlphaGoZero", "") shown in his personal home page. Selected papers for theoretical understanding of neural networks includes [Gradient Descent Learns One-hidden-layer CNN: Don't be Afraid of Spurious Local Minima - ICML 2018](https://arxiv.org/abs/1712.00779) and [An Analytical Formula of Population Gradient for two-layered ReLU network and its Applications in Convergence and Critical Point Analysis](https://arxiv.org/abs/1703.00560), though I haven't read these two papers yet.
+ [Tenyu Ma](https://ai.stanford.edu/~tengyuma/) Graduated from Tsinghua (got his bachelor's degree at Andrew Chi-Chih Yao's CS pilot class) and Princeton (got his doctor's degree), now works in Stanford as a assitant professor.
+ Researching on mixed integer programs and Relu DNN: [Thiago Serra](https://thiagoserra.com/) (with his ICML-2018 paper "Bounding and Counting Linear Regions of Deep Neural Networks") and [Matteo Fischett](http://www.dei.unipd.it/~fisch/) (with his paper "Deep Neural Networks as 0-1 Mixed Integer Linear Programs: A Feasibility Study"). 
#### depth-width tradeoff
+ Ronen Eldan and Ohad Shamir. The Power of Depth for Feedforward Neural Networks
+ [Raman Arora](http://www.cs.jhu.edu/~raman/Home.html), Johns Hopkins University. Selected publications: [Understanding Deep Neural Networks with Rectified Linear Units - ICLR 2018](https://arxiv.org/pdf/1611.01491.pdf)
#### paper recommondation
These papers are among good quality. If only I could find a paper that has good quality once every ten days. No matter how, this requires broadly reading among plentful literatures and references therein.
+ (Sep 5, 2018. I found this paper from Quora, by the recommondation of the author himself.) [Understanding Deep Neural Networks with Rectified Linear Units - ICLR 2018](https://arxiv.org/pdf/1611.01491.pdf), aims at universal approximation, one-hidden-layer NN optimization of Relu network.
+ (Nov 1, 2018. I found this paper from the reference at the end of [this paper](https://arxiv.org/abs/1806.06365)) [Deep Neural Networks as 0-1 Mixed Integer Linear Programs: A Feasibility Study](https://arxiv.org/abs/1712.06174). This paper aims at dead with the optimization problem of one-hidden-layer Relu NN using mixed integer programming (MIP). From this paper, I begin to know that MIP can be introduced into optimize Relu NN.
+ (Nov 14, 2018. Prof. Yuan recommend this paper to me, since one day I talk to him that the weights and biases in the final layer matters more and one can randomly initialize the weights and biases in other layer and then make a least square to calculate the weights in the final layer.) [Extreme learning machine: Theory and applications](https://www.sciencedirect.com/science/article/pii/S0925231206000385). This paper aims at universal approximation theory of one-hidden-layer NN with any kind of infinitely differentiable activation function. As I mentioned before at the begining of this paragraph, it gives an algorithm to train the single-hidden-layer NN. Main idea is, randomly initialize weights and biases and then make a least square for the weights that connects to the output layer. This paper follow a technique from [Capabilities of a Four-Layered Feedforward NN: 4 vs 3](https://ieeexplore.ieee.org/document/557662)
#### optimization
## model
### Boltzmann machines
### GAN
### Adversirial neural networks
## Methodology
### deep learning
### transferring learning
### reinforcement learning
