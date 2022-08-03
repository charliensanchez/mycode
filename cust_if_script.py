#!/usr/bin/env python3

#Beyonce Quiz

#Tallies up score by using a count variable that is set to zero
count = 0


#Welcome messages
print("How big of a Beyonce fan are you? Play this quiz to find out")
print("Let's begin")

#-------------------------------------------------------------------------------------------

#Quiz questions with their answers saved to a variable

grammys = (input("How many grammys has Beyonce  won?: ")
middlename = input("What is Beyonce's middle name?: ")
sign = input("What is Beyonce's astrological sign?: ")
album = input("What is Beyonce's first album called?: ")
kids = (input("How many kids does Beyonce have?: ")
year = (input("What year was Beyonce  born?: ")
artist = input("Who is featured on Beyonce's 2007 hit 'Beautiful Liar?': ")

#Conditionals that check for if the answer is correct or not.
#If correct, we will increment count by one

if(grammys == "28" or grammys == "twenty eight" or grammys == "twenty-eight"):
    count+=1
   
if(middlename.lower() == "giselle"):
    count+=1
           
if(sign.lower() == "virgo"):
    count+=1

if(album.lower() == "dangerously in love"):
    count+=1

if(kids == "3" or kids == "three"):
    count+=1

if(year == "1981"):
    count+=1

if(artist.lower() == "shakira"):
    count+=1

#Prints Results of Quiz
print(("You got "+str(count)+" out of 7 correct"))

#Logic for what level of a Beyonce fan you are
if(count == 7):
    print("Congratulations, you are a militant Beyhive member!")
elif(count>=5):
    print("You are a lowkey Beyhive supporter")
elif(count>=3):
    print("Your best friend probably won't shut up about Beyonce which is how you know certain things.")
else:
    print("You my friend, live under a rock.")

#Goodbye message!
print("Thanks for playing. Stream Renaissance!")
