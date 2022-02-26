# bloom filter
from random import randint 

def hash_helper(x,Nb):
    a=randint(1,10)
    b=a+1
    return (a*x+b)%Nb

def bloom_filter():
    Nb=int(input('Enter size of bit array(Nb):'))
    N_hash=int(input('Enter number of hash functions:'))
    hashes=[lambda x: hash_helper(x,Nb) for _ in range(N_hash)]
    
    SET=list(map(int,input('Enter Set elements(S):').split()))
    N_SET=len(SET)
    
    BIT_ARRAY=[False]*Nb

    for i in SET:
        for fn in hashes:
            idx=fn(i)
            BIT_ARRAY[idx]=True
    print('Bit Array => ',[int(i) for i in BIT_ARRAY])
        
    input_stream=[randint(1,100) for _ in range(25)]
    print('Input Streaam= > ',input_stream)
    FALSE_POSITIVES=0
    
    for i in input_stream:
        flag=True
        for fn in hashes:
            flag = flag and BIT_ARRAY[fn(i)]
        if(flag):
            print('{} is Positive'.format(i),end='')
            if(i not in SET):
                FALSE_POSITIVES+=1
                print(' => FALSE POSITIVE',end='')
            print()
        #else:
        #    print('{} is Negative'.format(i))
            
    print('False Positives:',FALSE_POSITIVES)

    



bloom_filter()
        
