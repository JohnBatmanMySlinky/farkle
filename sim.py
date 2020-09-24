import play_farkle as play
import numpy as np
import matplotlib.pyplot as plt


# sim scores
sim_rounds = 10
sim_means = []
sim_medians = []
sim_stds = []
sim_range_lower = 100
sim_range_upper = 1100
sim_range_by = 100
sim_range = range(sim_range_lower, sim_range_upper, sim_range_by)
for t in sim_range:
    print(t)

    # sim i games with t threshold
    # log all scores
    sim_scores = []
    for i in range(0,sim_rounds):
        sim_scores.append(play.play_game_of_farkle(t,10000,False))

    # store mean and sd for each t
    sim_means.append(np.mean(sim_scores))
    sim_medians.append(np.median(sim_scores))
    sim_stds.append(np.std(sim_scores))


plt.plot(sim_means, label = 'mean')
plt.plot(sim_medians, label = 'median')
plt.plot(sim_stds, label = 'std dev')
plt.xticks(range(0,sim_range_upper/sim_range_by - 1),sim_range)
plt.legend()
plt.show()




# sim number of rounds to win
# I think that I should save off a histogram of # rounds to win for a given t
# how to think about what strategy is optimal as a function of your opponent's strategies?
# what is threshold varied throughout the game????
