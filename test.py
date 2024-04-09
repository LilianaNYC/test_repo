
dic_candidates = {'Tom':0, "Anna":0}

data = [['Tom', 10], ['Anna', 20], ['Tom', 5]]

for row in data:
    candidate_name= row[0]
    dic_candidates[candidate_name]+=row[1] # same as dic_candidates[candidate_name] = dic_candidates[candidate_name] + row[1]
    
votes = 0   
for i in dic_candidates.values():
    print(i)