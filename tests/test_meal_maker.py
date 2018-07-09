from meals import meal_maker
import pytest


class TestMealMaker(object):

    # Error Checking

    @pytest.fixture(params=['mesomorf', 3, ''])
    def value_error_body_type(self, request):
        return request.param

    @pytest.mark.xfail(raises=AttributeError)
    def test_body_type_raises_value_error(self, value_error_body_type):
        with pytest.raises(ValueError, message="Expected ValueError"):
            meal_maker.MakeMeal(150, body_type=value_error_body_type)

    @pytest.mark.parametrize("fat_percent, carb_percent, protein_percent",
                            [
                                (None, 0.1, 0.2),
                                (None, None, 0.1),
                                (0.3, None, None), 
                                (None, None, None),
                                (0.4, None, 0.3),
                                (0.6, 0.4, None),
                                ('six', 'four', 0.1)
                            ])

    def test_macronutrient_percent_raises_type_error(self, fat_percent, carb_percent, protein_percent):
        with pytest.raises(TypeError, message="Expected TypeError"):
            meal_maker.MakeMeal(150, body_type=None, fat_percent=fat_percent, carb_percent=carb_percent, protein_percent=protein_percent)
    
    @pytest.mark.parametrize("fat_percent, carb_percent, protein_percent",
                            [
                                (0.9, 0.1, 0.2),
                                (0.1, 0.2, 0.3),
                            ])
    def test_macronutrient_percent_raises_value_error(self, fat_percent, carb_percent, protein_percent):
        with pytest.raises(ValueError, message="Expected ValueError"):
            meal_maker.MakeMeal(150, body_type=None, fat_percent=fat_percent, carb_percent=carb_percent, protein_percent=protein_percent)

    @pytest.fixture(params=[-150, 0])
    def value_error_check_weight(self, request):
        return request.param

    @pytest.fixture(params=['', 'one-hundred', 150.5, 100.0])
    def type_error_check_weight(self, request):
        return request.param

    def test_check_weight_type_error(self, type_error_check_weight):
        with pytest.raises(TypeError, message="Expected TypeError"):
            meal_maker.MakeMeal(type_error_check_weight)

    def test_check_weight_value_error(self, value_error_check_weight):
        with pytest.raises(ValueError, message="Expected Value Error"):
            meal_maker.MakeMeal(value_error_check_weight)

    @pytest.mark.xfail(raises=AttributeError)
    @pytest.mark.parametrize("activity_level, goal",
                            [
                                ('sedintary', 'w_l'),
                                ('moderate', ''),
                                ('very', 100),
                                (50, 'weight_loss'),
                                ('', 'maintenance'),
                                ('vry', 'weight_gain'),
                            ])
    def test_set_optimum_calories_raises_value_error(self, activity_level, goal):
        with pytest.raises(ValueError, message="Expected ValueError"):
            meal_maker.MakeMeal(150, activity_level=activity_level, goal=goal)

    # Test assigned macronutrient percentages by body type

    @pytest.mark.parametrize("body_type, expected",
                            [
                            ('MESOMORPH', 0.3),
                            ('Ectomorph', 0.2), 
                            ('endomorph', 0.4),
                            ])
    def test_fat_percent(self, body_type, expected):
        assert meal_maker.MakeMeal(150, body_type=body_type).fat_percent == expected

    @pytest.mark.parametrize("body_type, expected",
                            [
                            ('MESOMORPH', 0.3),
                            ('Ectomorph', 0.25), 
                            ('endomorph', 0.35),
                            ])
    def test_protein_percent(self, body_type, expected):
        assert meal_maker.MakeMeal(150, body_type=body_type).protein_percent == expected

    @pytest.mark.parametrize("body_type, expected",
                            [
                            ('MESOMORPH', 0.4),
                            ('Ectomorph', 0.55), 
                            ('endomorph', 0.25),
                            ])
    def test_carb_percent(self, body_type, expected):
        assert meal_maker.MakeMeal(150, body_type=body_type).carb_percent == expected

    @pytest.mark.parametrize("body_type, activity_level, goal, expected_min_cal",
                            [
                                ('mesomorph', 'sedintary', 'weight_loss', 10),
                                ('mesomorph','sedintary', 'maintenance', 12),
                                ('mesomorph','sedintary', 'weight_gain', 16),
                                ('endomorph', 'moderate', 'weight_loss', 12),
                                ('endomorph','moderate', 'maintenance', 14),
                                ('endomorph','moderate', 'weight_gain', 18),
                                ('ectomorph', 'very', 'weight_loss', 14),
                                ('ectomorph','very', 'maintenance', 16),
                                ('ectomorph','very', 'weight_gain', 20),
                            ])
    def test_expected_min_cal(self, body_type, activity_level, goal, expected_min_cal):
        assert meal_maker.MakeMeal(150, body_type=body_type, activity_level=activity_level, goal=goal).min_cal == expected_min_cal