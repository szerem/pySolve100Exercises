from pprint import pprint 

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

pprint(d["employees"][1]["lastName"])

d["employees"][1]["lastName"]="Smooth"
pprint(d["employees"][1]["lastName"])
