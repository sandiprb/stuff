from apiclient.discovery import build
DEVELOPER_KEY = "<DEVELOPER_KEY>"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)


def get_pagewise_channel_videos(channelId='UCBJycsmduvYEL83R_U4JriQ',\
          maxResults=50,part="id,snippet", token=None):
    
    search_response = youtube.search().list(
    pageToken=token,
    channelId=channelId,
    order="date",
    part=part, # Part signifies the different types of data you want 
    maxResults=maxResults).execute()
    
    return search_response
    


def get_all_channel_videos(channel_id='UCBJycsmduvYEL83R_U4JriQ'):
    
    total_respone = []
    token = None
    max_results=50
    part="id,snippet" # Part signifies the different types of data you want 
    
    for i in range(0,30):
        response = get_pagewise_channel_videos(
            channelId='UCBJycsmduvYEL83R_U4JriQ',
            token=token,
            part=part,
            maxResults=max_results,
        )
        total_respone.extend(response.get('items', []))
        if "nextPageToken" in response:
            token = response['nextPageToken']
        else:
            print ('Loop escaped after {} iters'.format(i))
            break
            
    return total_respone

def get_videoId_details(videoIds_list):
    result = []
    for video_id in videoIds_list:
        response = youtube.videos().list(
            part='statistics, snippet',
            id=video_id).execute()
        snippet = response['items'][0].get('snippet', '')
        stats = response['items'][0].get('statistics', '')
        print (snippet)
        
        formatted_response = {
            'title': snippet.get('title', ''),
            'publishedAt': snippet.get('publishedAt', ''),
            'description': snippet.get('description', ''),
            'tags': ','.join(snippet.get('tags', [])),
            'wasLive': snippet.get('publishedAt', ''),
            'likeCount': int(stats.get('likeCount',0)),
            'commentCount': int(stats.get('commentCount',0)),
            'viewCount': int(stats.get('viewCount',0)),
            'favoriteCount':int(stats.get('favoriteCount',0)),
            'dislikeCount': int(stats.get('dislikeCount',0)),
            
        }
        result.append(formatted_response)
        
    return result
