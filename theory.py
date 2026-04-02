import re
string="She sells sea shells on the sea shore"
pattern1="shell"

if re.match(pattern1,string):
    print("Found")
else:
    print("Not Found")

pattern2="sea"
if re.match(pattern2,string):
    print("Found")
else:
    print("Not Found")

