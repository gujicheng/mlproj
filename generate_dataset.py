'''
Transformation rules:
set       binary     index
{1}       001        1
{2}       010        2
{3}       100        4
{1,2}     011        3
{1,3}     101        5
{2,3}     110        6
{1,2,3}   111        7
'''
class dataset:
    def __init__(self,N,K):
        self.N = N
        self.K = K
        
        self.vfunction_for_N = [-1] * 2**N #v() for set N
        self.vfunction_for_K = [-1] * 2**N #v() for set K
    
    #transform the index of array into a set
    def index_into_set(self,index):
        set = ()
        for i in range(0,self.N):
            if index & (1 << i) > 0:
                set = set + (i+1,)
        return set

    #transform the set into the index of array
    def set_into_index(self,set):
        index = 0
        for i in set:
            index = index + 2**(i-1)
        return index

    def generate_dataset(self,characteristic_function):
        for i in characteristic_function.keys():
            self.vfunction_for_N[self.set_into_index(i)] = characteristic_function[i]
            if(len(i) <= self.K):
                self.vfunction_for_K[self.set_into_index(i)] = characteristic_function[i]

characteristic_function = {(1,):100,(2,):200,(3,):300,(1,2):500,(2,3):600,(1,3):700,(1,2,3):1000}
#key is the set, value is v(set)
if __name__ == '__main__':
    N = 3 # # of element in set N
    K = 1 # the maximum number of element in set K
    data1 = dataset(3,1)
    data1.generate_dataset(characteristic_function)
    print("data1.vfunction_for_N",data1.vfunction_for_N)
    print("data1.vfunction_for_K",data1.vfunction_for_K)
    for i in range(len(data1.vfunction_for_N)):
        print("set:",data1.index_into_set(i),"  value:",data1.vfunction_for_N[i])
    for i in range(len(data1.vfunction_for_K)):
        print("set:",data1.index_into_set(i),"  value:",data1.vfunction_for_K[i])