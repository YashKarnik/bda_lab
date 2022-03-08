from itertools import combinations

def pcy(data,threshold,hash_fn):
    
    #Get frequency of eeach element
    MIN=min([min(r) for r in data])
    MAX=max([max(r) for r in data])
    support_dict={}
    for i in range(MIN,MAX+1):
        S=0
        for tpl in data:
            S+=tpl.count(i)
        if(S>=threshold):
            support_dict[i]=S
    print('Frequency of items => ',support_dict)
    
    # Get frequency of each tuple
    sum_array=[0]*11
    for tpl in data:
        comb=list(combinations(tpl,2))
        for inner_tpl in comb:
            sum_array[hash_fn(*inner_tpl)]+=1
    print('Support array => ',sum_array)
    
    # Conver sum to 1 or 0 if element>=threshold
    support_bit_array=[0]*11
    for idx,val in enumerate(sum_array):
        support_bit_array[idx]=int(val>=threshold)
    print('Support bitmap => ',support_bit_array)
    
    # Calculate frequent items as per pcy algo
    frequent_items=[]
    for tpl in list(combinations(range(MIN,MAX+1),2)):
        idx=hash_fn(*tpl)
        if(support_bit_array[idx]==1):
            frequent_items.append(tpl)
    print('Frequent Items => ',frequent_items)
    
    #Check for false positives
    print('True frequent items:')
    test=[]
    for tpl in data:
        test+=list(combinations(tpl,2))
    
    for i in frequent_items:
        S=0
        for j in test:
            if(j==i):
                S+=1
        if(S>=threshold):
            print(i,' => ',S)
    
def main():
    data=[[1,2,3],[2,3,4],[3,4,5],[4,5,6],[1,3,5],[2,4,6],[1,3,4],[2,4,5],[3,5,6],[1,2,4],[2,3,5],[3,4,6]]
    threshold=4
    print('Data = ',data)
    print('Support Threshold =',threshold)
    print('Hash function => (i*j) % 11')
    print('Buckets => 12')
    print('Bit array Size => 11\n')
    pcy(data,threshold,lambda a,b : (a*b)%11)

main()
