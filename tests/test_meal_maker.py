from meals import meal_maker
import pytest


class TestMealMaker(object):

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