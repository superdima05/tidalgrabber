#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import tidalapi
from transliterate import translit
import os
from mutagen.flac import Picture, FLAC
from requests import get

session = tidalapi.Session(tidalapi.Config('LOSSLESS'))
session._config.api_token='BI218mwp9ERZ3PFI'
session.login('YOUR TIDAL LOGIN', 'YOUR TIDAL PASSWORD')

def start():

	if not os.path.exists("music/"):
		os.mkdir("music/")

	mode = raw_input("Mode: \n 1) Playlist grabber\n 2) Track grabber\n 3) Album grabber\n 4) Search \n")

	if int(mode) == 1:
		playlist_id = raw_input("Enter playlist id: ")
		try:
			playlist = session.get_playlist_tracks(playlist_id=playlist_id)
			can_download = 1
		except Exception:
			print("Playlist not found.")
			can_download = 0
		if can_download == 1:
			for track in playlist:
				download_flac(track)
		want_start()
	elif int(mode) == 2:
		track_id = input("Enter track id: ")
		try:
			track = session._map_request('tracks/'+str(track_id), params={'limit': 100}, ret='tracks')
			can_download = 1
		except Exception: 
			print("Track not found.")
			can_download = 0
		if can_download == 1:
			download_flac(track)
		want_start()
	elif int(mode) == 3:
		album_id = input("Enter album id: ")
		try:
			album = session.get_album_tracks(album_id=album_id)
			can_download = 1
		except Exception:
			print("Album not found")
			can_download = 0
		if can_download == 1:
			for track in album:
				download_flac(track)
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

def download_flac(track):
	url = session.get_media_url(track_id=track.id)
	name_tag = translit(""+track.name, "ru", reversed=True).encode("UTF-8")
	name = translit(""+track.name, "ru", reversed=True).encode("UTF-8").replace("?", "").replace("(", "").replace(")", "").replace("<", "").replace(">", "").replace(":", "").replace("/", "").replace("|", "").replace('"', "").replace("*", "")
	artist_name = translit(u""+track.artist.name, "ru", reversed=True).encode("UTF-8")
	album_name = translit(u""+track.album.name, "ru", reversed=True).encode("UTF-8")
	releaseDate = str(track.album.release_date)
	print(name+' - '+url)
	album_artist = translit(u""+track.album.artist.name, "ru", reversed=True).encode("UTF-8")
	try:
		if ".m4a" not in url:
			download(url, "music/"+name+".flac")
	except Exception:
		flac = 0
	try:
		if ".m4a" not in url:
			download(track.album.image, 'music/'+name+'.png')
	except Exception:
		flac = 0
	if os.path.exists("music/"+name+".flac"):
		flac = 1
	if not os.path.exists("music/"+name+".flac"):
		flac = 0
	if ".flac" not in url:
		flac = 0
	if ".flac" in url:
		flac = 1
	if flac == 1:
		audio = FLAC("music/"+name+".flac")
		albumart = "music/"+name+".png"
		image = Picture()
		image.type = 3
		mime = 'image/png'
		image.desc = 'front cover'
		with open(albumart, 'rb') as f:
			image.data = f.read()
		audio['artist'] = artist_name
		audio['title'] = name_tag
		audio['album'] = album_name
		audio['date'] = releaseDate
		audio.add_picture(image)
		audio.save()
		os.remove("music/"+name+".png")
	elif flac == 0:
		print(name+" isn't in flac or can't be downloaded in this country.")
	else:
		print("Unknown error.")

def download(url, file_name):
	with open(file_name, "wb") as file:
		response = get(url) 											
		file.write(response.content)

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
