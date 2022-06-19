def dfa_Check(your_String : str , t_table : dict , aceepting_state:list )-> bool:

    current_state = 0 # start state is zero
    for eachCharacter in your_String:
        current_state = t_table[current_state][eachCharacter]
    return True if current_state in aceepting_state else False


if __name__ == "__main__":
    yourString = input("enter your String")
    t_table = {
        0:{"a" : 1 , "b":4},
        1:{"a" : 2 , "b":3},
        2:{"a" : 2 , "b":3},
        3:{"a" : 8 , "b":3},
        4:{"a" : 5 , "b":4},
        5:{"a" : 8 , "b":6},
        6:{"a" : 8 , "b":7},
        7:{"a" : 8 , "b":8},
        8:{"a" : 8 , "b":8},
    }

   

    if dfa_Check(yourString , t_table , aceepting_state= [1,3,4,7]):
        print("Aceepted String")
    else:
        print("Not Accepted String")
