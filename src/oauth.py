from __future__ import absolute_import, print_function
import tweepy
import pandas as pd

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=""
consumer_secret=""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
# print(api.me().name)

# Get the geo code for USA
places = api.geo_search(query="United States", granularity="country")
place_id = places[0].id
print (place_id)
print (places)

searchquery = "donald trump OR trump since:2017-11-08 -filter:retweets"

output =[]
for tweet in tweepy.Cursor(api.search,q=searchquery,geo="true",lang="en",place="96683cc9126741d1" ,geocode="38.47935,-98.525391,2000.37km").items(1000):
    output.append(tweet)

print (len(output))

def toDataFrame(tweets):
    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]
    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet in tweets]
    return DataSet

#Pass the tweets list to the  function to create a DataFrame
DataSet = toDataFrame(output)
print ("done")

#print DataSet.userTimezone
DataSet.to_csv('trumpdata.csv', sep=',',encoding='utf-8')