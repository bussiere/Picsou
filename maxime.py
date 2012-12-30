import urllib
import simplejson


def searchTweets(query):
 search = urllib.urlopen("http://search.twitter.com/search.json?q="+query)
 dict = simplejson.loads(search.read())
 for result in dict["results"]: 
 # result is a list of dictionaries
 	print result['from_user_name'].encode('utf-8'),"\n"
 	print "*",result["text"].encode('utf-8'),"\n"


searchTweets("#apple")


