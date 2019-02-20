from functools import reduce
def getPrimes():
    return list(filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0, map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(1,100))))

print(getPrimes())