# The Galton box. Assignment 1 Randomized Algorithms

This project intends to simulate a Galton board or Galton box, a device used to illustrate the central limit theorem. 
In particular, the purpose of this project is to show experimentally that with a sufficiently large sample, the binomial 
distribution is approximated by the normal distribution.

All the relavant code is provided in the galtonbox.py file. First we define as parameters of the experiment the number 
of balls N and the number of levels in which they can fall n. We can adjust these two parameters as needed for the 
various simulations. We then simulate the Galton board with a one dimentional chart, were each ball starts at the 
initial box 0 and "bounces" to the box on the right with probability 1/2. After n steps each ball will be at some box 
of the board. After the simulation is done we calculate some relevant paramters, such as the mean of the observations 
and the standard deviation.

We then define the normal distribution that we want to compare with the experimental results. Similarly, we calculate the 
expected value and the standard deviation of this distribution. Finally, we compute the mean quadratic error of the 
observations with respect to the theoritical value from the normal distribution.

We then plot the experimental results of the simulation as well as the expected theoretical distribution.

