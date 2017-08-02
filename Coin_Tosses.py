import random
print "Starting the program..."
def Cointoss(num):
 

    flips = 0
    heads = 0
    tails = 0
    result = ""
    while flips < num:
        if random.randint(1,2) == 1:
            print("heads")
            heads += 1
            result = "heads"
        else:
            print("tails")
            tails += 1
            result = "tails"
        flips += 1
        print "Attempt #",flips,": Throwing a coin... It's a", result, heads," heads, and ", tails," tails!"
    input ("exit")

Cointoss(5000)