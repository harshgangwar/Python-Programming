# Python 3

max_value = -1000
 
test_case = input()
test_case = int(test_case)
while test_case > 0:
    no_of_tweets = input()
    tweets_dict = {}
    no_of_tweets = int(no_of_tweets)
    while no_of_tweets > 0:
        count = 1
        tweet = input()
        user_name = tweet.split(' ')[0]
 
        if user_name in tweets_dict:
            tweets_dict[user_name] = tweets_dict[user_name] + 1
        else:
            tweets_dict[user_name] = count
        no_of_tweets -= 1
 
    list_of_users = []
    for k in tweets_dict:
        if max_value <= tweets_dict[k]:
            if max_value < tweets_dict[k] and max_value in [ tweets_dict[x] for x in list_of_users]:
                for list_val in list_of_users:
                    if tweets_dict[list_val] == max_value:
                        list_of_users.remove(list_val)
            list_of_users.append(k)
            max_value = tweets_dict[k]
    list_of_users.sort()
 
    # Final Result
    for resultant_key in list_of_users:
        print (resultant_key, tweets_dict[resultant_key])
    test_case -= 1
    
# INPUT
# 1
# 4
# sachin tweet_id_1
# sehwag tweet_id_2
# sachin tweet_id_3
# sachin tweet_id_4

# OUTPUT
# sachin 3
    
