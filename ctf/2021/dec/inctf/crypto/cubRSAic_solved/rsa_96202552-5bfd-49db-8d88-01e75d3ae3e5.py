from Crypto.Util.number import *
from flag import flag,x,p,q,r
n=p*q*r
a=1
b=193397088739638251960555612436875600986330023883750295571725584630414480365724395898270141722031329748156082442012506741700345490623652456944752641259299481648189663225789316735492124809430246787061623943122992972555612870003055978190998434876318194750716018238436902415663573233192086436098541111277008199813
c=8728831297832120843336404142494383487861941996882802023565995709954417891405655853020017387748976733140991007940950795977416209344692420808833741595065361790155014723446976903204381140455085622575477064605600925830092628718070785954578133863918237568921639276619726474929358824725452522548936820930316044199781907769975116642583087228056122086340804371487673925003430886366328940606581590239833871087344153426940165114190628567985514860529931412375128745713119805742019339702063634799522188535333496263711303227429950221230519245843532481700865129308471919982350847692475752700865209968245261953392636533410992980775
d=63070596256679484662413410207373928004736001790383956853307898306602698350449502470396308261161065806877977215076829311908943777778986616540253214462303167277670756699548339028092316959537033018041441628359647493347189674598031375658196799172454802634799166223829305392192521613748720703056322649928224065867121497675495400662468690132676998903424015988906876418063546949676385421158504886275413258353832927820154529362504173957845256741347439175151413191454309190779489182687927387632163531223048994443162863182633645603482086186470861356033199650558396270818562930850023584234133180617891209746554867462265585965013354965873061584035287994018488964953755160036085993213998304861556792215861795195160484204162254562357064980532222046820367893936950321067965117665776931
assert b*(x**2)+d == x**3 + c*x
flag=bytes_to_long(flag)
e=0x10001
ct=pow(flag,e,n)
f=open('out.txt','w')
f.write('n ='+ hex(n) +'\n')
f.write('e ='+hex(e)+'\n')
f.write('ct = '+hex(ct))