patterns = []

with open('dataset_317410_5.txt') as f:
    text = f.readline()
    patterns = [line.rstrip() for line in f]
print(text)
print(patterns)

l=sum([len(i) for i in patterns])

def TirePattern (patterns, l):
    tires = [dict() for x in range(l+2)]
    end = 2
    #print tires
    for pattern in patterns:
       start = 1
       for s in pattern:
         if s in tires[start]:
             start = tires[start][s]
         else:
             print(start, end, s)
             tires[start][s] = end
             start = end
             end += 1
             #print start, end, s
             #start = end
        

    return tires

def PreTireMatch(Text, Tire):
    symbol = Text[0]
    start = 1
    i = 1
    while True:
       # print(start)
        if symbol in Tire[start]:
            start = Tire[start][symbol]
            symbol = Text[i]
            i += 1
            if i >= len (Text):
                return True
                break
        elif Tire[start] == {}:
            #print (Text[:i-1])
            return True
        else:
            #print "no matches found"
            return False

def TireMatching (text, Tire):
    j = 0
    while len(text) > min([len(i) for i in patterns]):
        #print text
        d = PreTireMatch(text, Tire)
        print(d)
        #print(j)
        if d:
            print(j)
            file1 = open("o.txt", "a")  # append mode
            file1.write(str(j)+' ')
        j += 1
        text = text[1:]


Tire = TirePattern (patterns, l)
print(Tire)
TireMatching (text, Tire)
