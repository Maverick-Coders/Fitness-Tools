class MakeMeal(object):
    """
    Use this class to create optimal meals regardless of your body type or fitness goals.

    :param weight: Enter your current weight.
    :param goal: Select a goal: 'weight_loss', 'maintenance', 'weight_gain', or None.
    :param body_type: Select a body type: 'endomorph', 'ectomorph', 'mesomorph' or None.
    :param activity_level: Select an activity level, 'sedentary', 'moderate', 'very', or None.
    :param min_cal: Enter the desired minimum calories per pound defaults to None.
    :param max_cal: Enter the desired maximum calories per pound defaults to None.
    :param fat_percent: Enter the desired percent of calories from fat defaults to None.
    :param protein_percent: Enter the desired percent of calories from protein defaults to None.
    :param carb_percent: Enter the desired percent of calories from carbohydrates defaults to None.

    Usage: There are four ways to use this class:

        1) Fully custom:

            Pass the following parameters manually: weight, desired minimum and maximum calories,
            and fat_percent, protein_percent, carb_percent.
            This allows for the finest control over all parameters.

        2) Preset calorie ranges custom macronutrient percentages:

            Pass a valid combination of goal and activity_level (see above)
            pass fat_percent, protein_percent, carb_percent manually.
            Yields ideal min_cal and max_cal values.

        3) Preset macronutrient percentages custom calorie ranges:

            Pass a valid body_type (see above)
            pass min_cal and max_cal manually.
            Yields ideal fat_percent, protein_percent, and carb_percent values

        4) Preset macronitrient percentages and calorie ranges.

           Pass valid body_type, activity_level, and goal (see above).
           Yields ideal fat_percent, protein_percent, carb_percent
           min_cal and max_cal.

    """

    def __init__(self, weight, goal=None, body_type=None, activity_level=None,
                 min_cal=None, max_cal=None, fat_percent=None,
                 protein_percent=None, carb_percent=None):

        self.weight = weight
        self.goal = goal
        self.body_type = body_type
        self.activity_level = activity_level
        self.min_cal = min_cal
        self.max_cal = max_cal
        self.fat_percent = fat_percent
        self.protein_percent = protein_percent
        self.carb_percent = carb_percent

        # These set the optimal caloric range and macronitriant ratios if the correct parameters are passed.

        self._check_weight()
        self._check_body_type()
        self._set_optimum_calories()
        self._check_macronutrient_percentages()
        self._check_min_cal()
        self._check_max_cal()

    def _check_weight(self):

        if isinstance(self.weight, int) is True:
            if self.weight <=0:
                raise ValueError('Weight must be a positive integer.')

        else:
            raise TypeError('Param weight must be type int.')

    #TODO Add check calorie for int

    def _check_min_cal(self):
        if self.min_cal is not None:
            if isinstance(self.min_cal, int) is True:
                if self.min_cal <=0:
                    raise ValueError('Min_cal must be a positive integer.')
            else:
                raise TypeError('Min_cal must be of type int.')

    def _check_max_cal(self):
        if self.max_cal is not None:
            if isinstance(self.max_cal, int) is True:
                if self.max_cal <=0:
                    raise ValueError('Max_cal must be a positive integer.')
            else:
                raise TypeError('Max_cal must be of type int.')

    def _check_body_type(self):

        """If valid body_type is passed; set the ideal fat_percent,
        protein_percent, and carb_percent in __init__."""

        if self.body_type is not None:

            if self.body_type.casefold() == 'mesomorph':
                self.fat_percent = 0.3
                self.protein_percent = 0.3
                self.carb_percent = 0.4

            elif self.body_type.casefold() == 'ectomorph':
                self.fat_percent = 0.2
                self.protein_percent = 0.25
                self.carb_percent = 0.55

            elif self.body_type.casefold() == 'endomorph':
                self.fat_percent = 0.4
                self.protein_percent = 0.35
                self.carb_percent = 0.25

            else:
                raise ValueError("Please enter a valid body type: 'endomorph', 'ectomorph', 'mesomorph', or set body_type to None")

    def _set_optimum_calories(self):
        """If valid activity_level and goals is passed; set the ideal min_cal and max_cal in __init__. """
            
        if self.activity_level is not None and self.goal is not None:

            if self.activity_level.casefold() == 'sedentary' and self.goal.casefold() == 'weight_loss':
                self.min_cal = 10
                self.max_cal = 12
            elif self.activity_level.casefold() == 'sedentary' and self.goal.casefold() == 'maintenance':
                self.min_cal = 12
                self.max_cal = 14
            elif self.activity_level.casefold() == 'sedentary' and self.goal.casefold() == 'weight_gain':
                self.min_cal = 16
                self.max_cal = 18
            elif self.activity_level.casefold() == 'moderate' and self.goal.casefold() == 'weight_loss':
                self.min_cal = 12
                self.max_cal = 14
            elif self.activity_level.casefold() == 'moderate' and self.goal.casefold() == 'maintenance':
                self.min_cal = 14
                self.max_cal = 16
            elif self.activity_level.casefold() == 'moderate' and self.goal.casefold() == 'weight_gain':
                self.min_cal = 18
                self.max_cal = 20
            elif self.activity_level.casefold() == 'very' and self.goal.casefold() == 'weight_loss':
                self.min_cal = 14
                self.max_cal = 16
            elif self.activity_level.casefold() == 'very' and self.goal.casefold() == 'maintenance':
                self.min_cal = 16
                self.max_cal = 18
            elif self.activity_level.casefold() == 'very' and self.goal.casefold() == 'weight_gain':
                self.min_cal = 20
                self.max_cal = 22
            else:
                raise ValueError("Please enter a valid goal; 'weight_loss', 'maintenance', 'weight_gain' or activity_level; 'sedentary', 'moderate', or 'very' alternatively, set these parameters to None.")

    def _check_macronutrient_percentages(self):
        """Checks if the sum of macronuitrient percentages equals one hunderd percent."""

        if isinstance(self.fat_percent, float) is True and isinstance(self.protein_percent, float) is True and isinstance(self.carb_percent, float) is True:
            if self.fat_percent + self.protein_percent + self.carb_percent != 1:
                raise ValueError('The sum of fat_percent, protein_percent, and carb_percent must equal 1')
        else:
            raise TypeError('Kwags fat_percent, protein_percent, and carb_percent must be float type.')
    
    def daily_min_calories(self):
        """Returns the total daily minimum calories."""
        min_calories = self.weight * self.min_cal
        return round(min_calories, 0)

    def daily_max_calories(self):
        """Returns the total daily maximum calories."""
        max_calories = self.weight * self.max_cal
        return round(max_calories, 0)

    def daily_min_fat(self):
        """Returns the total daily minimum fat in grams."""
        daily_min_fat = (self.daily_min_calories() * self.fat_percent) / 9
        return round(daily_min_fat, 0)

    def daily_max_fat(self):
        """Returns the total daily maximum fat in grams."""
        daily_max_fat = (self.daily_max_calories() * self.fat_percent) / 9
        return round(daily_max_fat, 0)

    def daily_min_protein(self):
        """Returns the total daily minimum protein in grams."""
        daily_min_protein = (self.daily_min_calories() * self.protein_percent) / 4
        return round(daily_min_protein, 0)

    def daily_max_protein(self):
        """Returns the total daily maximum protein in grams."""
        daily_max_protein = (self.daily_max_calories() * self.protein_percent) / 4
        return round(daily_max_protein, 0)

    def daily_min_carbs(self):
        """Returns the total daily minimum carbohydrates in grams."""
        daily_min_carbs = (self.daily_min_calories() * self.carb_percent) / 4
        return round(daily_min_carbs, 0)

    def daily_max_carbs(self):
        """Returns the total daily maximum protein in grams."""
        daily_max_carbs = (self.daily_max_calories() * self.carb_percent) / 4
        return round(daily_max_carbs, 0)

    def daily_requirements(self):
        """
        Returns a dictionary of recommended calories and macronutrients for the day.

        :return: daily_requirements
        :rtype: dict

        """

        daily = {
            'min_calories': round(self.daily_min_calories(), 0),
            'max_calories': round(self.daily_max_calories(), 0),
            'min_fat': round(self.daily_min_fat(), 0),
            'max_fat': round(self.daily_max_fat(), 0),
            'min_protein': round(self.daily_min_protein(), 0),
            'max_protein': round(self.daily_max_protein(), 0),
            'min_carbs': round(self.daily_min_carbs(), 0),
            'max_carbs': round(self.daily_max_carbs(), 0),
        }

        return daily

    def make_meal(self, number_meals):
        """
        Returns a dictionary of recommended calories and macronutrients for one meal.

        :param number_meals:
        :type number_meals: int
        :return: meal
        :rtype: dict

        """

        meal = {}

        for k, v, in self.daily_requirements().items():
            meal[k] = round(v / number_meals, 0)

        return meal
