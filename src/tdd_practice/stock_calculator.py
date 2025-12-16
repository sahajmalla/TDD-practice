def sum_current_stock(A, B, C, max_fill, min_threshold):
    if max_fill <= 0:
        return 'invalid'
    if (A < 0) or (B < 0) or (C < 0):
        return 'invalid'
    if A > max_fill or B > max_fill or C > max_fill:
        return 'invalid'
    
    production_a = 0
    production_b = 0
    production_c = 0
    
    gap_a = max_fill - A
    if gap_a > min_threshold:
        production_a = gap_a
        
    gap_b = max_fill - B
    if gap_b > min_threshold:
        production_b = gap_b
        
    gap_c = max_fill - C
    if gap_c > min_threshold:
        production_c = gap_c
        
    return production_a + production_b + production_c
