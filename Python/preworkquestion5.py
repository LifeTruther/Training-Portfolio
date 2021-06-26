def is_consecutive(a_list):
    if sorted(a_list) == list(range(min (a_list), max(a_list)+1)):
        print("Yes!")
    else:
        print("No!")
#Several questions on this one
x = [1,2,3,4,5,6,7,8,9]
is_consecutive(x)
#the terminal seemed very happy with this one, giving me true Yes and true No on test.