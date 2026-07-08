import json

with open('demo.json','r') as f:
    d = json.load(f)
    print(d)
    print(type(d))

# Serialize and deserialize tuple
import json

t = (1,2,3,4,5)

with open('demo.json','w') as f:
    json.dump(t,f)

# serialize and deserialize a nested dict

d = {
    'student':'naveen',
    'marks':[12,3,4,56,56]

}

with open('demo.json','w') as f:
    json.dump(d,f)