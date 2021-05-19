
#r = "TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC" 
#patterns = ["CCT", "CAC", "GAG", "CAG", "ATC"]
with open('dataset_317416_4.txt') as f:
    s = f.readline()
    patterns =f.read().splitlines()
#s = "AAAAAAAAAAAA" 
#patterns = ["A"]
#print(s)
#print(patterns)
l = len(s)
Index = []
#def is_dpattern (pattern):
#    for i in range(1, len(pattern)):
#        if pattern[i] == pattern[0]:
#            return i
#            break
def find_pattern(s, pattern):
    global Index
    #i = is_dpattern (pattern)
    #print("Ive been here")
   # print(len(s))
   # print(len(pattern))
    while len(s) >= len(pattern):
       # print("Ive been here")
#        print(pattern)
 #       print(s)
        if pattern in s:
           a = s.find(pattern)# + l - len(s)
           t = a+ l - len(s)
  #         print(t)
 #          if(pattern == "GCCAGGTGC"):
  #           print(a)
           if t not in Index:
              Index.append(t)
    #       s = s[a:]
        else:
          break
        if(a == 0):
          #print("dsada")
          s = s[1:]
        else:
          s = s[a:]
        
    return Index
    
#class Memoize:
#    def __init__(self, f):
#        self.f = f
#        self.memo = {}
#    def __call__(self, *args):
#        if not args in self.memo:
#            self.memo[args] = self.f(*args)
#        return self.memo[args]
#find_pattern = Memoize(find_pattern)     
Positions = [find_pattern(s, pattern) for pattern in patterns]
list_string = map(str, Positions[-1])

#print(sorted(list_string))
sor = sorted(list_string)
with open('o.txt', 'a') as of:
  for x in sor:
    of.write(' '+x)
