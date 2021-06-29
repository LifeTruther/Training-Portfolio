def is_consecutive(a_list):
    if sorted(a_list) == list(range(min (a_list), max(a_list)+1)):
        return True
    else:
        return False
# Several questions on this one
amr = [1,2,3,4,5,6,7,8,9]
print(is_consecutive(amr))
# the terminal seemed very happy with this one, giving me true Yes and true No on test.