#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import tidalapi
from transliterate import translit
import os

session = tidalapi.Session(tidalapi.Config('LOSSLESS'))
session._config.api_token='BI218mwp9ERZ3PFI'
session.login('superdima05@gmail.com', 'Apple123$3')

def start():

	mode = raw_input("Mode: \n 1) Playlist grabber\n 2) Track grabber\n 3) Album grabber\n 4) Search \n")

	if int(mode) == 1:
		playlist_id = input("Enter playlist id: ")
		playlist = session.get_playlist_tracks(playlist_id=playlist_id)
		for track in playlist:
			url = session.get_media_url(track_id=track.id)
			name = translit(u""+track.name, "ru", reversed=True).encode("UTF-8")
			print(name+' - '+url)
			os.system('wget "'+url+'" -O "music/'+name+'.flac"'.encode('utf-8'))
		want_start()
	elif int(mode) == 2:
		track_id = input("Enter track id: ")
		track = session._map_request('tracks/'+str(track_id), params={'limit': 100}, ret='tracks')
		url = session.get_media_url(track_id=track.id)
                name = translit(u""+track.name, "ru", reversed=True).encode("UTF-8")
                print(name+' - '+url)
                os.system('wget "'+url+'" -O "music/'+name+'.flac"'.encode('utf-8'))
		want_start()
	elif int(mode) == 3:
                album_id = input("Enter album id: ")
		album = session.get_album_tracks(album_id=album_id)
		for track in album:
			url = session.get_media_url(track_id=track.id)
                        name = translit(u""+track.name, "ru", reversed=True).encode("UTF-8")
                        print(name+' - '+url)
                        os.system('wget "'+url+'" -O "music/'+name+'.flac"'.encode('utf-8'))
		want_start()
	elif int(mode) == 4:
		search_query = raw_input("Enter search query: ")
		search = session.search(field='track', value=search_query)
		for track in search.tracks:
			print(track.artist.name+" - "+track.name+": "+str(track.id))
		want_start()
	else:
		print("Incorrect mode!")
		start()

def want_start():
	want = raw_input("Do you want to continue [0/1]: ")
	if want == "1":
		start()
	elif want == "0":
		print("OK!")
	else:
		want_start()
start()
#playlist = session.get_playlist_tracks(playlist_id='004a984e-6f9e-44ed-a447-9c3dd4b0405f')
#for track in playlist:
#    url = session.get_media_url(track_id=track.id)
#    name = translit(u""+track.name, "ru", reversed=True).encode("UTF-8")
#    print(name+' - '+url)
#    os.system('wget "'+url+'" -O "music/'+name+'.flac"'.encode('utf-8'))
