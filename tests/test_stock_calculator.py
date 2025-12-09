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

    
def test_calculate_current_stock_A_is_needed_to_fill():
    max_fill = 10
    min_threshold = 8
    A = 5
    B = 8
    C = 10
    
    stock_calculator.sum_current_stock(A,B,C,max_fill,min_threshold)
    
    assert stock_calculator.sum_current_stock(A,B,C,max_fill,min_threshold) == f'A needs {min_threshold - A} to fill'
    

    
