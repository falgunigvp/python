#5 program to match blood group

print("----------Match two blood groups----------")
print(" ")

bldgrp ={ 'A+':['A+', 'A-', 'O+', 'O-'],
          'A-': ['A-', 'O-'],
          'B+':['B+', 'B-', 'O+', 'O-'],
          'B-': ['B-', 'O-'],
          'AB+':['A+', 'A-', 'O+', 'O-','B+', 'B-','AB-'],
          'O+': ['O+', 'O-'],
          'O-':['O-']
        }

bld_1=input("Enter first blood group:( ig. A+ , B- etc.) ").upper()
print(" ")

bld_2=input("Enter blood group to Match: ").upper()
print(" ")
 
if bld_1 in bldgrp and bld_2 in bldgrp:
    if bld_2 in bldgrp[bld_1]:
        print("Matched")
    else:
        print("Not matched")
else:
    print("Enter valid blood group")