import re
matchob = re.match(r'(spo*n)\s(spo*n)\s(spo*n)', 'spn spon spoon spooon')

if matchob:
    print(matchob.group(0))  # Entire match
    print(matchob.group(1))  # First group: "spn"
    print(matchob.group(2))  # Second group: "spon"
else:
    print("No match found")

myP=re.compile(r'(\d{2})-([a-zA-Z]*)-(\d{4})')
myS=myP.search("15-aug-1947 whwn idia won")
print(myS.group(0))
print(myS.groups())