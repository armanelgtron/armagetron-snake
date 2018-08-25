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
import random
while True:
	line = input('')
	split = line.split(" ")
	if split[0] == "NEW_ROUND":
		length = -5 #start at -5, add 5 in spawn zone to make 0
		split[0] == "TARGETZONE_PLAYER_ENTER"
	if split[0] == "OBJECTZONE_PLAYER_ENTERED" or split[0] == "TARGETZONE_PLAYER_ENTER":
		length += 5
		print("CYCLE_WALLS_LENGTH "+str(length))
		print("DESTROY_ALL\nSPAWN_OBJECTZONE "+str(random.randint(5,495))+" "+str(random.randint(5,495))+" 30 0 0 0 false 0 15 0")
		#print("COLLAPSE_ZONE\nSPAWN_ZONE target "+str(random.randint(5,495))+" "+str(random.randint(5,495))+" 100 0")
