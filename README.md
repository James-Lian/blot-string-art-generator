# Blot String Art Generator
This is a string art generator created in Hack Club's [Blot Editor]([url](https://blot.hackclub.com/editor)), inspired by... well, string art!  
Insert a URL of your image in the outlined variable, and watch the magic happen!  
You are free to control the size of the canvas, the size of the circular frame, the number of pins, the number of lines, and the contrast of the string art generator's results!  
Play around to generate string art that fits your liking. 

(P.S. if you so wish, there is also a Python program to generate your own grayscale array from an image file. Just use a previous version of the JS file. )

### The algorithm
The string art generator works by finding all possible paths between different pins, and evaluating the 'darkness' of the pixels beneath the path. Once it has selected the darkest path, it lightens the pixels underneath to prevent a behaviour where the algorithm continuously draws lines in the same dark area. 

![An image of the Mona Lisa, generated as string art by an algorithm.](https://github.com/James-Lian/blot-string-art-generator/blob/main/examples/mona-lisa.png)
