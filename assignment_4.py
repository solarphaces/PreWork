words=['bob', 'jimmy', 'max b', 'bernie', 'jordan', 'future hendrix']
big_name = sorted(words, key=len)

print ("The longest word in the list is: %s." % (big_name[-1],))