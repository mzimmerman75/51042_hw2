# Problem 1

import statistics
from typing import final

dice = {
    'Boo' : (0, 0, 5, 5, 7, 7),
    'Bowser' : (0, 0, 1, 8, 9, 10),
    'BowserJr' : (1, 1, 1, 4, 4, 9),
    'Daisy' : (3, 3, 3, 3, 4, 4),
    'DiddyKong' : (0, 0, 0, 7, 7, 7),
    'DonkeyKong' : (0, 0, 0, 0, 10, 10),
    'DryBones' : (1, 1, 1, 6, 6, 6),
    'Goomba' : (0, 0, 3, 4, 5, 6),
    'HammerBro' : (0, 1, 1, 5, 5, 5),
    'Koopa' : (1, 1, 2, 3, 3, 10),
    'Luigi' : (1, 1, 1, 5, 6, 7),
    'Mario' : (1, 3, 3, 3, 5, 6),
    'MontyMole' : (0, 2, 3, 4, 5, 6),
    'Peach' : (0, 2, 4, 4, 4, 6),
    'PomPom' : (0, 3, 3, 3, 3, 8),
    'Rosalina' : (0, 0, 2, 3, 4, 8),
    'ShyGuy' : (0, 4, 4, 4, 4, 4),
    'Standard' : (1, 2, 3, 4, 5, 6),
    'Waluigi' : (0, 1, 3, 5, 5, 7),
    'Wario' : (6, 6, 6, 6, 0, 0),
    'Yoshi' : (0, 1, 3, 3, 5, 7)
}

#part a
def mean_stddev_stdlib(dict):

    mario_dict = {}

    for i in dict:
        mean_std = []
        
        mean_std.append(statistics.mean(dict[i]))
        mean_std.append(statistics.stdev(dict[i]))

        mario_dict[i] = mean_std


    return(mario_dict)

#part b
def mean_stddev_no_stdlib(dict):

    mario_dict = {}

    for i in dict:
        mean_std = []

        n_len = len(dict[i])
        n_sum = sum(dict[i])
        mean = n_sum / n_len
        mean_std.append(mean)

        std = (sum([((x - mean) ** 2) for x in dict[i]]) / n_len) ** 0.5
        mean_std.append(std)

        mario_dict[i] = mean_std


    return(mario_dict)


#part c
def mean_stddev_sorted(dict):

    mario_dict = {}

    for i in dict:
        mean_std = []

        n_len = len(dict[i])
        n_sum = sum(dict[i])
        mean = n_sum / n_len
        mean_std.append(mean)

        std = (sum([((x - mean) ** 2) for x in dict[i]]) / n_len) ** 0.5
        mean_std.append(std)

        mario_dict[i] = mean_std

    final_dict = {}
    mario_sorted = sorted(mario_dict.values(), reverse=True)
    final_dict = mario_sorted
    #does this work???
    #this is just sorting by the first number (which is the mean)
    #should i use the logic from the function without the imported library or with it?
    #need to make this a dict, keys have been lost

    return(final_dict)


#part d
def mean_stddev_filtered(dict):
    #using logic from part a

    mario_dict = {}

    for i in dict:
        mean_std = []
        
        mean_std.append(statistics.mean(dict[i]))
        mean_std.append(statistics.stdev(dict[i]))

        mario_dict[i] = mean_std

    #final_dict = dict[filter(lambda x: x[0] >= 3.5, mario_dict.items())]
    #dict object is not callable, use brakcets???

    #using dict comprehension
    final_dict = {key: value for (key, value) in mario_dict.items() if value[0] >= 3.5}
    #final_dict = sorted(final_dict.values(), reverse=True)
    #considering this is filtered on the mean
    #I would choose play as Bowser


    return(final_dict)



#print(mean_stddev_stdlib(dice))
#print(mean_stddev_no_stdlib(dice))
print(mean_stddev_sorted(dice))
#print(mean_stddev_filtered(dice))