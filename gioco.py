from sys import exit
from random import randint
import time

def tempo():
	global tris
	tris = tfi-tin
	print(str(tris))
	if tris < 60:
		tris = str(round(tris, 0)) + " secondi"
	else:
		nm = tris/60
		ns = tris%60
		tris = str(nm) + " minuti e " + str(ns) + " secondi"

ntent = 1
npg = 0
neg = 0
elg = []
ind = "no"
info = ""
cs1 = randint(0,9)
cs2 = randint(0,9)
cs3 = randint(0,9)
elg.append(cs1)
elg.append(cs2)
elg.append(cs3)
sol = str(cs1) + str(cs2) + str(cs3)
tin = time.time()

while ind == "no":
	print("\n\n\n\n\n\n" + info + "\n\n\n\n\n\n\n\n")
	nin = input("Tentativo " + str(ntent) + "> ")
	ni1 = int(nin[0])
	ni2 = int(nin[1])
	ni3 = int(nin[2])

	if nin == sol:
		ind = "si"
		tfi = time.time()
		tris = tfi-tin
		tempo()
		print("\n\n\nCorretto!\n\nTentativi: " + str(ntent) + "\nTempo: " + str(tris) + "\n\n\n")
	else:
		if ni1 in elg:
			if ni1 == elg[0]:
				npg = npg+1
			else:
				neg = neg+1
		if ni2 in elg:
			if ni2 == elg[1]:
				npg = npg+1
			else:
				neg = neg+1
		if ni3 in elg:
			if ni3 == elg[2]:
				npg = npg+1
			else:
				neg = neg+1
		if npg > 0:
			info = str(npg) + " numeri sono nella posizione corretta"
		elif neg > 0:
			info = str(neg) + " numeri sono corretti ma nella posizione sbagliata"
		neg = 0
		npg = 0
		ntent = ntent+1
			
exit()
