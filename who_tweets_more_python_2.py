# Python 2

import sys
 
max_value = -sys.maxint - 1
 
test_cases = input()
while test_cases > 0:
    no_of_tweets = input()
    tweets_dict = {}
    while no_of_tweets > 0:
        tweet = raw_input()
        user_name = tweet.split(' ')[0]
 
        if user_name in tweets_dict:
            tweets_dict[user_name] = tweets_dict[user_name] + 1
        else:
            tweets_dict[user_name] = 1
        no_of_tweets -= 1
 
    list_of_usernames = []
    max_value = -sys.maxint - 1
    for k in tweets_dict:
        if max_value <= tweets_dict[k]:
            if max_value < tweets_dict[k] and max_value in [ tweets_dict[x] for x in list_of_usernames]:
                for list_val in list_of_usernames:
                    if tweets_dict[list_val] == max_value:
                        list_of_usernames.remove(list_val)
            list_of_usernames.append(k)
            max_value = tweets_dict[k]
    list_of_usernames.sort()
 
    # Final Result
    for resultant_key in list_of_usernames:
        print resultant_key, tweets_dict[resultant_key]
    test_cases -= 1
    
# INPUT
# 1
# 4
# sachin tweet_id_1
# sehwag tweet_id_2
# sachin tweet_id_3
# sachin tweet_id_4

# OUTPUT
# sachin 3
