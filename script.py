#!/usr/bin/python3
"""
Simple armagetron snake script, MIT licensed

Copyright 2018 Glen Harpring

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
## A few notes for usage (hopefully your text editor wraps!): 
## Objectzones are more reliable than targetzones, but is a +ap only feature (at the time of this writing). To use targetzones instead, just comment out the SPAWN_OBJECTZONE line and uncomment the SPAWN_ZONE target line. I've also combined DESTROY_ALL vs COLLAPSE_ZONE to the line so you don't get confused on what to comment and what to uncomment :)
# user config
listladder = True #set this to True to list the contents of the ladder
ladderfile = "/home/armagetron/servers/snake/var/highscores.txt" #location of highscores.txt
# end user config
import random
def newzone(pre=''):
	return "DESTROY_ALL\n"+pre+"SPAWN_OBJECTZONE "+str(random.randint(5,495))+" "+str(random.randint(5,495))+" 30 0 0 0 false 0 15 0"
	#return "COLLAPSE_ZONE\nSPAWN_ZONE target "+str(random.randint(5,495))+" "+str(random.randint(5,495))+" 30 0"
while True:
	line = input('')
	split = line.split(" ")
	if split[0] == "NEW_ROUND":
		length = 0
		print(newzone("DELAY_COMMAND 0 "))
		if listladder:
			try:
				i = 0;string = "0x00ff00Top 3 players 0x808080WIP:"
				with open(ladderfile) as f:
					for line in f:
						i += 1
						splice = " ".join(line.split()).split(" ")
						string += "\\n0x808080#0xRESETT "+str(i)+" 0x808080#0xRESETT "+splice[1]+" 0x808080#0xRESETT "+str(int(splice[0])*5)+" 0x808080#0xRESETT"
						if i >= 3: break;
				print("CONSOLE_MESSAGE "+string)
			except FileNotFoundError:
				print("CONSOLE_MESSAGE 0xff0000Warning: 0xffff7fLadder file not found!")
	if split[0] == "OBJECTZONE_PLAYER_ENTERED" or split[0] == "TARGETZONE_PLAYER_ENTER":
		length += 5
		try: p = split[5]
		except: p = '0'
		print("ADD_SCORE_PLAYER "+p+" 1\nCYCLE_WALLS_LENGTH "+str(length)+"\n"+newzone())
