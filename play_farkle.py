import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import pdb

def roll(n):
    return([np.random.randint(1,6) for x in range(n)])

def score_hand_pick_keepers(hand):
    starting_hand_number = len(hand)

    str_for_search = ''.join([str(x) for x in hand])

    # score 1's and 5's naively
    a_num = sum(1*[x.find('1')>-1 for x in str_for_search])
    a_keep = '1' * a_num
    a = 100 * a_num

    b_num = sum(1*[x.find('5')>-1 for x in str_for_search])
    b_keep = '5' * b_num
    b = 50 * b_num

    # score triples
    # pdb.set_trace()
    c = 0
    c_keep = ''
    for x in range(1,7):
        bonus = 1 + (x==1)*9
        val = x*100
        c_new = (sum(1*[y.find(str(x))>-1 for y in str_for_search])==3) * val * bonus
        if c_new > c:
            c_keep = str(x) * 3
        c = max(c , c_new)

    # four, five, six of a kind
    d = 0
    d_keep = ''
    for z in [4,5,6]:
        val = 1000 + (z-4)*1000
        d_new = val*(Counter(str_for_search).most_common()[0][1] == z)
        if d_new > d: d_keep = Counter(str_for_search).most_common()[0][0] * z
        d = max(d, d_new)

    # 1-6 straight
    e = (sorted(hand) == [1,2,3,4,5,6]) * 1500
    if e > 0 : e_keep = '123456'
    else: e_keep = ''

    # 3 doubles
    try:
        x = 1*(Counter(str_for_search).most_common()[0][1] == 2)
        x_keep = str(Counter(str_for_search).most_common()[0][0]) * x * 2

        y = 1*(Counter(str_for_search).most_common()[1][1] == 2)
        y_keep = str(Counter(str_for_search).most_common()[1][0]) * y * 2

        z = 1*(Counter(str_for_search).most_common()[2][1] == 2)
        z_keep = str(Counter(str_for_search).most_common()[2][0]) * z * 2
    except:
        x,y,z = 0,0,0
        x_keep, y_keep, z_keep = '','',''
    f = x * y * z * 1000
    f_keep = x_keep + y_keep + z_keep

    # 4x2 & 1x2
    try:
        x = 1*(Counter(str_for_search).most_common()[0][1] == 4)
        x_keep = str(Counter(str_for_search).most_common()[0][0]) * x * 4
        y = 1*(Counter(str_for_search).most_common()[1][1] == 2)
        y_keep = str(Counter(str_for_search).most_common()[1][1]) * y * 2
    except:
        x,y = 0,0
        x_keep, y_keep = '',''
    g = x * y * 1500
    g_keep = x_keep + y_keep

    # 2x3
    try:
        x = 1*(Counter(str_for_search).most_common()[0][1] == 3)
        x_keep = str(Counter(str_for_search).most_common()[0][1]) * x * 3
        y = 1*(Counter(str_for_search).most_common()[1][1] == 3)
        y_keep = str(Counter(str_for_search).most_common()[1][1]) * y * 3
    except:
        x,y = 0,0
        x_keep, y_keep = '',''
    h = x * y * 2500
    h_keep = x_keep + y_keep

    # this section here is kinda shitty, could be less shitty
    scores = [a, b, c, d, e, f, g, h]
    keepers = [a_keep, b_keep, c_keep, d_keep, e_keep, f_keep, g_keep, h_keep]
    scores_winner = max(scores)
    keepers_winner = keepers[scores.index(scores_winner)]
    resulting_hand = str_for_search
    for each in keepers_winner:
        resulting_hand = resulting_hand.replace(str(each),'')
    #assert len(keepers_winner) + len(resulting_hand) == starting_hand_number

    # build in something like if you get 333114
    # so you keep 333 for 300
    # then what about those two 11s
    # gotta build some manual logic here at the end for grabbing any extra 1s n 5s

    return(hand, scores_winner, keepers_winner, resulting_hand)


def play_farkle(accept_threshold, verbose = True):
    running_score = 0
    score = 1
    re_roll = 6

    while (score > 0) & (running_score < accept_threshold):
        #roll dice, play farkle and update score
        hand_in, score, keepers, hand_out = score_hand_pick_keepers(roll(re_roll))
        running_score = running_score + score

        #print results for checking
        if verbose == True:
            print(hand_in)
            print(score)
            print(keepers)

        # set up for next roll
        if hand_out == '':
            re_roll = 6
        else:
            re_roll = len(hand_out)

        running_score = running_score * (score != 0)

    return(running_score)


if __name__ == '__main__':
    print(play_farkle(500, True))
