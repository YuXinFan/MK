def facn2():
    print('you will get a n*n matrix made of the numbers you input')
    n=input('n=')
    n=int(n)
    all=[]
    for i in range(n):
        all.append([])
        all[i]=[]
        
        while i<=n-1:
            f=input('number:')
            if f==';':
                break
            else:
                all[i].append(f)
    for i in all:
        for e in i:
            print(e,end=' ')
        print('\n')
    C=[c for c in range(n)]
    for i in range(n):
        for l[C[i]] in all:
            
                
            
