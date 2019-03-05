import JenkinsLib as JL

JenkinsLib_functions = dir(JL)

def lin_search(aim, list):
    n = 0
    value_found = False
    while n < (len(list)):
        if aim == list[n]:
            value_found = True
            n=n+1
        else:
            n = n+1
            value_found = False
    if value_found == True:
        print("value found in list")
    if value_found != True:
        print ("value not found in list")

def search_JenkinsLib_functions(aim):
    TL.lin_search(aim,JenkinsLib_functions)

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
                    
def Binary_Search_Num(aim,list):
    min = 0
    max = len(list)
    found = False
    while found == False:
        mid = int((min+max)/2)
        if aim == mid:
            found = True
            print ("found")
        if aim < mid:
            max = mid
        if aim > mid:
            min = mid
    


