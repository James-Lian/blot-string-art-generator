# Blot String Art Generator
This is a string art generator created in Hack Club's Blot Editor, inspired by... well, string art!  
Using the custom python script in this repository, you can upload your images (png or jpg) in order to copy an image array to then paste into the Blot editor, and then see the magic happens as the script automatically generates string art!  
You are free to control the size of the canvas, the size of the circular frame, the number of pins, the number of lines, and the contrast of the string art generator's results!  
Play around to generate string art that fits your liking. 

### The algorithm
The string art generator works by finding all possible paths between different pins, and evaluating the 'darkness' of the pixels beneath the path. Once it has selected the darkest path, it lightens the pixels underneath to prevent a behaviour where the algorithm continuously draws lines in the same dark area. 