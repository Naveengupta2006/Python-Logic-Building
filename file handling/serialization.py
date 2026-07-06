import json
l = [1,2,3,4]

with open('demo.json','w') as f:
    json.dump(l,f)

#dict 
d = {
    'name':'nitist',
    'age':3,
    'gender':'male'
}

with open('demo.json','w') as f:
    json.dump(d,f)