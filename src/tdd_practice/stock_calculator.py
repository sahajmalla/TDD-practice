def sum_current_stock(A,B,C,max_fill,min_threshold):
    if(max_fill <= 0):
        return 'invalid'
    if((A < 0) or (B < 0 ) or (C < 0)):
        return 'invalid'
    if(A > max_fill or B > max_fill or C > max_fill):
        return 'invalid'
    if (A < min_threshold):
        return f'A needs {min_threshold - A} to fill'