PR=0
github={}
for PR in github:
    PR+=1
if PR>=4:
    print("You've successfully completed the Hctoberfest!")
else:
    print("You're almost there,only", 4-PR, "PR's to go!")
