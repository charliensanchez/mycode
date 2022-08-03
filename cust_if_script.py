#!/usr/bin/env python3

count = 0

print("How big of a Taylor Swift fan are you? Play this quiz to find out")
print("Let's begin")

grammys = str(input("How many grammys has Taylor won?: "))
middlename = input("What is her middle name?: ")
longsong = input("What is the name of her album that is based on a color?: ")
biggesthit = input("What is her best selling song called?: ")
cats = str(input("What number of cats does she own?: "))
year = str(input("What year was Taylor Swift born?: "))
songname = input("What song of hers is named after a country music star?: ")

if(grammys == "10"):
    count+=1
   
if(middlename.lower() == "alison"):
    count+=1
           
if(longsong.lower() == "red"):
    count+=1

if(biggesthit.lower() == "shake it off"):
    count+=1

if(cats == "3"):
    count+=1

if(year == "1989"):
    count+=1

if(songname.lower() == "tim mcgraw"):
    count+=1

print(("You got "+str(count)+" out of 7 correct"))

if(count == 7):
    print("Congratulations, you are a militant Swiftie!")
elif(count>=5 and count<7):
    print("You are a lowkey Swiftie")
elif(count>=3 and  count<5):
    print("Your best friend is probably an annoying Swiftie")
else:
    print("You my friend, don't even listen to Taylor Swift")

