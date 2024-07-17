key = "Roads? Where We're Going, We Don't Need Roads."
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()"
message = "ftmpH.:lemGubTDmMb'YtfsublbnkKlMmOoKywmmOIpa.,3mNeEbl?(bVtkUy?xtoNtCkAg:;n)OlInqp2rjap6JwiG)9H'jHm: pjok'9njQbtOxusdql'b'VtkrBb5j!aMWGieIjOHfrw,j,ubsbm,xrufoKljGdob8q,APzqI:0fpi:.Jsipk6lueD):!wrwbd?j(LbmODCCz7:vjbANCsqp2ts);Of,?p; lulx,tXGbLmbTflKBbYlCCdle1bnYtGrCl1bnw:PrphBeYFviLoZD.7pb!)nrztr0lCvl8n'tqIHn8"
num_answer = []
answer = []
Final = ''
spaces = []
mletters = []
letters = []
x=-1
                        
for i in range(len(message)):
    if x>=(len(key)-1):
        x=0
    else:
        x+=1
    if message[i]==' ':
        spaces.append(i)
        
    for j in range(len(characters)):
        if key[x]==characters[j]:
            letters.append(j+1)
        if message[i] == characters[j]:
            mletters.append(j)


for i in range(len(mletters)):
    l = int(mletters[i])-int(letters[i])# + to encode message and - to decode message
    num_answer.insert(i,l)
for i in range(len(num_answer)):
    if num_answer[i]>(len(characters)):
        num_answer[i]-=len(characters)
    answer.append(characters[num_answer[i]])
#for i in spaces:
#    answer.insert(i,' ')
for i in answer:
    Final += i
print(Final)
