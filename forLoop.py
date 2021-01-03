for _ in range(10):
    print("ok")
print("Done")

n= int(input())
nrev=0
while(n>0):
    nrev*=10
    nrev+=n%10
    n//=10
print("Reverse of", n, "is", nrev)

print('In rishabhporia02 branch')
print('new chnage')
