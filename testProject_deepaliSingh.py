PR = 0
github = {}
for pr in github:
    PR+=1

if PR >= 4:
    print("You've successfully completed the Hacktoberfest!")

if PR < 4:
    print("You're almost there, only", 4-PR, " PR's to go!")
