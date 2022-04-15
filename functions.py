class BinaryOperations:

    # constructor 
    def __init__(self,operation): 
        self.this_list=[]
        self.operation=operation

    # adds element x to the list
    def add_to_list(self,x):
        if x not in self.this_list:
            self.this_list.append(x)

    def f(self,nr1,nr2):    # transforms the string into a computation
        x=nr1
        y=nr2
        result=eval(self.operation)
        return result            

    def to_print(self): # tests if it is binary operation and prints it
        ok = 1   # we suppose the operation is commutative
        for i in self.this_list:
            for j in self.this_list:
                if self.f(i,j) not in self.this_list: 
                    ok = 0  # we found out it is not commutative 
                    break
            else:
                continue    # only executed if the inner loop did NOT break
            break           # only executed if the inner loop DID break
        if ok==1:
            print("Binary operation:", self.operation)
        else:
            print(self.operation,"is not a binary operation.")
        print(" ")

    def commutative(self): # tests if the operation is commutative
        ok=1
        for i in self.this_list:     # the value of x
            for j in self.this_list: # the value of y
                if self.f(i,j)!=self.f(j,i):
                    ok=0
                    break
                else: 
                    continue
                break
        if ok==1:          # returns true if it is commutative
            return True     
        else:
            return False

    def associative(self):  # verifies the associativity
        ok=1
        for i in self.this_list:      # we get 3 numbers of the list simultaneously
            for j in self.this_list:
                for k in self.this_list:
                    if self.f(self.f(i,j),k)!=self.f(i,self.f(j,k)):   # verify for each case the mathematical expression
                        ok=0                                           # e.g. (i?j)?k=i?(j?k), where ? represents the operation itself
                        break    # if we find a case that doesn't correspond we break the loops and we know it is not associative
                    else:
                        continue
                    break
                else:
                    continue
                break
        if ok==1:
            return True
        else:
            return False

    def neutral_element(self):  # computes the neutral element as a global variable
        ok=1
        global Nelement
        for i in self.this_list:   # the value of Nelement
            for j in self.this_list:   # the value of x
                if self.f(i,j)!=self.f(j,i) or self.f(i,j)!=j:
                    ok=0
                    break  # i cannot be the neutral element so we break the inner loop and search for another i
            if ok==1:  # after ending the inner loop we can tell if we found the neutral element
                Nelement=i
                break
        if ok==1:
            return True
        else:
            return False

    def reverse_element(self): # checks if in our list is a reverse element 
        ok=1
        if self.neutral_element()==False:
            return False
        for i in self.this_list:  # the value of x' (reverse element)
            for j in self.this_list: # the value of x
                if self.f(i,j) != self.f(j,i) or self.f(i,j)!=Nelement:
                    ok=0
                    break
            if ok==1:
                break
        if ok==1:
            return True
        else:
            return False

    def associative_and_commutative(self): # display the correct message regarding commutativity and associativity
        if self.commutative()== True: 
            print("The operation is commutative.")
        else:
            print("The operation is not commutative.")
        if self.associative()==True:
            print("The operation is associative.")
        else:
            print("The operation is not associative.")

    def commutative_group(self): # display the correct message regarding being a commutative group
        if self.associative()==True and self.neutral_element()==True and self.reverse_element()==True:
            if self.commutative()==True:
                print("Commutative group.")
            else:
                print("Group.")
        else:
            print("Not a group.")
        print(" ")

