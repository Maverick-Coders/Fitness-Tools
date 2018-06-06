class RM_Estimator(object):
    """
    This class is used to estimate correct weight and repetition combinations.
    Enter the your current weight, current reps, and your desired reps to use this class.
    NOTES: For best results use the weight from 5 or less reps to estimate your one rep max.
           Percentages of the one rep max are within ± 0.5 to 2% depending on your training status.

    :param current_weight: the weight you are currently using as a float ending in 0.0 or 0.5.
    :param current_reps: the reps you are currently completing using the current_weight as a whole number.
    :param desired_reps: the desired repeitions to complete as a whole number.

    """

    _percent_max = {1: 1, 2: 0.95, 3: 0.93, 4: 0.9, 5: 0.87, 6: 0.85,
                   7: 0.83, 8: 0.8, 9: 0.77, 10: 0.75, 11: 70, 12: 0.67,
                   13: 0.665, 14: 0.66, 15: 0.65, 16: 0.64, 17: 0.63,
                   18: 0.62, 19: 0.61, 20: 0.6
                   }

    def __init__(self, current_weight, current_reps, desired_reps):
        self.current_weight = current_weight
        self.current_reps = current_reps
        self.desired_reps = desired_reps

        # error checking

        if self.current_reps not in self._percent_max or self.desired_reps not in self._percent_max:
            raise ValueError('Please enter a whole number between 1 and 20 for current_reps and desired_reps paramaters.')

        if str(self.current_weight).endswith(('.0', '.5')) is False or self.current_weight <= 0:
            raise ValueError('Current weight paramater must be a nonnegative number ending in .0 or .5')

        # if isinstance(self.current_weight) is False or self.current_weight <= 0:
        #     raise ValueError('Please enter a whole nonnegative number for current weight parameter.')

        # TODO add a class method to construct the weight value in kilograms?

    def estimate_weight(self, base=2.5):
        """
        Takes params current_weight, current_reps, and desired_reps and returns the estimated weight for your desired reps rounded to the base keyword argment.
    
        :param base: The value that you wish to round to.  Most commonly 2.5 or 5.0
        :return: estimated_weight
        :rtype: float
    
        """

        estimated_weight = ((self.current_weight/self._percent_max[self.current_reps])
                            * self._percent_max[self.desired_reps])

        return float(base * round(float(estimated_weight)/base))
