import urllib
import simplejson


def extract_hash_tags(s):
	return set(part[1:] for part in s.split() if part.startswith('#'))

def searchTweets(query):
 search = urllib.urlopen("http://search.twitter.com/search.json?q="+query)
 dict = simplejson.loads(search.read())
 for result in dict["results"]: 
 # result is a list of dictionaries
 	print result['from_user_name'].encode('utf-8'),"\n"
 	print "*",result["text"].encode('utf-8'),"\n"
 	print result["text"].encode('utf-8').split('#')
 	r = extract_hash_tags(result["text"].encode('utf-8'))
 	for i in r :
 		print i


searchTweets("apple%20stockvalue")


