from random_word import RandomWords
import enchant
from termcolor import colored

def find_freq(W):
    #to find the frequency of letters in a given word
    fw={}
    for w in W:
        if w in fw.keys():
            fw[w]+=1
        else:
            fw[w]=1
    return fw
            
def init_freq(G):
    #initialize frequency values to 0
    fg={}
    for g in G:
        fg[g]=0;
    return fg

def wordle_check(W,fw,G):
    #check if the guess matches letters in the word
    fg=init_freq(G)
    C=[0,0,0,0,0]
    for i in range(0,5):
        g=G[i]
        if g not in fw.keys():
            continue
        elif fg[g]<fw[g]:
            if g==W[i]:
                C[i]=2
            else:
                C[i]=1
            fg[g]+=1
    return C

def print_color(G,C):
    #display the guess word in color
    CD={0:'grey',1:'yellow',2:'green'}
    GC=[]
    for i in range(0,5):
        GC.append(colored(G[i],CD[C[i]]))
    print(GC[0],GC[1],GC[2],GC[3],GC[4])

r=RandomWords()
d=enchant.Dict('en_US')

f=0;
while f==0:
    #generate random 5 letter English word
    W=r.get_random_word(hasDictionaryDef='true',minLength=5,maxLength=5)
    if W != None and '-' not in W:
        W=W.upper()
        if d.check(W):
            f=1
            fw=find_freq(W)
            
c=0
f=0
while c<6:
    prompt='Enter your guess ('+str(c+1)+'/6) : '
    G=input(prompt)
    if len(G)!=5 or (d.check(G)==False):
        print('Invalid')
    else:
            G=G.upper()
            C=wordle_check(W,fw,G)
            print_color(G,C)
            c+=1
            if sum(C)==10:
                print('Congrats: ',c,'/',6)
                f=1
                break
if f==0:
    print('Fail. The word is: ',W)