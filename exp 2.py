def railfence(s,k):
    ans=['' for i in range(k)]
    d=-1
    i=0
    for j in s:
        ans[i]+=j
        if i==k-1 or i==0:d*=-1
        i+=d
    return ''.join(ans)
def rail_decrypt(s):
    n=len(s)
    i,j=0,(n+1)//2
    ans=''
    while True:
        ans+=s[i]
        i+=1
        if j==n:break
        ans+=s[j]
        j+=1
    return ans
msg=input('Enter Plain text: ')
cipher=railfence(msg,2)
print('Cipher text: ',cipher)
dec=rail_decrypt(cipher)
print('Decrypted cipher: ',dec)
