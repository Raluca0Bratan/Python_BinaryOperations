from functions import BinaryOperations

# Driver code
if __name__=='__main__':
    object1=BinaryOperations("x+y")
    object1.add_to_list(1)
    object1.add_to_list(2)
    object1.add_to_list(3)
    object1.add_to_list(0)
    object1.to_print()
    object1.associative_and_commutative()
    object1.commutative_group()

    object2=BinaryOperations("x+y-2")
    object2.add_to_list(2)
    object2.to_print()
    object2.associative_and_commutative()
    object2.commutative_group()

    object3=BinaryOperations("x/y")
    object3.add_to_list(9)
    object3.add_to_list(1)
    object3.add_to_list(3)
    object3.to_print()
    object3.associative_and_commutative()
    object3.commutative_group()

    object4=BinaryOperations("-x+y")
    object4.add_to_list(0)
    object4.add_to_list(-1)
    object4.add_to_list(1)
    object4.to_print()
    object4.associative_and_commutative()
    object4.commutative_group()

    object5=BinaryOperations("x**y-2")
    object5.add_to_list(1)
    object5.to_print()
    object5.associative_and_commutative()
    object5.commutative_group()