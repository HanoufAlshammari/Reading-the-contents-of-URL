import requests as req

resp = req.get("https://en.wikipedia.org/wiki/Over_the_Garden_Wall")

#print(resp.text)
file = open("wikifle.rtf","w")
x = resp.text.encode('utf-8')
file.write(x)


file.close()

file = open("wikifle.rtf","r")
print(file.read())
file.close()