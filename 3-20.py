a = input('please input:')
try:
    a=int(a)
    if isinstance(a,(int)) == True:
        print(a)
except:
    print('str')

