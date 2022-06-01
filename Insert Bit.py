import random

def insert_bit(number):
    string = str(number)
    new_string = string
    one_count = 0
    zero_count = 0
    one_proportion = 0
    zero_proportion = 0
    majority = ""
    
    for byte in string:
        if byte in "1":
            one_count += 1
        if byte in "0":
            zero_count += 1
    
    one_proportion = (one_count / len(string)) * 100
    zero_proportion = 100 - one_proportion
    
    if one_count > zero_count:
        diff = one_count - zero_count
        minority = "0"
    else:
        diff = zero_count - one_count
        minority = "1"
    
    for i in range(diff):
        index = random.randint(0, len(string) - 1)
        new_string = new_string[:index] + minority + new_strin[index:]
    
    print(f"1's Quantity: {str(one_count)}")
    print(f"0's Quantity: {str(zero_count)}")
    print(f"1's Proportion: {str(round(one_proportion, 2))}%")
    print(f"0's Proportion: {str(round(zero_proportion, 2))}%")
    print(f"Difference of {str(round(diff/len(string) * 100, 2))}% ({str(diff)} bit(s))")
    print("Mostly 1's" if minority else "Mostly 0's")
    print(f"{str(len(string))} Numbers")
    print(f"Original number: {string}")
    print(f"{len(new_string)} Numbers")
    print(f"Modified number: {new_string}")

insert_bit()
