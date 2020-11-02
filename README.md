

### important observations in part 2:

* one of most important things that we can conspicuously say from the charts modeling the class-arriving task is that the monetary value regarding the value of time is so potent that adjusting this hyper-parameter can largely impact the convergance of our model. 

* By changing this monetary value from 3.33 that is equal to 4 timesteps to 7.1 we can spot the the point in 4.1.
with monetary values lower than this, the value of time can readily outweigh the value of money. But at this point that monetary value is equal to punishment of 2 minutes delay or 5 minutes early arriving, we can see that the model is considering options other than just taking taxi and getting too soon to the university.

![](results/part2/Screenshot%20from%202020-11-02%2016-27-16.png)


* after some trials and also by adjusting the hyper-parameters that were cardinal factors in describing the behvaior and the decision making of the people regarding the period of time they wait for the bus service to save money, I found that the value that we assign to getting the class with delay and also the relative monetary value would be considerably determining. 

* At first we opt the utility function suggested by Kahnemman et al. with 0.88, 0.88, 2.55 for alpha, beta, and the punishment coefficient respectively. By considering different monetary values, that was so compelling that by altering this value the decision made by people will be influenced. By considering no value regarding the value of reaching the class early, people will just choose to take taxi and get to their class as soon as possible. By nudging the monetary value we observed that people shift toward choosing wait longer. This introduces a point where people have no more tendency toward taking a taxi or saving the money by take a bus ride. These observation are depicted in the charts attached to this document. 

* The below plot can illustrate the point that the monetary value is trivial compared to the value of getting to the class as soon as possible.

![](results/part2/Screenshot%20from%202020-11-01%2018-49-54.png)

* After some trials I have found that the monetary value of 5 and also the punishment coefficient of 3.25 will culminate in a equilibrium in which getting people don't want to miss the class no matter what is the expense. Moreover, they will wait patiently until the time that if they wait longer, they will miss the class. The plots showing the mean rate of opting these decisions are presented below:

![mean_rate_actions](results/part2/Screenshot%20from%202020-11-02%2017-12-42.png)