import JenkinsLib as JL

def lin_search(aim, list):
    n = 0
    value_found = False
    while n < (len(list)):
        if aim == list[n]:
            value_found = True
            n=n+1
        else:
            n = n+1
    if value_found != True:
        print ("value not found in list")
    if value_found == True:
        print("value found in list")
        value_found = False

def search_JenkinsLib_functions(aim):
    JL.lin_search(aim,JenkinsLib_functions)

def bubble_sort_num(list):
    A = 0
    B = 1
    pass_n = 1
    swaps = 0
    list_len = len(list)
    while pass_n < list_len :
        for I in list:
            if B == list_len:
                A = 0
                B = 1
                pass_n = pass_n+1
            else:
                if list[A] > list [B]:
                    index_A = list[A]
                    index_B = list[B]
                    list[B] = index_A
                    list[A] = index_B
                    A = A + 1
                    B = B + 1
                else:
                    A = A+1
                    B = B+1
    return list
                    
def Binary_Search_Num(aim,list):
    min = 0
    max = len(list)
    not_Found = False
    guesses = 1
    while not_Found != True:
        mid = int((min+max)/2)
        if aim == mid:
            print ("value found in list after "+str(guesses)+" guesses")
        if aim < mid:
            max = mid
            guesses=guesses+1
        if aim > mid:
            min = mid
            guesses=guesses+1
        if mid == max or mid == min:
            print("Value not found in list")
            not_Found = True


def Functions():
    return JenkinsLib_functions #These must go at the end of JL
    
JenkinsLib_functions = dir(JL)
    


