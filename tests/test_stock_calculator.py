import src.tdd_practice.stock_calculator as stock_calculator

def test_A8_FR_01_stock_gap_exceeds_threshold_object_A():
    max_fill = 10
    min_threshold = 2
    
    A = 5
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 5

def test_A8_FR_02_stock_gap_equals_threshold_boundary():
    max_fill = 10
    min_threshold = 2
    
    A = 10
    B = 8
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 0

def test_A8_FR_03_stock_gap_exceeds_threshold_object_C():
    max_fill = 10
    min_threshold = 2
    
    A = 10
    B = 10
    C = 3
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 7

def test_A8_FR_04_summation_logic():
    max_fill = 10
    min_threshold = 2
    
    A = 5
    B = 8
    C = 3
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 12

def test_A8_FR_05_zero_stock_handling():
    max_fill = 10
    min_threshold = 2
    
    A = 0
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 10

def test_BVA_01_gap_exactly_equals_threshold():
    max_fill = 10
    min_threshold = 2
    
    A = 8
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 0

def test_BVA_02_gap_just_above_threshold():
    max_fill = 10
    min_threshold = 2
    
    A = 7
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 3

def test_BVA_03_gap_just_below_threshold():
    max_fill = 10
    min_threshold = 2
    
    A = 9
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 0

def test_BVA_04_current_stock_is_zero():
    max_fill = 10
    min_threshold = 2
    
    A = 0
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 10

def test_BVA_05_current_stock_equals_target():
    max_fill = 10
    min_threshold = 2
    
    A = 10
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 0

def test_BVA_06_current_stock_exceeds_target():
    max_fill = 10
    min_threshold = 2
    
    A = 11
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 0

def test_BVA_07_minimum_threshold_is_zero():
    max_fill = 10
    min_threshold = 0
    
    A = 9
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 1
