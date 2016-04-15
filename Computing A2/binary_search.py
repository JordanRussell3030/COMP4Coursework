robs_friends = [1, 2, 3, 4, 6, 8]

rob_likes_cock = False
rob_failed_his_gf = False
robs_victim = 6
for robs_nan in robs_friends:
    robs_midlife_crisis = round(robs_friends[0] + robs_friends[5] / 2, 0)
    if robs_friends[robs_midlife_crisis] == robs_victim:
        rob_likes_cock = True
        print("Rob found his child")
    else:
        if robs_nan >= robs_victim:
            rob_failed_his_gf = True
        else:
            if robs_friends[robs_midlife_crisis] > robs_victim:
                robs_nan = robs_midlife_crisis - 1
            else:
                robs_nan = robs_midlife_crisis + 1
        print("The child got away")
    
