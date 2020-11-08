import json

my = open('templates/json/ex.json')
js = my.read()

obj = json.loads(js)

lst = obj["data"]["regional"]

#print(len(lst))
n = input("Enter a state name")
for i in range(0,len(lst)):
    if lst[i].get('loc') == n:
        print("Active Cases: ",lst[i].get("confirmedCasesIndian"))
        break
    if i >= len(lst)-1:
        print("Wrong input")