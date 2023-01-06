import random

dict={2:[2,4],3:[3,4],4:[4,4],5:[5,4],6:[6,4],7:[7,4],8:[8,4],9:[9,4],10:[10,4],'as':[11,4],'j':[10,4],'q':[10,4],'k':[10,4]}
def getcard():
    while 1:
        card=random.choice(list(dict.items()))
        if card[1][1]!=0:
            dict.update({card[0]:[card[1][0],card[1][1]-1]})
            return card
def endgame(usercards,dealercards):
    if dealerpts>userpts:
        print(f"you lost!, your deck={usercards} dealer's deck={dealercards}")
    elif dealerpts<userpts:
        print(f"you win!, your deck={usercards} dealer's deck={dealercards}")
    elif dealerpts==userpts:
        print(f"draw!, your deck={usercards} dealer's deck={dealercards}")

def drawcard(usercards,dealercards,userpts,dealerpts,userkey,dealerkey):
    userstatus=False
    dealerstatus=False
    if userkey==True:
        card=getcard()
        usercards.append(card[0])
        userpts+=card[1][0]
        if userpts-10*(usercards.count('as'))>21:
            print(usercards)
            userstatus=True

    while dealerkey==True and dealerpts<17 and dealerstatus==False:
        card=getcard()
        dealercards.append(card[0])
        dealerpts+=(card[1][0])
        if dealerpts-10*(dealercards.count('as'))>21:
            dealerstatus=True
    return userstatus,dealerstatus,userpts,dealerpts
dealerpts=0
userpts=0
dealercards=[]
usercards=[]
for i in range(4):
    card=getcard()
    if i<2:
        dealerpts+=card[1][0]
        dealercards.append(card[0])
    else:
        userpts+=card[1][0]
        usercards.append(card[0])
print(f"you got {userpts} with {usercards[0]} and {usercards[1]}, dealer has {dealercards[0]} as his first card write down you choice: [go],[stop]")
while 1:
    choice=input()
    if choice.lower()=='go':
        result=drawcard(usercards,dealercards,userpts,dealerpts,userkey=True,dealerkey=False)
        userpts=result[2]
        dealerpts=result[3]
        if result[0]==True or dealerpts==21:
            print(f"you lost!, your deck={usercards} dealer's deck={dealercards}")
        elif result[1]==True or userpts==21:
            print(f"you win against dealer!, your deck={usercards} dealer's deck={dealercards}")
        else:
            print(f"game continues with your deck={usercards}...")

    elif choice.lower()=='stop':
        result=drawcard(usercards,dealercards,userpts,dealerpts,userkey=False,dealerkey=True)
        endgame(usercards,dealercards)
        break
    else:
        print('incorrect input try again')
