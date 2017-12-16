#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Python script to like all pictures of any given user.
Thus script uses instagram_private_api as Instagram API wrapper
Available at https://github.com/ping/instagram_private_api
"""

from instagram_private_api import Client, ClientCompatPatch
from time import sleep
import getpass


def get_user_medias(user_id):
    fetched_medias = []
    next_max_id = ''

    for i in range(0, 50):
        user = api.username_feed(user_id, max_id=next_max_id)
        fetched_medias.extend(user['items'])
        if 'next_max_id' in user:
            next_max_id = user['next_max_id']
        else:
            break

    return fetched_medias


def get_media_ids(media_list):
    return [i['pk'] for i in media_list]


def like_by_media_ids(media_list, sleep_time=2):
    if not len(media_list):
        raise ValueError('Please provide valid media list')

    for index, media_id in enumerate(media_list):
        response = api.post_like(media_id)
        post = target_user_medias[index]
        print ('Liking Post No -> {}'.format(index + 1))
        try:
            caption_text = (post['caption']['text'])
            print ('Caption:  {} \n'.format(caption_text))
        except:
            print('Caption not available')

        print (' Like Status -> {}'.format(response['status']))
        print ('--' * 20)
        sleep(sleep_time)

    return 'Done!'


if __name__ == "__main__":
    user_name = raw_input('Enter your Instagram Username : ')
    password = getpass.getpass('Enter your Instagram Password : ')
    print ('Please wait while logging in....')
    api = Client(user_name, password)
    if not api:
        print('Sorry! Some error, try later!')

    print ('Welcome! {}'.format(api.current_user()['user']['full_name']))

    target_user_name = raw_input('Please enter the user you want to like pictures of : ')
    target_user_medias = get_user_medias(target_user_name)
    target_user_media_ids = get_media_ids(target_user_medias)
    print ('Starting to 😍😍😍 like {} pictures of {}'.format(len(target_user_media_ids), target_user_name))
    like_by_media_ids(target_user_media_ids)

