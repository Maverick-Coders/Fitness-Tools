from fitness_tools.exercise import rm_estimator
import pytest


class TestRMCalculator(object):

    @pytest.fixture(params=['', '20', 'twenty', -20, 21])
    def value_error_reps(self, request):
        return request.param

    @pytest.fixture(params=['', 'twenty', -20, 100.3, 100])
    def value_error_weight(self, request):
        return request.param

    def test_desired_reps_raise_value_error(self, value_error_reps):
        with pytest.raises(ValueError, message="Expected ValueError"):
            rm_estimator.RM_Estimator(150.0, 5, value_error_reps)

    def test_current_reps_raise_value_error(self, value_error_reps):
        with pytest.raises(ValueError, message="Expected ValueError"):
            rm_estimator.RM_Estimator(150, value_error_reps, 5)

    def test_current_weight_raises_value_error(self, value_error_weight):
        with pytest.raises(ValueError, message='Expected ValueError'):
            rm_estimator.RM_Estimator(value_error_weight, 5, 10)

    @pytest.mark.parametrize("current_weight,current_reps,desired_reps,base,expected",
                               [
                                (150.0, 10, 5, 5, 175.0),
                                (150.0, 10, 5, 2.5, 175.0),
                                (150.0, 8, 5, 2.5, 162.5),
                                (150.0, 8, 5, 5, 165.0)
                               ])
    def test_estimations(self, current_weight, current_reps, desired_reps, base, expected):
        assert rm_estimator.RM_Estimator(current_weight, current_reps, desired_reps).estimate_weight(base=base) == pytest.approx(expected)
