with open("dataset_317417_10.txt") as r1:
    s = r1.readline()
#    patterns =str(r1.readlines())
#    patterns = patterns.split()
    reads =r1.read().splitlines()
    k = int(reads[-1])    
    patterns=reads[0]
    patterns = patterns.split()
#print(s)
print(patterns)
print(k)
#print len(text), len(patterns), d
#t = (r.readline()).translate(None, "\n")
#s = "ACATGCTACTTT" 
#patterns = ["ATT", "GCC", "GCTA", "TATT"]
#k = 1

#print len(s), len(patterns), k
Index  = []
def find_pattern(s, pattern, k):
    global Index
    n = len(pattern)
    m = len(s)
    for i in range(0, m - n + 1):
        dist = 0
        for j in range (0, n):
            if s[i + j] != pattern[j]:
                dist += 1
            if dist > k:
                break
       # print dist        
        if dist <= k:
            Index.append(i)
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
positions = [find_pattern(s, pattern, k) for pattern in patterns]
list_string = map(str, positions[-1])

#print(sorted(list_string))
sor = sorted(list_string)
#print(sor)
with open('o.txt', 'a') as of:
  for x in sor:
    of.write(' '+x)
