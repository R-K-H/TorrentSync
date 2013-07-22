import urllib.request
import re 
import os 
import msvcrt
import json
import math
# import libtorrent

#get a count of all the movies that we want
response = urllib.request.urlopen('http://yify-torrents.com/api/list.json?quality=1080p&rating=6.5')
encoding = response.headers.get_content_charset()
data = response.readall().decode("utf-8")
moviecount = json.loads(data)
moviecount = moviecount["MovieCount"]
print (moviecount)

#this makes the api call for yifitorrents to return our requested data
print ("How many movies per request(10-50)?") #pick page size )should just set this at the highest possible
numberofmovies = input()

numberofpages = math.ceil(int(moviecount) / int(numberofmovies)) #determine the number of pages to run through
print(numberofpages)

#begin our run through our pages
set = 1
while set < numberofpages:
	response = urllib.request.urlopen('http://yify-torrents.com/api/list.json?limit='+ str(numberofmovies) +'&quality=1080p&set='+ str(set) +'&sort=rating&rating=6.5')
	encoding = response.headers.get_content_charset()
	data = response.readall().decode("utf-8")
	movies = json.loads(data)

	#starts moving through each movie and adding torrents if they haven't been found in the folder
	numbermovie = 0
	for movie in movies["MovieList"]:
		moviename = movie["MovieTitle"]
		moviename = str.replace(' (1994) 1080p ', '', moviename)
		print (moviename)
		for filename in os.listdir('D:\Movies'):
			filename = str.replace(' (HD)]', "", filename)
			if re.search(moviename, filename):
				foundmovie = True;
			else:
				foundmovie = False;
		if not foundmovie:
			print ("Download " + moviename + "?")
			if ord(msvcrt.getch()) == 121:
				download = '"' + movie["TorrentMagnetUrl"] + '"'
				#html = urllib.request.urlopen(download).readall()
				#os.system("uTorrent " + download)
				os.startfile(download)
				numbermovie += 1
			else:
				print (ord(msvcrt.getch()))
	set += 1