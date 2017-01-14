import time; import random;

name = input('Monster name: ')
try:
    maxhealth = eval(input('Input HP value: '))
except:
    maxhealth = 100

try:
    health = eval(input('Input HP value, less than previous: '))
    if health > maxhealth:#Makes it so that if health exceeds max use half of max
        health = maxhealth // 2
except:
    health = maxhealth#IF except just set health to max

try:
    ball = eval(input('What ball (1-8): '))
    if ball <= 0 or ball > 8:
        ball = 1
    ball = ball / 2
except:
    ball = 1 #if else make it a poke- I mean, the weakest type of capture device

try:
    capturerate = eval(input('Capture rate (1-50): '))
    if capturerate <= 0 or capturerate > 50:
        capturerate = 1
except:
    capturerate = 50

try:
    status = eval(input('Status deffect (1-3): '))
    if status <= 0 or status > 3:
        status = 1
except:
    status =1
    
capture = 0
HPpotential = (maxhealth / health) * 4
capturerate = capturerate // 1
attempts = 0#Tracks attempts to capture

while capture < 1:
    attempts += 1
    capture1 = random.randrange(0,256,1)
    capture2 = random.randrange(0,256,1)
    capture3 = random.randrange(0,256,1)
    print('You initiate a capture!')
    time.sleep(1)
    if (((HPpotential * capturerate)* ball)*status) > capture1:
        print("It's fighting!")
        time.sleep(1)
        if (((HPpotential * capturerate)* ball)*status) > capture2:
            print('Almost there!')
            time.sleep(1)
            if (((HPpotential * capturerate)* ball)*status) > capture3:
                time.sleep(0.25)
                print('GOT IT!', name,'was caught!')
                capture = capture + 1
            else:
                print('Drat! It managed to escape!')
                time.sleep(0.5)
        else:
            print('It broke loose!')
            time.sleep(0.5)
    else:
        print('It evaded the capture beam!')
        time.sleep(0.5)
print(attempts," Attempts to capture ",name)
input()
