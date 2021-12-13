'''
Transformation rules:
string_tuple        num_set       binary     index
('A',)              (1,)          001        1
('B',)              (2,)          010        2
('C',)              (3,)          100        4
('A','B')           (1,2)         011        3
('A','C')           (1,3)         101        5
('B','C')           (2,3)         110        6
('A','B','C')       (1,2,3)       111        7
'''
import random
random.seed(10)
class dataset:
    def __init__(self,N,K,input_for_characteristic_function):
        self.N = N
        self.K = K
        
        self.vfunction_for_N = [-1] * 2**N #v() for set N
        self.vfunction_for_K = [-1] * 2**N #v() for set K
        self.string_into_num = [-1] * (N+1) #string_into_num[0] = -1 forever it record the relationship between string and num
        for i in range(1,N+1):
            self.string_into_num[i] = input_for_characteristic_function[i-1]


    #transform the index of array into num set
    #input: 7   output:(1,2,3)
    def index_into_num_set(self,index):
        set = ()
        for i in range(0,self.N):
            if index & (1 << i) > 0:
                set = set + (i+1,)
        return set

    #transform num set into the index of array
    #input: (1,2,3)   output:7
    def num_set_into_index(self,set):
        index = 0
        for i in set:
            index = index + 2**(i-1)
        return index

    #transform string_tuple into num_set
    #input:('A','B','C')   output:(1,2,3)
    def string_tuple_into_num_set(self,string_tuple):
        num_set = ()
        for i in string_tuple:

            num_set = num_set + (self.string_into_num.index(i),)
        return num_set

    #transform num_set into string_tuple
    #input:(1,2,3)   output:('A','B','C')
    def num_set_into_string_tuple(self,num_set):
        string_tuple = ()
        for i in num_set:
            string_tuple = string_tuple + (self.string_into_num[i],)
        return string_tuple

    #input:(1,2)     output:[1,1,0]
    def num_set_into_learning_need(self,num_set):
        array = []
        for i in range(1,self.N+1):
            if i in num_set:
                array.append(1)
            else:
                array.append(0)
        return array

    def generate_dataset(self,characteristic_function,random_size):

        data = []
        target = []
        for i in characteristic_function.keys():
            
            self.vfunction_for_N[self.num_set_into_index(self.string_tuple_into_num_set(i))] = characteristic_function[i]
            if(len(i) <= self.K):
                self.vfunction_for_K[self.num_set_into_index(self.string_tuple_into_num_set(i))] = characteristic_function[i]
            
            data.append(self.num_set_into_learning_need(self.string_tuple_into_num_set(i)))
            target.append(characteristic_function[i])

        random_index = random.sample(range(0,len(data)),int(random_size * len(data)))


        partial_data = []
        partial_target = []
        
        for i in random_index:
            partial_data.append(data[i])
            partial_target.append(target[i])

        
        return partial_data,partial_target

#characteristic_function = {(1,):100,(2,):200,(3,):300,(1,2):500,(2,3):600,(1,3):700,(1,2,3):1000}
characteristic_function = {('A',):200,('B',):100,('C',):300,('A','B'):400,('B','C'):500,('A','C'):500,('A','B','C'):800}

input_for_characteristic_function = ('A','B','C')

#key is the set, value is v(set)
if __name__ == '__main__':
    N = 3 # # of element in set N
    K = 2 # the maximum number of element in set K
    random_size = 1 # how much data should we randomize
    data1 = dataset(N,K,input_for_characteristic_function)
    data,target = data1.generate_dataset(characteristic_function,random_size)
    print("data1.vfunction_for_N",data1.vfunction_for_N)
    print("data1.vfunction_for_K",data1.vfunction_for_K)
    for i in range(len(data1.vfunction_for_N)):
        print("set:",data1.num_set_into_string_tuple(data1.index_into_num_set(i)),"  value:",data1.vfunction_for_N[i])
    for i in range(len(data1.vfunction_for_K)):
        print("set:",data1.num_set_into_string_tuple(data1.index_into_num_set(i)),"  value:",data1.vfunction_for_K[i])

    print("data:",data)
    print("target:",target)