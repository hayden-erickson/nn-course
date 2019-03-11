Keras
  - tensorflow
  - theano
  - cntk
FastAI
  - PyTorch

Keras has a simple API that allows you to define a neural network of almost any
kind in just a few lines of code. One awesome feature of keras is its
pluggability. It allows you to write one neural net, but run it with several
distributed computing libraries. With a model defined in Keras you can export
it in theano, CNTK, and tensorflow. These libraries are all basically for
efficient distributed processing of matricies and arrays. In other words,
they're very fancy, very fast calculators for doing operations on a lot of
numbers. Which is why they can be used to create neural nets, efficiently
train, and run them across many cores or machines.

Tensorflow itself has the widest adoption of any deep learning library and
Keras is the official front end for it. All that means is if you wanted to
create a custom neural network using tensorflow, you could. However, it would
require more code because you actually have to define all the operations. For
instance matrix multiplication, activation functions, and vector addition.
Once the operations are defined, you manually chain them together in a sequence
to create your network.

However, with keras all you need to do is declare "new neural network" with
"new dense layer" No matrix operations or math involved whatsoever. Then, to
train the model is simply one call `model.train(...)`. Out of the box there are
many layer types defined that you can use essentially as legos to construct
your network. However, should you need to implement custom operations, layer
architectures, or connections you can do so in tensorflow, theano, or cntk and
then plug in to an existing network.

In the course we wrote all of the functions and their derivatives ourselves.
However, with all of these fancy calculators at our disposal that is not
necessary. Once you define a cost, activation, or any other numeric function
for that matter, the libraries handle the derivatives for you. This is a very
fascinating technique called auto-differentiation and it essentially involves
breaking all the math down into it's most basic component (addition or
multiplication) and then applying it in reverse.

Because there is no need to write any math, no dependency on a
specific distributed computation library, and a wide array of existing
functionality, keras is definitely the way to go if you're just starting out.

The interface keras uses to define networks and layers is very similar to the
structure used throughout the course. However, instead of running all the code
on one processor using numpy, we could run it on as many processors or GPU's as
we want.

If you wanted to, you could absolutely learn how to use tensorflow, theano, or
CNTK on their own, but you would write more code to get to the same place.

PyTorch is another deep learning framework that can also act as a fancy
calculator. It also has a relatively simple interface for just defining neural
nets. PyTorch is also meant to act as a drop in replacement for numpy with the
added benefit that it can parallelize the operations across many processors.
PyTorch is not as widely adopted as Tensorflow or Keras, but can definitely
hold it's own. An added benefit for PyTorch is that, because it can be a
stand-in for numpy, we can rewrite all of the examples in the course notebooks
to run on a GPU and be highly parallelized without having to change much about
the code. We would simply replace the calls to numpy operations with
those of pytorch and voila, it's parallelized.

So it seems that keras and tensorflow are our best bets for getting started
because of the simple api, distributed computation, and wide community adoption.
However, I would be remiss if I didn't mention performance. Obviously, when
running a ton of distributed operations, we must consider speed and Tensorflow
is not the fastest. On benchmark tests comparing several types of neural nets
trained using anywhere from one CPU to many GPUs, tensorflow is not always the
fastest. In general, tensorflow performs well on a single machine whereas other
libraries perform better on multiple machines. The bigger the single machine
(i.e. one server with 32 cores) the better tensorflow does. However, if you
want to start scaling up and using multiple machines, libraries such as caffe
and torch often perform better.

This lends itself to our use case though because often times we will only be
training on one machine. Unless you have really large models (with a lot of
layers) or are running a lot of experiments, you won't necessarily need to
leverage a cluster of machines. In that sense tensorflow and keras win again.
Also, because keras supports the use of CNTK for distributed computation, we
can tell keras to use that if we need to leverage the power of a cluster. CNTK
outperforms tensorflow when run on clusters of GPU's. And because we've used
keras as our front end API, to switch from using tensorflow to CNTK requires no
code changes.

There you have it, if you want to get started creating some neural network,
quickly prototype new architectures, have a pluggable interface that allows for
any customization, and leverage multiple distributed computing libraries then
keras is the way to go!
