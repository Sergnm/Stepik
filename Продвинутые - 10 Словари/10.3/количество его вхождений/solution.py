text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
sp = list(text)
result = {}
for sim in sp:
    result[sim] = result.get(sim,0)+1
print(result, sep='\n')
