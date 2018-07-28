Macronutrient Assignments
=========================

The idea of proper nutrition is certainly opinionated.
While the information one may encounter can vary drastically, calculating your calorie and macronutrient requirements should not be difficult once you have settled on a paradigm that is right for you.

The goal of this package is to automate these calculations so you can spend more time following through with your nutrition plan.

There are two functions of note here:

* daily_requirements() which returns a dictionary of recommended calories and macronutrients for a day based on your input.
* make_meal(int) returns a dictionary of recommended calories and macronutrients for a meal based on your input and passing int through the function.

Please review the documentation_ for a complete list of parameters and their accepted values.

.. _documentation: https://fitness-tools.readthedocs.io/en/latest/fitness_tools.meals.html

There is one class in this package, MakeMeal, and four ways to use it.  The only positional argument is weight and everything else is dictated by keyword arguments.
Here is the usage ordered from most to least opinionated:

Preset Macronutrient Percentages And Calorie Ranges
---------------------------------------------------

Your body type dictates your macronutrient percentages.  Further, your activity level and goal dictates your calorie range per pound.

.. code-block:: python

   >>> from fitness_tools.meals.meal_maker import MakeMeal
   >>> body_type_activity_level_goal = MakeMeal(180, goal='maintenance',
                                                activity_level='moderate',
                                                body_type='mesomorph')

   >>> body_type_activity_level_goal.daily_requirements()

   # returns calories and fat, protein, and carbs in grams for one day

   {
   'min_calories': 2520,
   'max_calories': 2880,
   'min_fat': 84.0,
   'max_fat': 96.0,
   'min_protein': 189.0,
   'max_protein': 216.0,
   'min_carbs': 252.0,
   'max_carbs': 288.0
   }

   # Daily requirements divided by 4 meals

   >>> body_type_activity_level_goal.make_meal(4)

   {
   'min_calories': 630.0,
   'max_calories': 720.0,
   'min_fat': 21.0,
   'max_fat': 24.0,
   'min_protein': 47.0,
   'max_protein': 54.0,
   'min_carbs': 63.0, '
   max_carbs': 72.0
   }

Preset Macronutrient Percentages Custom Calorie Ranges
------------------------------------------------------

Your body type sets the macronutrient percentages and you provide min_cal and max_cal per pound.

.. code-block:: python

   >>> from fitness_tools.meals.meal_maker import MakeMeal
   >>> body_type_custom_cal = MakeMeal(180, min_cal=12, max_cal=14, body_type='ectomorph')

   # returns calories and fat, protein, and carbs in grams for one day

   >>> body_type_custom_cal.daily_requirements()
   {
   'min_calories': 2160,
   'max_calories': 2520,
   'min_fat': 48.0,
   'max_fat': 56.0,
   'min_protein': 135.0,
   'max_protein': 158.0,
   'min_carbs': 297.0,
   'max_carbs': 346.0
   }

   # Daily requirements divided by 3 meals

   >>> body_type_custom_cal.make_meal(3)
   {
   'min_calories': 720.0,
   'max_calories': 840.0,
   'min_fat': 16.0,
   'max_fat': 19.0,
   'min_protein': 45.0,
   'max_protein': 53.0,
   'min_carbs': 99.0,
   'max_carbs': 115.0
   }

Preset Calorie Ranges Custom Macronutrient Percentages
-------------------------------------------------------

Your activity level and goal sets the calorie range per pound.  You set the percentage of calories from fat, carbs, and protein manually.

.. code-block:: python

   >>> from fitness_tools.meals.meal_maker import MakeMeal
   >>> activity_level_goal_custom_macros = MakeMeal(180, activity_level='sedentary',
                                                   goal='weight_loss', fat_percent=0.2,
                                                   protein_percent=0.2, carb_percent=0.6)

   # returns calories and fat, protein, and carbs in grams for one day

   >>> activity_level_goal_custom_macros.daily_requirements()
   {
   'min_calories': 1800,
   'max_calories': 2160,
   'min_fat': 40.0,
   'max_fat': 48.0,
   'min_protein': 90.0,
   'max_protein': 108.0,
   'min_carbs': 270.0,
   'max_carbs': 324.0
   }

   # Daily requirements divided by 6 meals

   >>> activity_level_goal_custom_macros.make_meal(6)
   {
   'min_calories': 300.0,
   'max_calories': 360.0,
   'min_fat': 7.0,
   'max_fat': 8.0,
   'min_protein': 15.0,
   'max_protein': 18.0,
   'min_carbs': 45.0,
   'max_carbs': 54.0
   }

Fully Custom
------------

You are in complete control. Set macronutrient percentages and calorie ranges manually.

.. code-block:: python

   >>> from fitness_tools.meals.meal_maker import MakeMeal
   >>> custom = MakeMeal(180, min_cal=10, max_cal=12, fat_percent=0.2,
                         protein_percent=0.25, carb_percent=0.55)

   # returns calories and fat, protein, and carbs in grams for one day

   >>> custom.daily_requirements()
   {
   'min_calories': 1800,
   'max_calories': 2160,
   'min_fat': 40.0,
   'max_fat': 48.0,
   'min_protein': 112.0,
   'max_protein': 135.0,
   'min_carbs': 248.0,
   'max_carbs': 297.0
   }

    # Daily requirements divided by 8 meals

    >>> custom.make_meal(8)
   {
   'min_calories': 225.0,
   'max_calories': 270.0,
   'min_fat': 5.0,
   'max_fat': 6.0,
   'min_protein': 14.0,
   'max_protein': 17.0,
   'min_carbs': 31.0,
   'max_carbs': 37.0
   }
