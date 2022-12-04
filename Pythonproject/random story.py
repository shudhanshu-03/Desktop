import random

when = ["A few year ago", "Last night", "A long time ago", "On 29th Jam"]
who = ["a rabbit", "an elephant", "a mouse", "a turtle", "a cat"]
name = ["Jack", "Monty", "Jojo", "Pam"]
residence = ["India", "Germany", "England", "Venice"]
went = ["cinema", "university", "seminar", "school", "laundry"]
happend = ["made a lot of friend", "Eats a burger", "found a secret key", "participates in dance"]


randomwhen = random.choice(when)
randomwho = random.choice(who)
randomname = random.choice(name)
randomresidence = random.choice(residence)
randomwent = random.choice(went)
randomhappend = random.choice(happend)

print(randomwhen + ", " + randomwho + " called " + randomname + " that lived in " + " went to the " + randomwent + " and " + randomhappend + ".")