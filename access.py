import csv
from googleapiclient.discovery import build
import pandas as pd
import time
DEVELOPER_KEY = "AIzaSyBMArI3aNxrkyXfqZjsmVUhW1O_2Np2HH0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
service = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

def get_video_comments(service, **kwargs):
	comments = []
	results = service.commentThreads().list(**kwargs).execute()
	while results:
		for item in results['items']:
			comment1 = item["snippet"]["topLevelComment"]
			comment=dict(nbrReplies = item["snippet"]["totalReplyCount"],
			author = comment1["snippet"]["authorDisplayName"],
			likes = comment1["snippet"]["likeCount"],
			publishedAt=comment1["snippet"]["publishedAt"],
			text = comment1['snippet']['textDisplay'].encode('utf-8').strip())

			comments.append(comment)

		# Check if another page exists
		if 'nextPageToken' in results:
			kwargs['pageToken'] = results['nextPageToken']
			results = service.commentThreads().list(**kwargs).execute()
		else:
			break

	return comments


def write_to_csv(comments):
	with open('comments.csv', 'w', encoding="utf-8" ) as comments_file:
		comments_writer = csv.writer(comments_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		comments_writer.writerow(['Video ID', 'Title', 'nbrReplies','author','likes','publishedAt','text'])
	for row in comments:
# convert the tuple to a list and write to the output file
		comments_writer.writerow(list(row))


def get_videos(service, **kwargs):
	final_results = []
	results = service.search().list(**kwargs).execute()
	i = 0
	max_pages = 1
	while results and i < max_pages:
		final_results.extend(results['items'])

# Check if another page exists
		if 'nextPageToken' in results:
			kwargs['pageToken'] = results['nextPageToken']
			results = service.search().list(**kwargs).execute()
			i += 1
		else:
			break

	return final_results


def search_videos_by_keyword(service, **kwargs):
	results = get_videos(service, **kwargs)
#	return results
	final_result = []
	for item in results:
		title = item['snippet']['title']
		video_id = item['id']['videoId']
		comments = get_video_comments(service, part='snippet', videoId=video_id, textFormat='plainText')
# make a tuple consisting of the video id, title, comment and add the result to
# the final list
		final_result.extend([(video_id, title, comment) for comment in comments])
	fp=open('comments.txt','a')
	fp.write(str(final_result))
	fp.close()
	final_result
	return final_result
#write_to_csv(final_result)



keyword = input('Enter a keyword: ')
res=search_videos_by_keyword(service, q=keyword, part='id,snippet', eventType='completed', type='video')
fp=open('output.txt','a')
fp.write(str(res))
fp.close()
print res

