import o_lib.o_consts as o_consts

def verbose_print(*msg, end:str="\n", sep:str=""):
    # NOTE: The * allows for any amount of parameters
    if o_consts.VERBOSE: 
        print(*msg, end=end, sep=sep)

def debug_print(*msg, end:str="\n", sep:str=""):
    # NOTE: The * allows for any amount of parameters
    if o_consts.DEBUG:
        print(*msg, end=end, sep=sep)