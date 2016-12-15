#!/usr/bin/env python
# encoding: utf-8

print("hello world")

def position(a,b):
    return (a,b)

life = {position(5,5):1,position(5,6):1,position(4,5):1,position(5,4):1,position(6,6):1}
keep = {}
keep = life.copy()
keeplife = {}
time = 0
maxlife = 0
def evolute(a,b,keep):
    if(position(a,b) in keep):
        keep[position(a,b)]+=1
    else:
        keep[position(a,b)]=0.5

def radiation(theposition,keep):
    evolute(theposition[0]-1,theposition[1]-1,keep)
    evolute(theposition[0],theposition[1]-1,keep)
    evolute(theposition[0]+1,theposition[1]-1,keep)
    evolute(theposition[0]-1,theposition[1],keep)
    evolute(theposition[0]+1,theposition[1],keep)
    evolute(theposition[0]-1,theposition[1]+1,keep)
    evolute(theposition[0],theposition[1]+1,keep)
    evolute(theposition[0]+1,theposition[1]+1,keep)

#for 1:200:


while(time < 9000):
    #繁殖开始
    for i in life:
        radiation(i,keep)

    #繁殖结果
    for i in keep:
        if(keep[i]==2.5 or keep[i]==3 or keep[i]==4):
            keeplife[i] = 1
    time+=1
    life = keeplife
    keep = life.copy()
    keeplife = {}


#print(life)

#print(keep)
#print(keeplife)
    if len(life) > maxlife :
        print time
        print(len(life))
        print("\n")
        maxlife = len(life)





