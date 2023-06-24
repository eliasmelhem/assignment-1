d={}
L1=['HTTP','HTTPS','FTP','DNS']
L2=[80,443,20,53]
for i in range(4):
    d[L1[i]]=L2[i]
print(d)