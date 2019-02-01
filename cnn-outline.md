# CNN Mini Course

# Module 1 Convolutions & Pooling

## Video 1 Why convolutions

not a matrix multiplication, but a mask
- padding
- stride

act as feature detectors
- low level = edges, smooth patches, or very small patterns
- mid level = basic shapes
- high level = complex patterns made of basic shapes

## Video 2 Why pooling
- max vs avg pooling
- invariance. Obscures the exact location of features detected by kernels. We
  don't care where the face is we just care that there's a face

[Why is the pooling layer used](https://www.quora.com/Why-is-the-pooling-layer-used-in-a-convolution-neural-network)

# Module 2 Back prop for convolutions
- Similar to fully connected b/c chain of operations
- Because the convolution kernel weights touch multiple inputs compared to the
  fully connected layer weights, we have to sum them together.
- max pooling only gets the gradient of the max with respect to input
- avg pooling will work the same as the activation function b/c it's linear

# Module 3 Transfer learning


Bonuses
- Style transfer guide
- image in-painting guide
- Capsule nets
- Generative Query Networks
- NEAT
- Controlling Game Characters



## Video #1

> Introducing the Module What’s the topic of this video and where does it fit
> in within the overall training?

Convolutional Neural Networks.


> Why is this topic important to your student’s overall life, career, health,
> relationship, and our greater society?


> What’s a personal story that illustrates this topic and the struggles you’ve
> faced dealing with it? What mindset helped you deal with it?


> What are the goals of this module?


> What do you want the student to think, do and setup as a habit by the end of
> the module?


## Video #2

> Teaching Your Content/Framework/Steps What specific concepts, takeaways, or
> steps should someone take or know to improve in this area? Try to teach 3-10
> points. This is where you really add the value and TEACH!


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



