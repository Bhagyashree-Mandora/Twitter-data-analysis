import json

# Parse the JSON sentiment responses and extract the sentiment label in a separate file
lines = [line.rstrip('\n') for line in open('responses')]
f= open("sentiments","w+")

for line in lines:
    sentiment = json.loads(line)
    f.write(sentiment['label']+"\n")

f.close()