from collections import Counter
def main():
    fileObj=open('words.txt','r')
    s=fileObj.read()
    s=s.lower()
    s=s.replace('.',' ').replace(',',' ').replace('!',' ')
    s=s.split()
    phase_1=[[i,1] for i in s]
    phase_2=sorted(s,key=lambda x:x[0])
    phase_3=[[i,1] for i in phase_2]
    phase_4=Counter(s)
    print('Outcome\n',phase_1,'\n','='*50)
    #print('Map\n',phase_3,'\n','='*50)
    print('Shuffle and sort\n',phase_2,'\n','='*50)
    print('Reduce Phase\n',phase_4,'\n','='*50)
main()
