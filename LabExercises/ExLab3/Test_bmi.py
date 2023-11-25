from lab2.Exercise1.bmi import calculate_bmi

def test_bmi_normal_weight():
    # Test for normal weight
    result = calculate_bmi(weight=57,height=1.73)
    assert result == 0

def test_bmi_over_weight():
    # Test for over weight
    result = calculate_bmi(weight=57,height=1.73)
    assert result == 1

def test_bmi_under_weight():
    # Test for underweight
    result = calculate_bmi(weight=57,height=1.73)
    assert result == -1
