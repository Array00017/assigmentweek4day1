#Exercise 1
#Write a function that takes in a tweet and returns a list of the hashtags in the tweet
#Ex. 1
#tweet = "Python is the best #Python #Programming #CodingTemple"
#Expected Output: ["#Python", "#Programming", "#CodingTemple"]

#Ex. 2
#tweet = "I love my life! #blessed"
#Expected Output: ["#bleesed"]

#Ex. 3
#tweet = "Bear Down"
#Expected Output: []

def returninghash(list1):
  list2 = []
  for x in list1
  if x in list1 == # + "."
  return x + ".".append(list2)


#Exercise 2
#Develop a regular expression to validate a username. The username should start with a letter, followed by any combination of letters, numbers, underscores, and dots. It should be between 3 and 16 characters long
#Ex. 1
#username = "CodingTemple123"
#Expected Output: True

#Ex. 2
#username = "1love"
#Expected Output: False

#Ex. 3
#username = "CT"
#Expected Output: False

#Ex. 4
#username = "This_is_a_username_that_I_would_like_to_use"
#Expected Output: False

#Ex. 5
#username = "brian_ct123"
#Expected Output: True

def validate(username):
  letters = "abcdefghijklmnopqrstuvwyz"
  nums = 123456789
  for x in username:
    if username == letters + nums or username.includes("." and "_") and < char(16) and > char(3):
      return true
    else
      return false


#Exercise 3
#Using the Python open() function, read in the example.txt file (attached in Google Classroom, make sure it is in the same folder as this notebook). Create a pattern that will find all of the dates in the text. Dates are in the format of YYYY-MM-DD. The pattern should have groups for year, month, and day. Using the .finditer() method, iterate over the dates and print in format of month/day/year

#Output:

#05/15/1990
#09/20/2015
#12/03/1985
#06/18/2010
#11/30/2002
#08/10/1978
#04/25/1992
#07/07/2019
#02/12/1980
#03/22/2005
    
text = Daniel Martinez was born on 1990-05-15. He later married Elizabeth Anderson on 2015-09-20.

Alice Johnson's birthdate is 1985-12-03, and she got her degree on 2010-06-18.

Michael Brown's graduation date is 2002-11-30. He celebrated his birthday on 1978-08-10.

Emily Wilson was born on 1992-04-25. She completed her Ph.D. on 2019-07-07.

Sarah Clark's birthdate is 1980-02-12. She joined the company on 2005-03-22.


import re

print (text re.finditer([0-9,{,4}][0-9{2}][0-9{2}])))
print (text re.findall([0-9][0-9][0-9]))

