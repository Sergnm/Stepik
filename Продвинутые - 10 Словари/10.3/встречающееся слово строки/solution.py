s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
sp=s.split()
result={}
for num in sp:
    result[num]=result.get(num,0)+1
print(sp)
print(result,len(result))
maxx=max(result.values())
print(maxx)
sp2=[k for k,v in result.items() if v==maxx]
print(sp2,len(sp2))
print(min(sp2))
