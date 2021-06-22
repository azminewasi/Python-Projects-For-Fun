n = input()
n = int(n)
for i in range(n):
s = input()
s1 = ""
s2 = ""
for j in range(len(s)):
if '9' >= s[j] >= '0': s1 += s[j]
else: s2 += s[j]
s1 = sorted(s1)
s2 = sorted(s2)
cnt1=0
cnt2=0
s3 = ""
for j in range(len(s)):
if '9' >= s[j] >= '0':
s3 += s1[cnt1]
cnt1+=1
else:
s3 += s2[cnt2]
cnt2+=1
print (s3)
#Alphabetically and Numerically sorting of a string maintaining relative positions