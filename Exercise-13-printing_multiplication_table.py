# Pseudocode
# 1. Create a multiplication table up to 10
# 2. Return the result

for number_across in range(1, 11):
    for number_down in range(1, 11):
        print(number_across * number_down, end= " ")
    print("\t\t")