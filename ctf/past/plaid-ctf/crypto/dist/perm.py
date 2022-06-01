#!/usr/bin/python3
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import isPrime
from sympy import factorint
from z3 import *
from sage import *
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)
z=16158503035655503426113161923582139215996816729841729510388257123879913978158886398099119284865182008994209960822918533986492024494600106348146394391522057566608094710459034761239411826561975763233251722937911293380163746384471886598967490683174505277425790076708816190844068727460135370229854070720638780344789626637927699732624476246512446229279134683464388038627051524453190148083707025054101132463059634405171130015990728153311556498299145863647112326468089494225289395728401221863674961839497514512905495012562702779156196970731085339939466059770413224786385677222902726546438487688076765303358036256878804074494
lest=[]
def permute(x,y):
	if(y==len(x)):
		lest.append(int(x,2))
		return
	if(x[y]=='0'):
		permute(x,y+1)
	else:
		permute(x,y+1)
		temp=x[0:y]+'0'+x[y+1:]
		permute(temp,y+1)
b_dict = {'0': '1', '1': '0'}
y=bin(z)
y=str(y)[2:]
inverse_s = ''
for i in y:
    inverse_s += b_dict[i]
permute(inverse_s,0)
with open('listfile.txt','w') as f:
	for listitem in lest:
		f.write('%s\n' % listitem)

