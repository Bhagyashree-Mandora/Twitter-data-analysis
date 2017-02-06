import pandas
import re
import requests
import json

f= open("responses","w+")
tweets = pandas.read_csv('trumpdataCleaned1.csv')

# Send an HTTP POST request to the url on the website http://text-processing.com/docs/sentiment.html
# Since there is a limit on the number of requests per day, query for smaller chunks of data at a time
# The JSON responses are stored in a file
counter = 0
rowno = 0
for index, row in tweets.iterrows():
    rowno += 1
    if (rowno > 5578 and counter<900):
        text = row.loc['tweetText']
        text = re.sub(r'http\S+', '', text)  #remove urls
        text = re.sub(r'@\S+', '', text)    #remove @user tagging
        text = re.sub(r'RT', '', text)      #remove retweet indicator RT
        data = {"text": text}

        try:
            response = requests.post(url="http://text-processing.com/api/sentiment/", data=data)
            f.write(response.text+"\n")
            counter += 1
            #To test if the response is the correct JSON format and not a bad response 503
            sentiment = json.loads(response.text)

        except:
            print ("In exception..")
            f.close()
            break

if(not f.closed):
    f.close()
print (counter)
