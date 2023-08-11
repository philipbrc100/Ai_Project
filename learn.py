#youtuber = ""

#print ("subscribe to" + youtuber)
#print (f"subscribe to {youtuber}")
#print ("subscribe to {}".format(youtuber))


from sample_madlibs import hp, code, zombie, hungergames
import random


if __name__=="_main_":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()