
def mergesort(arr,f,l):
   if f<l:
      mid=(f+l)//2
      mergesort(arr,f,mid)
      mergesort(arr,mid+1,l)
      merge(arr,f,mid,l)


def merge(arr,f,mid,l):
     s1 = mid-f+1
     s2 = l-mid
     L  = [0]*(s1)
     R  = [0]*(s2)
     for i in range(0,s1):
         L[i]=arr[f+i]
     for j in range(0,s2):
         R[j]=arr[mid+1+j]
     i = 0
     j = 0
     k = f
     while i<s1 and j<s2:
          if L[i]<R[j]:
             arr[k]=L[i]

             i+=1
          else:
              arr[k]=R[j]

              j+=1
          k+=1
     while i < s1:
         arr[k] = L[i]
         i+=1
         k+=1
     while j < s2:
         arr[k] = R[j]
         j+=1
         k+=1




n=int(input(" "))
arr=[]
for i in range(n):
    t=int(input(" "))
    arr.append(t)
mergesort(arr,0,n-1)
print(arr)

