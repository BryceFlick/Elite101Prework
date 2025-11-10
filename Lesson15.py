from nrclex import NRCLex
##Feel freed to add your own tweets to the list
# Two of the tweets were modified to help with accuracy. but you can use the original ones from the bottom of the program.

#individual tweet posts
tweet1 ="I know I was not the only one hoping to love the Pixel Watch when it finally got announced, but turns out it is a bit of a clumsy first gen fumble. I would recommend waiting for the second generation."

tweet2 = "This $43 Razor Wannabe Is the Best Deal You will Find for a Non-electric Scooter. I did not feel like paying $80 for a Razor scooter for my 13 years old. So I tried this Uenjoy one instead and it turned out to be an excellent value."

tweet3 ="The Apple iPhone 14 Pro Max is the best iPhone overall, with excellent performance, stellar battery life, sharp cameras, and a number of useful features you don't get with the standard models."

tweet4 = "The Moto E is a very price concious phone. I didn't know if I would like it at first but when I use it in daily life I realize how much I truely love it. It really is a great phone."
#add the tweets to a list
tweetList=[tweet1,tweet2,tweet3,tweet4]

#convert the tweets to a string and function return
def tweets():
  tweets = " ".join(tweetList)
  return tweets

tweet_emotion = NRCLex(tweets())


'''if tweet_emotion.raw_emotion_scores == "positive":
  print("Positive")
  countpos += 1
else:
  print("Negative")
  countneg += 1
  '''


### ORIGINAL TWEETS
"""Tweet 1 from Marques Brownlee / @MKBHD
NEW VIDEO - I know I wasn't the only one hoping to love the Pixel Watch when it finally got announced, but turns out it's a bit of a clumsy first gen fumble. I'd recommend waiting for the second gen. My full review: https://youtu.be/-OpUg0GDrII
"""

"""
Tweet 2 from reviews and Cnet / @reviews and @CNET
Tech News> This $43 Razor Wannabe Is the Best Deal You'll Find for a Nonelectric Scooter - CNET: I didn't feel like paying $80 for a Razor scooter for my 13-year-old. So I tried this Uenjoy one instead and it turned out to be an excellent value.
"""

"""
Tweet 3 from PCMag / @PCMag
The Apple iPhone 14 Pro Max is the best iPhone overall, with excellent performance, stellar battery life, sharp cameras, and a number of useful features you don't get with the standard models.
"""