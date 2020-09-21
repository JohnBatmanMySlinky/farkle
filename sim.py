from play_farkle import play_farkle
import numpy as np
import matplotlib.pyplot as plt


# sim scores
sim_rounds = 10000
sim_means = []
sim_stds = []
for t in range(100,2100,100):
    print(t)

    # sim i games with t threshold
    # log all scores
    sim_scores = []
    for i in range(0,sim_rounds):
        sim_scores.append(a_turn(t,False))

    # store mean and sd for each t
    sim_means.append(np.mean(sim_scores))
    sim_stds.append(np.std(sim_scores))


plt.plot(sim_means)
plt.plot(sim_stds)
plt.show()




# sim number of rounds to win
# I think that I should save off a histogram of # rounds to win for a given t
# how to think about what strategy is optimal as a function of your opponent's strategies?
# what is threshold varied throughout the game????
