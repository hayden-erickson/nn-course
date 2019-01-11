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
    changing the weight values

Don’ts
1.	worry if you don’t know why this matters yet, we will get there. 2.	
2. get discouraged that we're not actually talking about NN's yet, trust me we
   will get there and you will be glad you took the time here


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
  - logical functions XOR, AND, etc.
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

Don't reinvent the wheel. If you look hard enough you can almost always find an
existing implementation. Again, LOOK FOR A SOLUTION BEFORE YOU DECIDE TO CREATE
IT YOURSELF.


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
3. some layers are fully connected
4. Generally go from big to small
5. model zoos give ideal networks for certain tasks
6. network topology is an unsolved problem
7. matrix "reshapes" input
8. regression vs. classification network. single linear neuron vs softmax.
9. aside from input and output, layers are "hidden"
10. deep comes from multiple layers

> Now that the student knows the steps or important concepts, what are the Do’s
> and Don’ts they should be aware of? 

Do
- always question the architecture
- review a little tiny bit of linear algebra
- explore different activations and their effect
- look for new and exciting applications
- listen to podcasts on deep learning
- try to read papers (you may understand nothing, but it will make you smarter)

Don't
- think that this is the only way to do layers
- think that neural nets will solve all your problems


> where might they screw up, get lost, or be disappointed, and how can they
> deal with that well? 

drown in terminology
- one piece at a time, one word at a time, repeat
- you can't learning everything in a day
- anytime you start in a new place there will be things you don't know, eventually you get them

not understanding linear algebra or matrix multiplication
- linear algebra is really hard!!!!
- its just for convenience and efficiency and good for parallelization, not for understanding

may all seem too complicated
- it is extremely complicated, but it can be broken into small chunks which is what we'll do
- This stuff is dense, so in order to unpack the whole house it's gonna take some time

## Video #3
> Case Study What is a case study - about you, one of your students, or in the
> greater marketplace - that really illustrates what you’ve been teaching in
> this module? 

why layers? who came up with them why
layers are an empirical byproduct. They aren't really required for NNs to work.
However, NNs with many layers learn faster, require less weights and neurons,
and intuitively represent hierarchies of ideas. A hierarchy of ideas can be
thought of as sub tasks for instance if we try to turn audio into text the
first task is to identify phonemes or letter sounds, then syllables and spaces,
then entire words. Layers then are proposed to accomplish these tasks
sequentially.

more layers = less linearity. i.e. More complex relationships between input and
output. 

if we're trying to recognize a handwritten digit 0-9 there are many conditions
involved. First if someone writes anything then there should be some lines.
Next those lines need to be arranged in very specific ways. For example, to
identify a 6 the conditions might be 

1. are there lines 
2. are there lines in a circle 
3. are the circular lines near the bottom 
4. do the circular lines at the bottom have another line coming off 
5. is the line coming off of the left side of the circle 
6. is the line coming off going up (not down)

These conditions are all composed together and can be organized in a hierarchy.
This is the intuitive reason for layers

> Tell the story, and give some teaching points. What is a download or a tool
> that could help your student better understand or implement your idea? (For
> example, this download is a tool that is helping you implement what Brendon
> taught about online courses in this module). 

python notebook

> What cheerleading or parting words of advice and encouragement can you give
> at the end of this video? (Also, don’t forget to ask your student’s to
> participate by commenting or asking questions on the video).

That is the structure! You now know how AI is built! Next we will get into how it learns.
You are well on your way to understanding what I believe to be one of the most amazing innovations of our time.
If you've gotten this far that means you're really interested and want to learn and that is amazing. 
You want to be on the cutting edge of what tech can do and I celebrate you for that!


Because neural networks can approximate any function, they are limited only by
what you imagine. What I mean is that you can define almost any task and as
long as you have a way to measure how good the output is, then you can train a
neural network to do it. I can't wait to see what you come up with!


# Module 3 Gradient Descent

## Video #1

> Introducing the Module What’s the topic of this video and where does it fit
> in within the overall training? 

This is how the networks actually LEARN. This process is what allows us to find
connections between neurons that are optimal for the given task. It is
basically a bunch of trial and error. We try some connection weights at random,
then change them, then try again. If the change we made lowered the overall
error that our network makes, then we continue in the same direction.


> Why is this topic important to your student’s overall life, career, health,
> relationship, and our greater society? 

Gradient descent can be applied to any machine learning algorithm not just
neural networks. It is an automatic process that allows our predictor to figure
out how to function. It is amazing because it means that any task we can assign
a quantitative error to (i.e. a number for how good or bad it is doing) can be
automatically figured out using gradient descent. For example, if we want to
teach a neural network to classify images we need to give it an image and it
will give us a list of probabilities. Each probability represents how likely
the network predicts the image to belong to that class. For example if our
network can predict 3 different classes car, person, and road and we give it an
image of a person, then the list of probabilities it gives us would be
something like car: 1%, road: 2%, person: 97%. We know that the image is a
person so the optimal list should look like car: 0%, road: 0%, person: 100%.
Using these numbers we can say how wrong the network is by subtracting them.
The combination of gradient descent and neural networks has enabled what is now
called the AI revolution. It has allowed us to create self driving cars, facial
recognition, art generation, speech to text, language understanding and a whole
mess of other awesome stuff.


> What’s a personal story that illustrates this topic and the struggles you’ve
> faced dealing with it? What mindset helped you deal with it? 

This is where the course really goes deep and becomes more challenging. But,
stick with me and we'll get a feel for why this works not just a formula! This
topic and the next one took me months to fully grasp, but I was doing it on my
own. I literally stared at the equations for hours just trying to wrap my head
around them. BUT, the insights and intuition I've gained through continuous
consistency and determination are the reason I wanted to make this course. I
want to share with you the gut feel understanding of this math, yes it does
exist. The thing that kept me going through all of it was my inspiration.
Seeing what deep learning is capable of lit a fire inside me and I hope it will
for you too.

> What are the goals of this module? 

By the end of this module you will understand how to find the optimal solution
to a problem with a quantitative measure by defining a cost. You will
understand how optimizing a function can be simply thought of as rolling a ball
down a hill.


> What do you want the student to think, do and setup as a habit by the end of
> the module? 

The problem can always be broken down. We can disassemble functions into
simpler and simpler parts like legos. Always try to simplify the problem until
you can understand it, then you can build it back up one piece at a time. Often
complicated equations look very intimidating, but I think it's because they
contain so much meaning. If you break it apart, get an intuition for that small
piece, then put it make together it will make much more sense.


## Video #2

> Teaching Your Content/Framework/Steps What specific concepts, takeaways, or
> steps should someone take or know to improve in this area? Try to teach 3-10
> points. This is where you really add the value and TEACH! 

1. The slope of a line is the change in the output divided by the change in the input


> Now that the student knows the steps or important concepts, what are the Do’s
> and Don’ts they should be aware of? 


> where might they screw up, get lost, or be disappointed, and how can they
> deal with that well? 


## Video #3

> Case Study What is a case study - about you, one of your students, or in the
> greater marketplace - that really illustrates what you’ve been teaching in
> this module? 


> Tell the story, and give some teaching points. What is a download or a tool
> that could help your student better understand or implement your idea? (For
> example, this download is a tool that is helping you implement what Brendon
> taught about online courses in this module). 


> What cheerleading or parting words of advice and encouragement can you give
> at the end of this video? (Also, don’t forget to ask your student’s to
> participate by commenting or asking questions on the video).


# Module 4 Backpropagation


2. plot a complicated function like y = 1/2 * ( $100,000 - (x/5) )^2 we can decompose it by
   feeding the output of one part into the input of the next. If we break this
   into 3 separation functions it would look like this. y1 = x/5, y2 = $100,000 - y1, y3 = 1/2 * y2^2
3. we chained the functions together to create the final. This why we have
   something called the chain rule. 
4. We can plot each sub function and look at their slopes. If the slope is the
   change in output divided by the change in input we can write it like this dy/dx.
   d just stands for delta or change. 
5. we have this big giant function at the top, let's say this defines our cost
   or how wrong we are. What do we mean by wrong? Let's say we're talking about
   houses. We want to build a function that can take in the number of rooms in
   a house and give us back the price. We have a bunch of examples of houses
   with their corresponding price and number of rooms, but we don't have a way
   to take in a new house we've never seen before and try to predict it's
   price. In other words a new house has just been built. We know the number of
   rooms, but not what the price should be. So how can we come up with
   something that will be able to predict the price of a house well? This is
   where gradient descent comes in. So what does the big function above tell us? 
   It will give us a number that represents how wrong our house price predictor
   is. In other words it will tell us how different the price our function
   predicted is from the actual price of $100,000. This means that y1 is our
   predictor. In other words y1 is the function that will ultimately take in
   the number of room and give back a house price. The rest of the math is to
   tell us how wrong we are.
6. If y1 is our predictor then that is the thing we really want to change. In
   other words the changes we make to y1 ultimately affect how good our
   function is at predicting house prices. Therefore, we need to know how to
   change y1 so that we lower the cost, making it 'more correct.' We know our
   goal is to lower the cost because if we do that then our function will be
   giving us answers that are as close as possible to the correct answers. We
   can plot our cost function and see where the lowest point is. On the
   function curve this means we want to go down the slopes just like a ball
   rolling down a hill to get to the lowest point. Hence the name gradient
   descent. So what changes can we make to y1 to affect its output. We can
   change the value we multiple by x (the number of rooms).
7. How do we change the value to lower the cost function? 
