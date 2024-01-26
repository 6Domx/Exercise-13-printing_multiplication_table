# Pseudocode
# 1. Create a multiplication table up to 10
# 2. Return the result

# loop for numbers across at the top
for number_across in range(1, 11):
# loop for numbers going down at the side
    for number_down in range(1, 11):
# printing the result of their multiplication
        print(number_across * number_down, end= " ")
# pattern of printing for the results
    print("\t\t")