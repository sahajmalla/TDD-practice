import src.tdd_practice.stock_calculator as stock_calculator

def test_calculate_current_stock_invalid_max_fill_less_than_or_equal_to_zero():
    max_fill = -1
    A = 5
    B = 5
    C = 5
    min_threshold = 8
    
    stock_calculator.sum_current_stock(A,B,C,max_fill,min_threshold)
    
    assert stock_calculator.sum_current_stock(A,B,C,max_fill,min_threshold) == 'invalid'
    

def test_calculate_current_stock_negative():
    A = -3
    B = -5
    C = -8
    max_fill = 10   
    min_threshold = 8
    stock_calculator.sum_current_stock(A,B,C,max_fill,min_threshold)

    
    #assert that sum current stock is invalidate
    assert stock_calculator.sum_current_stock(A,B,C,max_fill,min_threshold) == 'invalid'
    
def test_calculate_current_stock_more_than_max_fill():
    max_fill = 10
    A = 11
    B = 100
    C = 10.1
    min_threshold = 8
    stock_calculator.sum_current_stock(A,B,C,max_fill,min_threshold)

    assert stock_calculator.sum_current_stock(A,B,C,max_fill,min_threshold) == 'invalid'

    
def test_calculate_production_quantities():
    # Example Calculation:
    # Current stocks: A = 5, B = 8, C = 3
    A = 5
    B = 8
    C = 3
    
    # Desired fill levels: A = 10, B = 10, C = 10
    max_fill = 10
    
    # Minimum threshold = 2
    min_threshold = 2
    
    # For A: gapA=10-5=5 (5 > 2, so produce 5)
    # For B: gapB=10-8=2 (2 is not > 2, so produce 0)
    # For C: gapC=10-3=7 (7 > 2, so produce 7)
    # Total to produce: 5+0+7=12
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 12

def test_calculate_production_boundary_gap_equals_threshold():
    # Gap is exactly equal to threshold -> Should produce 0
    max_fill = 10
    min_threshold = 5
    
    # A gap = 5 (10-5), equal to threshold -> 0
    A = 5
    # B gap = 4 (10-6), less than threshold -> 0
    B = 6
    # C gap = 6 (10-4), greater than threshold -> 6
    C = 4
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 6

def test_calculate_production_all_full():
    # All slots full -> 0 production
    max_fill = 10
    min_threshold = 2
    A = 10
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 0

def test_calculate_production_all_empty():
    # All slots empty -> Max production (if gap > threshold)
    max_fill = 10
    min_threshold = 2
    A = 0
    B = 0
    C = 0
    
    # Each gap is 10, 10 > 2, so produce 10+10+10 = 30
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 30

def test_calculate_production_high_threshold():
    # Threshold higher than max_fill -> No production ever possible
    max_fill = 10
    min_threshold = 11
    A = 0
    B = 0
    C = 0
    
    # Gaps are 10, but threshold is 11. 10 is not > 11.
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 0
