gifts = ["","a Partridge in a Pear Tree","two Turtle Doves","three French Hens","four Calling Birds","five Gold Rings",
"six Geese-a-Laying","seven Swans-a-Swimming","eight Maids-a-Milking","nine Ladies Dancing","ten Lords-a-Leaping",
"eleven Pipers Piping","twelve Drummers Drumming"]

days = ["","first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"]
def recite(start_verse, end_verse):
	song = []
	for b in range(start_verse, end_verse+1):
		verseGifts = []
		for c in range(b,0,-1):
			if c == 1 and b != 1:
				verseGifts.append("and %s" % (gifts[c]))
			else:
				verseGifts.append(gifts[c])
    		
		song.append("On the %s day of Christmas my true love gave to me: %s." % (days[b],", ".join(verseGifts)))
    
	return song