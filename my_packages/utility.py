def validate(n):
    # validate that n is a number
    if type(n)==int or type(n)==float:
        return n
    else:
        return 1 # a sensible default