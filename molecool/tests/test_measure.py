"""
Unit tests for measure module.
"""

import molecool 
import numpy as np
import pytest

def test_calculate_distance():
    """Test the calculate distance function"""

    r1 = np.array([0,0,0.8])
    r2 = np.array([0,0,0])

    expected_distance = 0.8
    calculated_distance = molecool.calculate_distance(r1,r2)

    assert calculated_distance == expected_distance

def test_calculate_angle():
    """Test the calculate angle function"""

    rA = np.array([0,0,-1])
    rB = np.array([0,0,0])
    rC = np.array([1,0,0])
    

    expected_angle = 90.0
    calculated_angle = molecool.calculate_angle(rA,rB,rC,degrees=True)


    assert expected_angle == calculated_angle

# @pytest.mark.paramatetrize("varaible_name1,variable_name2, variable_name3,..,variable_nameN, expected_answer",[
#     (varaible_name1,variable_name2,variable_name3,...,variable_nameN, expected_answer)
# ])

def test_calculate_distance_typeerror():
    r1=[0,0,0]
    r2=[0,1,0]

    with pytest.raises(TypeError):
        calculate_distance = molecool.calculate_distance(r1,r2)