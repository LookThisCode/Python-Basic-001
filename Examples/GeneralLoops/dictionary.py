__author__ = 'nickbortolotti'

d1 = {'texto':'hhh','ofensa':'ooo'}
d2 = {}

#print(d1['texto'])

# for key, value in d1.iteritems():
#     print(value)

for c,v in d1.iteritems():
    d2.update({c:v})
    print(v)

print("Segundo paso")
for x,y in d2.iteritems():
     print(x,y)

#for x in d2:
#    print(x['texto'])

