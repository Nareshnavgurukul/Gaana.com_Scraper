import requests,webbrowser
from bs4 import BeautifulSoup
P = "https://gaana.com/playlist/gaana-dj-punjabi-top-50-1"
B = "https://gaana.com/playlist/gaana-dj-bollywood-top-50-1"
In = "https://gaana.com/playlist/gaana-dj-gaana-international-top-50"
print("Here are the list of songs type")
print("1. Bollywood Top 50")
print("2. Pubjabi Top 50")
print("3. International Top 50")
userinput = int(input("Just enter the rank of your type:-"))

storage = []
def songs(url):
	html = requests.get(url)
	soup = BeautifulSoup(html.text,"html.parser")
	divlist = soup.findAll("div",class_="playlist-data") 
	rank = 0
	for i in divlist:
		Art = []
		Play = {}
		Art.append(i.find("div",class_="mobile").get_text())	
		rank+=1
		Play["Postion"] = rank 
		Play["Song"] = i.find("a").text
		Play["SongUrl"] = i.find("a")["href"]
		Play["Artists"] = Art
		Play["Type"] = url[42:-7]
		storage.append(Play)

	userAlpha = input("Enter the starting alphabet of your song_ _ _ _. ").upper()#C
	pos = 0
	choice  = {}
	for i in storage:
		if userAlpha == i["Song"][0]:
			pos+=1
			if pos>=1:
				print(pos,i["Song"])
				choice [pos] = i["SongUrl"]
	if pos>=1:
		demand = int(input("Enter your choice :_ _ _ "))
		Playthis = choice [demand]
		webbrowser.open_new_tab(Playthis)
	else:
		print("There is no song starting with",userAlpha)

if userinput == 1:
	songs(B)
if userinput == 2:
	songs(P)
if userinput == 3:
	songs(In)



