a=list(map(int,input().split()))
if (a[0]>a[1] and a[0]>a[2]):
  print(a[0])
elif (a[1]>a[0] and a[1]>a[2]):
  print(a[1])
else:
  print(a[2])
