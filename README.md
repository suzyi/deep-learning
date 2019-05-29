# deep-learning

| Date | codes |
| ---- | ----- |
| Nov 11, 2018 | [universal-approximation-theorem](https://github.com/suzyi/deep-learning/tree/master/universal-approximation-theorem) |
### Top authors based on their NeurIPS papers
+ [Andrew Y. Ng](https://scholar.google.com/citations?user=mG4imMEAAAAJ&hl=en)
+ [Michael I. Jordan](https://scholar.google.com/citations?user=yxUduqMAAAAJ&hl=en)
+ [Ilya Sutskever](https://scholar.google.com/citations?user=x04W_mMAAAAJ&hl=en)
+ [Geoffrey Hinton](https://scholar.google.com/citations?user=JicYPdAAAAAJ&hl=en)
+ [Bernhard Schölkopf](https://scholar.google.com/citations?user=DZ-fHPgAAAAJ&hl=en)
+ [Yoshua Bengio](https://scholar.google.com/citations?user=kukA0LcAAAAJ&hl=en)
+ [Alex Smola](https://scholar.google.com/citations?user=Tb0ZrYwAAAAJ&hl=en)
+ [Yair Weiss](https://scholar.google.com/citations?user=9DXQi8gAAAAJ&hl=en)
+ [Jeff Dean](https://scholar.google.com/citations?user=NMS69lQAAAAJ&hl=en&oi=sra)
+ [Kai Chen](https://scholar.google.com/citations?user=TKvd_Z4AAAAJ&hl=en)
+ [Partha Niyogi](http://people.cs.uchicago.edu/~niyogi/)
## Recommendation
### best papers that may relavant with my research
+ (One of the ICLR 2018 best papers) On the Convergence of Adam and Beyond.
+ (One of the NeurIPS 2018 best papers) Neural Ordinary Differential Equations.
+ (One of the ICLR 2017 best papers) Understanding deep learning requires rethinking generalization.

other selected papers:
+ Global convergence of the Heavy-ball method for convex optimization.
### deep learning courses
+ [EPFL course](https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/#information). This is a deep learning course provided by senior researcher FRANÇOIS FLEURET [(His homepage)](https://www.idiap.ch/~fleuret/), who is now an adjunct faculty in the School of Engineering of the École Polytechnique Fédérale de Lausanne.

#### scholars studying the theory of deep learning
+ [Yao Xie](https://www2.isye.gatech.edu/~yxie77/) is now an assitant professor at Gatech. I've read her paper "Relu Regression: Complexity, ...." at Dec 25-27, 2018.
+ [Shiyu Liang](https://www.shiyu-liang.com/), university of Illinois at Urbana-Champaign. I've read their paper [Why Deep Neural Network For Function Approximation? - ICLR 2017](https://arxiv.org/abs/1610.04161) at Sep, 2018.
+ [Yixuan Li](http://yixuanli.net/) now works for FB AI Lab. She is a co-worker of Shiyu Liang.
+ [Raman Arora](http://www.cs.jhu.edu/~raman/Home.html), assistant prof in John Hopkin univ. I've read his paper [Understanding deep neural networks with rectified linear units - ICLR 2018](https://arxiv.org/abs/1611.01491) at Oct 2018.
+ [Ruoyu Sun](https://sites.google.com/site/ruoyusun88/home), assistant professor in UIUC, was a postdoctoral scholar with Prof. Yinyu Ye.
+ [Yuandong Tian](http://www.yuandong-tian.com/), a Facebook AI researcher, got his phd from CMU. There're many practical interesting applications (including "A Reimplementation of AlphaGoZero", "") shown in his personal home page. Selected papers for theoretical understanding of neural networks includes [Gradient Descent Learns One-hidden-layer CNN: Don't be Afraid of Spurious Local Minima - ICML 2018](https://arxiv.org/abs/1712.00779) and [An Analytical Formula of Population Gradient for two-layered ReLU network and its Applications in Convergence and Critical Point Analysis](https://arxiv.org/abs/1703.00560), though I haven't read these two papers yet.
+ [Tenyu Ma](https://ai.stanford.edu/~tengyuma/) Graduated from Tsinghua (got his bachelor's degree at Andrew Chi-Chih Yao's CS pilot class) and Princeton (got his doctor's degree), now works in Stanford as a assitant professor. I've his paper "Identity Matters in Deep Learning" at the 2nd half year of 2017.
+ Researching on mixed integer programs and Relu DNN: [Thiago Serra](https://thiagoserra.com/) (with his ICML-2018 paper "Bounding and Counting Linear Regions of Deep Neural Networks").
+ [Matteo Fischett](http://www.dei.unipd.it/~fisch/). I've read his paper "Deep Neural Networks as 0-1 Mixed Integer Linear Programs: A Feasibility Study" at Oct-Nov, 2018.
#### depth-width tradeoff
+ Ronen Eldan and Ohad Shamir. The Power of Depth for Feedforward Neural Networks
+ [Raman Arora](http://www.cs.jhu.edu/~raman/Home.html), Johns Hopkins University. Selected publications: [Understanding Deep Neural Networks with Rectified Linear Units - ICLR 2018](https://arxiv.org/pdf/1611.01491.pdf)
#### paper recommondation
These papers are among good quality. If only I could find a paper that has good quality once every ten days. No matter how, this requires broadly reading among plentful literatures and references therein.
+ (Sep 5, 2018. I found this paper from Quora, by the recommondation of the author himself.) [Understanding Deep Neural Networks with Rectified Linear Units - ICLR 2018](https://arxiv.org/pdf/1611.01491.pdf), aims at universal approximation, one-hidden-layer NN optimization of Relu network.
+ (Nov 1, 2018. I found this paper from the reference at the end of [this paper](https://arxiv.org/abs/1806.06365)) [Deep Neural Networks as 0-1 Mixed Integer Linear Programs: A Feasibility Study](https://arxiv.org/abs/1712.06174). This paper aims at dead with the optimization problem of one-hidden-layer Relu NN using mixed integer programming (MIP). From this paper, I begin to know that MIP can be introduced into optimize Relu NN. Notice that solving integer programming exactly may take an exponential running time.
+ (Nov 14, 2018. Prof. Yuan recommend this paper to me, since one day I talk to him that the weights and biases in the final layer matters more and one can randomly initialize the weights and biases in other layer and then make a least square to calculate the weights in the final layer.) [Extreme learning machine: Theory and applications](https://www.sciencedirect.com/science/article/pii/S0925231206000385). This paper aims at universal approximation theory of one-hidden-layer NN with any kind of infinitely differentiable activation function. As I mentioned before at the begining of this paragraph, it gives an algorithm to train the single-hidden-layer NN. Main idea is, randomly initialize weights and biases and then make a least square for the weights that connects to the output layer. This paper follow a technique from [Capabilities of a Four-Layered Feedforward NN: 4 vs 3](https://ieeexplore.ieee.org/document/557662)
+ (Dec 26, 2018) I am still not sure if it's a good idea or not that [A Tropical Approach to Neural Networks with Piecewise Linear Activations](https://arxiv.org/abs/1805.08749) paper provides an innovative view of applying tropical geometry to Relu NN. This paper now (it's Dec 26, 2018) cited by only 1 paper.
+ (Dec 26, 2018) The paper "[ReLU Regression: Complexity, Exact and Approximation Algorithms](https://arxiv.org/pdf/1810.03592.pdf)", cited by 0 since posted on axiv.org (it's Dec 26, 2018) An auxiliary function method to eliminate the diffidulty of brute-forcely searching global optimality of single-hidden-layer Relu NN.
### Conferences recommendation
#### machine learning
The following international conferences are most cited conferences by nips, see [Top 10 venues that nips papers reference](https://www.microsoft.com/en-us/research/project/academic/articles/nips-conference-analytics/).
+ Top 1: NeurIPS - [nips 2018](https://nips.cc/Conferences/2018/Dates)  is held Dec 2nd - 8th, 2018 and paper submission deadline is May 18, 2018. No info about nips 2019.
+ Top 2: ICML - [ICML 2018](https://icml.cc/Conferences/2018/Dates) Thirty-fifth is held Jul 10 - 15, 2018. Paper Submission Opening is at Jan. 9, 2018, noon. [ICML 2019](https://icml.cc/Conferences/FutureMeetings) will be held at June 10 - 15, 2019.
+ Top 3: Journal of Machine Learning Research
+ Top 4: CVPR - [CVPR 2019](http://cvpr2019.thecvf.com/files/CFP_CVPR2019.pdf) will be held June 15-21, 2019 and the submission deadline is Nov 16th, 2018.
+ Top 5: Neural Computation
+ Top 6: COLT
+ Top 7: ICLR - International Conference on Learning Representation, founded by Yoshua Bengio & Yann LeCun. You can find all of reviews about accepted paper on [openreview-iclr](https://openreview.net/group?id=ICLR.cc). [ICLR 2019](https://iclr.cc/Conferences/2019/Dates), Paper Submission Deadline is 	Sept. 27, 2018.
+ Top 8: IEEE Transaction on Pattern Analysis
+ Top 9: Annals of Statistics
+ Top 10: UAI 

and some other conferences that cite nips most:
+ AAAI - American Association for AI. [AAAI-18](https://aaai.org/Conferences/AAAI-18/aaai18call/) has been held at Feb 2–7, 2018 and paper submission deadline was Sep 11, 2017. [AAAI-19] will be held at Jan 27 - Feb 1, 2019 and electronic papers due at Sep 5, 2018.
+ Neuralcomputing
+ ICCV

and some other recommendations from [quora - best conference on ML](https://www.quora.com/What-are-the-best-conferences-and-journals-about-machine-learning):
+ ECCV - European conference on computer vision. [ECCV 2018](https://eccv2018.org/) has been held Sep 8 - 14 2018 and paper submission deadline is March 14 2018.
+ CPAIOR - [CPAIOR 2018 accepted papers](https://sites.google.com/view/cpaior2018/program/accepted-papers)
#### control theory
+ CDC: IEEE Conference on Decision and Control
+ ACC: American Control Conference
+ IFAC: International Federation of Atomatic Control

#### optimization
## model
### Boltzmann machines
### GAN
### Adversirial neural networks
## Methodology
### deep learning
### transferring learning
### reinforcement learning
