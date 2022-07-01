from Crypto.Util.number import *

N1 = 18266349196400324728796632198426724065863341515460128017379722167088811564142208540762217975696666190887534687486334974478770458134458646785682182438231047535912495200486295399237083743354006572775979196273345894016812147421648391560534928953791045301656072851030393661346227010573392017192092871743599780733618974144278058844414678104713310777338685821340236864598500469843212331330335171804328016140678014295178395686821469446312308097781506852568269309368807576215036130913554259546509277614896420588483929704110258122427731934119749960465772609969329231395097168664992720797902433454838999670183197496533599372453
e1 = 65537
ct1 = 6873813036805706192019236826822502457972771100457517090756917047060847774848540323350759250580238758998913544271128101335276213320240302206398066922772200444602226203653559017733029810367927075606003863202964202725297461799495530697341270915140044964898303984854574497628349362668695378519684693264593494716972185326436905495762497116849607924837994943127697112124217181161062684698865533001086211217060178202980704668203486578672364578669469712587269077695001297138207491663356223994825422557742042083843727850238507161657755737436196961552942941154267260840237025593539923533367161391402240798650010287812581011106

N2 = 24659767524526013018768938973883991511377669248630968999008468264428208747461052247749924232027616129566843290411914770222062361142014390330463814302544910044772535448949923181736285951382305617780092296934319600643083108399436503551987425616568398265868184384255524744326852580109993750455923648308457300741311644056806840080239266629430170801800674692923486070263947659308964150022391540089059138911526148899685247042835949241530880572488161927637699425020944697998483747469309576045917038431425710502056969197916002745593176785614139365197372746789456581367558816039809574657471032143676431357391125588624599050493
e2 = 65537
ct2 =  11715772208083492702167997175167454009301340692399196360593824415816062365292031273728996255749695189978948242292097965040268601546052250584302206331424224398934005270192769085862845465718216946900897219973683677713043297722976307588263004621450861659350169718646844558379707749844428304916965303036455448719228506667752535085465025614399994834368259311922477097878143154258042140694172977284700008301528490157090476538427961683829505682126281348126157784828204887638985638647829395157101409725453166939388563809584382420835218557337222313577592617066209235421605768519128885685600282422644017925260843832358253267634

p1 = GCD(N1,N2)
q1 = N1 // p1

assert p1 != 1

p2 = p1
q2 = N2 // p2

d1 = inverse(e1,(p1-1)*(q1-1))
d2 = inverse(e2,(p2-1)*(q2-1))

pt1 = long_to_bytes(pow(ct1,d1,N1))
pt2 = long_to_bytes(pow(ct2,d2,N2))

print(pt1,pt2)


''' accessdenied{r3us31ng_5tuff_1s_n0t_f0r_crypt0gr4phy_69c36434}' '''