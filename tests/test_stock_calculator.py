import src.tdd_practice.stock_calculator as stock_calculator

# ----------------------------------------------------------------------------------
# 2.1 Low-Level Test Cases (TDD)
# Context: Coded during the session to verify internal logic and basic math.
# ----------------------------------------------------------------------------------

def test_A8_FR_01_stock_gap_exceeds_threshold_object_A():
    """
    Test-A8-FR-01: Stock Gap Exceeds Threshold
    Scenario: Current Stock = 5, Target = 10, Threshold = 2.
    Logic: Gap is 5. Since 5 > 2, produce 5.
    """
    max_fill = 10
    min_threshold = 2
    
    A = 5   # Gap = 5 (> 2) -> Produce 5
    B = 10  # Full -> 0
    C = 10  # Full -> 0
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 5

def test_A8_FR_02_stock_gap_equals_threshold_boundary():
    """
    Test-A8-FR-02: Stock Gap Equals Threshold (Boundary Check)
    Scenario: Current Stock = 8, Target = 10, Threshold = 2.
    Logic: Gap is 2. Since 2 is NOT > 2, produce 0.
    """
    max_fill = 10
    min_threshold = 2
    
    A = 10  # Full -> 0
    B = 8   # Gap = 2 (= Threshold) -> Produce 0
    C = 10  # Full -> 0
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 0

def test_A8_FR_03_summation_logic():
    """
    Test-A8-FR-03: Total Production Summation
    Scenario: Mix of different needs (A=5, B=0, C=7).
    Logic: 5 + 0 + 7 = 12.
    """
    max_fill = 10
    min_threshold = 2
    
    A = 5   # Needs 5
    B = 8   # Needs 0 (Gap 2 not > 2)
    C = 3   # Needs 7
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 12

def test_A8_FR_04_zero_stock_handling():
    """
    Test-A8-FR-02-03: Zero Stock Handling
    Scenario: Current Stock = 0 (Empty).
    Logic: Gap is 10. 10 > 2 -> Produce 10.
    """
    max_fill = 10
    min_threshold = 2
    
    A = 0   # Needs 10
    B = 10  # Needs 0
    C = 10  # Needs 0
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 10

# ----------------------------------------------------------------------------------
# 2.2 High-Level Test Cases (Boundary Value Analysis)
# Context: Systematic tests derived from specs to break the logic at the edges.
# ----------------------------------------------------------------------------------

def test_BVA_01_gap_exactly_equals_threshold():
    """
    TC-BVA-01: Gap Exactly Equals Threshold (On-Boundary)
    Scenario: Stock = 8 (Gap 2), Threshold = 2.
    Expected: 0 (Strict inequality check).
    """
    max_fill = 10
    min_threshold = 2
    
    # Target testing on A
    A = 8   # Gap 2 == Threshold 2 -> Produce 0
    B = 10  # Ignored
    C = 10  # Ignored
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 0

def test_BVA_02_gap_just_above_threshold():
    """
    TC-BVA-02: Gap Just Above Threshold (Boundary + 1)
    Scenario: Stock = 7 (Gap 3), Threshold = 2.
    Expected: 3 (Tipping point for production).
    """
    max_fill = 10
    min_threshold = 2
    
    A = 7   # Gap 3 > 2 -> Produce 3
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 3

def test_BVA_03_current_stock_is_zero():
    """
    TC-BVA-04: Current Stock is Zero (Lower Input Boundary)
    Scenario: Stock = 0.
    Expected: 10 (Max possible production per slot).
    """
    max_fill = 10
    min_threshold = 2
    
    A = 0   # Gap 10 -> Produce 10
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 10

def test_BVA_04_current_stock_equals_target():
    """
    TC-BVA-05: Current Stock Equals Target (Upper Input Boundary)
    Scenario: Stock = 10.
    Expected: 0 (No production needed).
    """
    max_fill = 10
    min_threshold = 2
    
    A = 10  # Gap 0 -> Produce 0
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 0

def test_BVA_05_current_stock_exceeds_target():
    """
    TC-BVA-06: Current Stock Exceeds Target (Robustness Boundary)
    Scenario: Stock = 11 (Overfilled manually).
    Expected: 0 (Should not return negative numbers like -1).
    """
    max_fill = 10
    min_threshold = 2
    
    A = 11  # Gap -1 -> Should be treated as 0
    B = 10
    C = 10
    
    # Assert result is 0 (or strictly >= 0)
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 0

def test_BVA_06_minimum_threshold_is_zero():
    """
    TC-BVA-07: Minimum Threshold is Zero (Configuration Boundary)
    Scenario: Stock = 9 (Gap 1), Threshold = 0.
    Expected: 1 (Since 1 > 0 is True).
    """
    max_fill = 10
    min_threshold = 0  # Configuration change
    
    A = 9   # Gap 1 > 0 -> Produce 1
    B = 10
    C = 10
    
    assert stock_calculator.sum_current_stock(A, B, C, max_fill, min_threshold) == 1