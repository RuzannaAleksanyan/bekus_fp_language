from validation import valid_argument

def id(arguments):
    if(valid_argument(arguments)):
        return arguments
    
    return "error: Invalid arguments."

def eq(arguments):
    if(valid_argument(arguments)):
        if len(arguments) != 2:
            return "error: Incorrect number of arguments passed to the eq function."
        return "True" if arguments[0] == arguments[1] else "False"
    
    return "error: Invalid arguments."

def null(arguments):
    if(valid_argument(arguments)):
        if len(arguments) == 1 and arguments[0] == ' ':
            return True
        return all(x is None for x in arguments) if arguments else True
    
    return "error: Invalid arguments."

def add(arguments):
    if(valid_argument(arguments)):
        if len(arguments) != 2:
            return "error: The + function was passed the wrong number of arguments."
        if None in arguments or True in arguments or False in arguments:
            return "error: One of the arguments is invalid."
        if not all(isinstance(x, (int, float)) for x in arguments):
            return "error: The arguments to + must be numbers."
        return arguments[0] + arguments[1]
    
    return "error: Invalid arguments."

def sub(arguments):
    if(valid_argument(arguments)):
        if len(arguments) != 2:
            return "error: The - function was passed the wrong number of arguments."
        if None in arguments or True in arguments or False in arguments:
            return "error: One of the arguments is invalid."
        if not all(isinstance(x, (int, float)) for x in arguments):
            return "error: The arguments to - must be numbers."
        return arguments[0] - arguments[1]
    
    return "error: Invalid arguments."

def mul(arguments):
    if(valid_argument(arguments)):
        if len(arguments) != 2:
            return "error: The * function was passed the wrong number of arguments."
        if None in arguments or True in arguments or False in arguments:
            return "error: One of the arguments is invalid."
        if not all(isinstance(x, (int, float)) for x in arguments):
            return "error: The arguments to * must be numbers."
        return arguments[0] * arguments[1]
    
    return "error: Invalid arguments."

def nott(argument):
    if(valid_argument(argument)):
        if len(argument) != 1:
            return "error: Invalid number of arguments."
        return not argument[0] if isinstance(argument[0], bool) else "error: Invalid argument."

    return "error: Invalid arguments."

def andd(arguments):
    if(valid_argument(arguments)):
        if len(arguments) != 2:
            return "error: The function was passed the wrong number of arguments."
        if not all(isinstance(x, bool) for x in arguments):
            return "error: Both arguments must be boolean values (True or False)."
        return arguments[0] and arguments[1]
    
    return "error: Invalid arguments."

def orr(arguments):
    if(valid_argument(arguments)):
        if len(arguments) != 2:
            return "error: The function was passed the wrong number of arguments."
        if not all(isinstance(x, bool) for x in arguments):
            return "error: Both arguments must be boolean values (True or False)."
        return arguments[0] or arguments[1]
    
    return "error: Invalid arguments."

def si(index, arguments):
    if(valid_argument(arguments)):
        if not index.isdigit():
            return "error: Invalid index format."
        index = int(index)
        return arguments[index - 1] if 0 < index <= len(arguments) else "error: Index out of bounds."

    return "error: Invalid arguments."

def tl(arguments):
    if(valid_argument(arguments)):
        return arguments[1:] if len(arguments) > 1 else "None"

    return "error: Invalid arguments."

def apndl(arg, arguments):
    if(valid_argument(arguments)):
        arguments.insert(0, arg)
        return arguments
    
    return "error: Invalid arguments."

def apndr(arg, arguments):
    if(valid_argument(arguments)):
        arguments.append(arg)
        return arguments

    return "error: Invalid arguments."

def atom(arguments):
    if(valid_argument(arguments)):
        return True
    
    return False