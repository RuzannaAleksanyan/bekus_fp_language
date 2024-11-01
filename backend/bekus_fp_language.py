def run_bekus_fp(user_input):
    rows = user_input.splitlines()
    # clear empty line 
    rows = [row for row in rows if row and row.strip()]

    if len(rows) == 2:
        f_1 = rows[0].find('=')
        if f_1 != -1:
            right1 = rows[0][:f_1]
            rows[0] = rows[0][f_1 + 1:].strip()
        
        f_2 = rows[1].find('(')
        if f_2 != -1:
            right2 = rows[1][:f_2]
            rows[1] = rows[1][f_2 + 1:].strip()
            if rows[1][len(rows[1]) - 1] != ')':
                return "error: A function call does not end with."
            rows[1] = rows[1][:-1]
            
        if right1 != right2:
            return "error: An invalid function is called!"
        
        # if are_valid_arguments(rows[1]):
        return parse(rows[0], rows[1])
        # else:
        #     return "error: Function is called with wrong arguments"

    return "error: Input format is incorrect."

        
# # ???
# def are_valid_arguments(*args):
#     # ???
#     args
#     # print(args)
#     # def is_valid_value(value):
#     #     return isinstance(value, (int, float, bool)) or value is None

#     # for arg in args:
#     #     if isinstance(arg, list):
#     #         for item in arg:
#     #             if not is_valid_value(item):
#     #                 return False  
#     #     elif not is_valid_value(arg):
#     #         return False

#     return True

def parse(function, argument):
    paren_index = function.find('(')
    if paren_index != -1:
        # if paren_index != -1:
        func = function[:paren_index]
        # kazmakerpel rekursiv funkcia
        # func_arg = function[paren_index:]
    else:
        func = function
        return function_validation(func, argument)
   

def function_validation(func, arguments):
    if func == "si":
        index = func[1:]
        if valid_index(index):
            # index cast to int
            print("roz")
            print(arguments)
            return si(index, arguments)
        else:
            error = "non valid index"
            return error
    if func == "id":
        # stugel argumentnery chisht en te voch
        return id(arguments)
    if func == "eq":
        # ???
        # print("roz")
        # print(eq(arguments))
        return eq(arguments)
    # if func == "tl":
    #     print("tl")
    # if func == "apndl":
    #     print("apndl")
    # if func == "apndr":
    #     print("apndr")
    # if func == "null":
    #     print("null")
    # if func == "atom":
    #     print("atom")
    # if func == "+":
    #     print("+")
    # if func == "-":
    #     print("-")
    # if func == "*":
    #     print("*")
    # if func == "and":
    #     print("and")
    # if func == "or":
    #     print("or")
    # if func == "not":
    #     print("not")
    # if func == "comp":
    #     print("comp")
    # if func == "constr":
    #     print("constr")
    # if func == "const":
    #     print("const")
    # if func == "cond":
    #     print("cond")
    # if func == "atom":
    #     print("atom")
    # if func == "eq":
    #     print("eq")
    else:
        return "Non valid function!"


def valid_index(index):
    index += 1
    return True

def si(index, arguments):
    return arguments[index]

# def validating_id_function_arguments(*arguments):
#     def is_valid_value(value):
#         # Check if value is an int, float, bool, or None
#         return isinstance(value, (int, float, bool)) or value is None

#     # Check each argument in the input arguments
#     for arg in arguments:
#         if arg == 'true' or arg == 'false' or arg == 'nil':
#             continue
#         if isinstance(arg, list):
#             # If it's a list, check each item in the list
#             for item in arg:
#                 if not is_valid_value(item):
#                     return False  # Invalid item found
#         elif not is_valid_value(arg):
#             return False  # Invalid argument found

#     return True

def id(*arguments): 
    print("............")
    print(arguments)
    return arguments

def eq(arguments):
    if len(arguments) > 2:
        error = "eq funckian stanum e miayn erku parametr"
        return error