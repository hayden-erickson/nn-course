# Module 1 Neuron

## Video #1

> Introducing the Module What’s the topic of this video and where does it fit
> in within the overall training? 

A neural net is built up of a bunch of neurons connected. The idea is that the
neuron itself isn’t really what’s important, but rather the connections between
them. A neuron is basically a gate that combines a bunch of inputs and passes
along a single value. 

Once we understand the neuron, we can connect them together into our network.

> Why is this topic important to your student’s overall life, career, health,
> relationship, and our greater society? 

- It is used in all modern ML
- understanding our brains can help cure disease.
- Our brains are the most intelligent things we know of so it just makes sense
  that we would try to replicate them in machines
- Our lives become a little easier when our machines get smarter
- Changing the neuron or finding a new way to implement could completely change
  NN’s

> What’s a personal story that illustrates this topic and the struggles you’ve
> faced dealing with it? What mindset helped you deal with it? 

Because we’ve given a name to this thing that combines inputs (a neuron) it is
easy to think that neurons actually exist in a neural network, but they do not!
The neuron isn’t a thing it’s just a sequence of operations that take an input
and produce an output much like a function in code. You can basically think of
a neuron like this y = 2x. That function isn’t really a thing it’s just an
operation. Ultimately there is some input like a picture and some output like
the class of object in the picture. The only way to get from a bunch of pixel
values to an answer is by combining the pixel values together. Since the pixel
values are just numbers, we must use numeric functions to get to the final
answer. That’s where the neuron comes in

> What are the goals of this module? 

Understand the neuron and the motivation behind choosing to emphasize
connections rather than rules. Where did the neuron idea start and why? 

> What do you want the student to think, do and setup as a habit by the end of
> the module? 

Always ask why. Tinker a play around, get your hands dirty, and try things out. 

## Video #2

> Teaching Your Content/Framework/Steps What specific concepts, takeaways, or
> steps should someone take or know to improve in this area? Try to teach 3-10
> points. This is where you really add the value and TEACH! 

1.	A Neuron is just a numeric function. It takes in multiple inputs and
    produces a single output, like a real neuron.
2.	It may or may not have a bias and an activation function.
3.	The activation function affects how the output is interpreted. For
    instance, if we have no activation function, the output is a continuous
    value like a house price or conversion rate. When we have an activation
    function we can interpret the output as a probability of something
    happening which is between 0 and 1. Think about the configurable sprayer on
    a hose attachment or shower head. 
4.	Given a single example, the only thing we can change is the weights or the
    activation function in order to change the output. We change the weights to
    try to make the output closer to the actual value. 
5.	Without an activation function, the output is just a hyper-plane. If we
    just have a single weight and a single input, it’s a line. 2 inputs are a
    plane. 
6.	Because one neuron can only produce one output, we must have multiple
    neurons for outputs such as classes where there is one neuron per class.
    For each class the neuron outputs the probability that the input belongs to
    that class. This is what image classification networks do. (Segway into
    networks).  One neuron per class and they can all be independent
7.  Each weight is a line, the whole neuron makes a plane. Think of just one
    input column compared to output. As number of rooms goes up, so does house
    price (positive weight). As distance from city goes up, price goes down
    (negative weight).

> Now that the student knows the steps or important concepts, what are the Do’s
> and Don’ts they should be aware of? 

Dos
1.	Literally try to implement one yourself
2.	Try to connect a bunch together
3.	See if you can find out how the neuron is similar to linear regression by
changing the weight values Don’ts
1.	worry if you don’t know why this matters yet, we will get there. 2.	


> where might they screw up, get lost, or be disappointed, and how can they
> deal with that well? 

Throughout the course don’t get discouraged by the math. It is very complicated
and there is a lot going on. It just takes time to digest. It’s like each a ton
of food. You can’t eat all of it at once it is going to take multiple days.
Each day that you come back and look it will be easier to understand. Don’t be
afraid to look something up! I literally had to review all the math when I
first started learning this stuff. I barely remembered anything from school and
often visited websites for high school math courses. Anyone can understand this
stuff even if you’re not crazy about math. The hardest thing is taking a
derivative, but even that has a very intuitive explanation that I visually
explain.  Honor the struggle and be excited about how amazing this is.

## Video #3

> Case Study What is a case study - about you, one of your students, or in the
> greater marketplace - that really illustrates what you’ve been teaching in
> this module? 

Why neurons? What made us think that we should use them for computation and
where did this idea begin? 
-	research from 1870 to 1900 discovered the structure of neurons connected in
  an electrical network
-	from the 1930-1950 with the advent of digital computers, it  was proposed
  that a brain could be replicated electronically
-	1940 to 1950 shown that computation can be done by idealized networks of
  neurons
-	1949 Donald Hebb’s proposes theory that repeated coincident neuron firing
  leads to strengthened connections (fire together wire together)


> Tell the story, and give some teaching points. What is a download or a tool
> that could help your student better understand or implement your idea? (For
> example, this download is a tool that is helping you implement what Brendon
> taught about online courses in this module). 

python notebook

> What cheerleading or parting words of advice and encouragement can you give
> at the end of this video? (Also, don’t forget to ask your student’s to
> participate by commenting or asking questions on the video).

Exciting journey
-	Brand new research
-	State of the art
-	Can do amazing things This stuff is mind blowing that it even works You’re
  not going to be intimidated by it like others are because we’re going through
  it together and at the end a whole new world is going to open up to your
  understanding.


# Module 2 Network

## Video #1

> Introducing the Module What’s the topic of this video and where does it fit
> in within the overall training? 

- made up of a bunch of neurons
- all deep learning is some kind of NN
- Allow us to define some computational shorthand
- Deep learning does not happen with a single neuron

> Why is this topic important to your student’s overall life, career, health,
> relationship, and our greater society? 

- voice recognition, natural language understanding, search, predicting cancer
  all through NN's
- high level concepts need abstraction
- This is how our own brain works

> What’s a personal story that illustrates this topic and the struggles you’ve
> faced dealing with it? What mindset helped you deal with it? 

Understanding how the connection weights turn into a matrix.
Forward propagation in the context of the whole network
The fact that getting from the input data to the output prediction is literally
just multiplying matricies. 

Mindset: Everything is just a number and you're just feeding numbers through a
function to get an output. There is no spoon!

> What are the goals of this module? 

Understand how we can take images and rows of data and transform them into predictions
using a network of neurons represented as a matrix.

> What do you want the student to think, do and setup as a habit by the end of
> the module? 

it's just matrix multiplication. With a single example, the only thing that we
can change are the weights. 


## Video #2

> Teaching Your Content/Framework/Steps What specific concepts, takeaways, or
> steps should someone take or know to improve in this area? Try to teach 3-10
> points. This is where you really add the value and TEACH! 

1. put all input weights into the neuron in a single list. Use vector dot
   product to multiply all weights by all inputs in one step.
2. A layer is just a list of neurons that are not connected. For each neuron we
   have a weight vector and we have a list of neurons so we have a list of
   vectors i.e. a matrix. So a layer can be represented by a matrix which is
   the strength of connections to previous layer.

> Now that the student knows the steps or important concepts, what are the Do’s
> and Don’ts they should be aware of? 

> where might they screw up, get lost, or be disappointed, and how can they
> deal with that well? 

## Video #3
