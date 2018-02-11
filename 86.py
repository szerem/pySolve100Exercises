
checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries-new.txt", "r") as file_cuntries:
    content = file_cuntries.readlines()

content = [i.rstrip() for i in content]
checked = [i for i in content if i in checklist]

print(checked)