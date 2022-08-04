#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input())
i=n
while(i>0):
    print('* '*n)
    i-=1


# In[2]:


a=int(input())
b=a
i=0
while(a>1):
    print(' '*i,'* '*a)
    i+=1
    a-=1
while(i>=0):
    print(' '*i,'* '*a)
    i-=1
    a+=1
    


# In[3]:


a=int(input())
i=0
while(a>=1):
    print(' '*i+'* '*a)
    i+=1
    a-=1
a=1
while(i>0):
    print(' '*(i-1)+'* '*a)
    i-=1
    a+=1
    


# In[4]:


n=int(input())
print((('* '*n)+'\n')*n)


# In[5]:


s=int(input())
k=s//2
for i in range(s):
    for j in range(s):
        if(i+j==s//2) :
            print('*',end='')
        elif((i==s//2)):
            print('*',end='')
        elif(k==j):
            print('*',end='')
        else:
            print(' ',end='')
    k+=1
    print()
        
            


# In[6]:


n=int(input())
for i in range(n):
    print(' '*i,end='')
    for j in range(i,n):
        print(j+1,'',end='')
    print()
for i in range(n,1,-1):
    print(' '*(i-2),end='')
    for j in range(0,n-i+2):
        print(i+j-1,'',end='')
    print()
        
    


# In[7]:


n=input('enter character')
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=n.upper()
b=a.index(n)
for i in range(b+1,0,-1):
    for j in range(i):
        print(a[j],end=' ')
    print()
for i in range(0,b+1):
    for j in range(i+1):
        print(a[j],end=' ')
    print()
    


# In[8]:


n=int(input())
k=n//2
for i in range((n//2)+1):
    for j in range(n+1):
        if(i+j==n//2 or j==k):
            print(chr(65+i),end=' ')
            a=i
        else:
            print(' ',end=' ')
    k+=1
    print()
k=n//2
b=a
q=1
for i in range(a):
    if(n%2!=0):
        for j in range(n):
            if(i+1==j ):
                print(chr(65+b-1),end=' ')
                b-=1
            elif(i+j==n-2):
                print(chr(65+b),end=' ')
            else:
                print(' ',end=' ')
    else:
        for j in range(n):
            if(i+1==j ):
                print(chr(65+b-1),end=' ')
                b-=1
            elif(i+j==n-1):
                print(chr(65+b),end=' ')
            else:
                print(' ',end=' ')
    print()


# In[9]:


n=int(input())
#upper half
for i in range(n,0,-1):
    print('* '*i,end='')
    print('  '*(n-i)*2,end='')
    print('* '*i)
    
#lower half
for i in range(1,n+1):
    print('* '*i,end='')
    print('  '*(n-i)*2,end='')
    print('* '*i)
    


# In[10]:


n=int(input())
#upper half
for i in range(n,0,-1):
    print('* '*i)
    
#lower half
for i in range(1,n+1):
    print("* "*i) 


# In[11]:


n=int(input())

    
#upper half
for i in range(1,n+1):
    print('* '*i,end='')
    print('  '*(n-i)*2,end='')
    print('* '*i)
    
#lower half
for i in range(n,0,-1):
    print('* '*i,end='')
    print('  '*(n-i)*2,end='')
    print('* '*i)


# In[12]:


n=int(input())
#upper half
for i in range(n,0,-1):
    print(' '*(i-1),end='')
    for j in range(n-i+1,0,-1):
        print(j,end='')
    for k in range(1,n-i+1):
        print(k+1,end='')
    print()
    
#lower half
for i in range(n):
    print(' '*(i+1),end='')
    for j in range(n-i-1,0,-1):
        print(j,end='')
    for k in range(1,n-i-1):
        print(k+1,end='')
    print()


# In[ ]:




