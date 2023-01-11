s = "The Terrible Tiger Tore The Towel"
length = len(s)
print(length)
pos = 0
print(0,"T")
while(pos<=length):
    pos = s.find("T",pos+1)
    if(pos == -1):
        break
    print(pos,s[pos])

new_s = s.replace("T","t")
print(new_s)
