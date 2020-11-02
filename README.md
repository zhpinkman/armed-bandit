# AMALearn

For installation, run: 
`pip install -e .`


### important observations:

* one of most important things that we can conspicuously say from the charts modeling the class-arriving task is that the monetary value regarding the value of time is so potent that adjusting this hyper-parameter can largely impact the convergance of our model. 

By changing this monetary value from 3.33 that is equal to 4 timesteps to 7.1 we can spot the the point in 4.1.
with monetary values lower than this, the value of time can readily outweigh the value of money. But at this point that monetary value is equal to punishment of 2 minutes delay or 5 minutes early arriving, we can see that the model is considering options other than just taking taxi and getting too soon to the university.