Guessing Repetitions
==================

Research shows that different repetition ranges yield different results.  Generally speaking the following training adaptations occur:

* Endurance between 10 - 15 repetitions
* Hypertrophy (muscle growth) between 8 - 12 repetitions
* Strength <= 6 repetitions
* Power between 1 - 6 repetitions

With that being said, the fitness enthusiast uses repetition ranges congruent with their goals.

Those goals, however, change over time and there is a need to reassign the proper weight and repetition range quickly.

Lets say you can lift 175 lbs. 10 times and now you want increase your strength.  Lets set your new rep goal to 6.

When creating a new RM_Estimator object pass the following arguments in this order:

* Current weight used ending in .0 or .5
* Current repetitions you can complete with the above weight
* Desired repetitions

.. code-block:: python

   >>> from fitness_tools.exercise.rm_estimator import RM_Estimator
   >>> new_reps = RM_Estimator(175.0, 10, 6)
   >>> new_reps.estimate_weight()
   197.5

By this calculation if you can lift 175 lbs 10 times you should be able to lift 197.5 lbs. approximately 6 times.


By default the estimate_weight() function rounds the results to the nearest 2.5 lbs.  You can alter the rounding behavior by passing the base keyword argument like so:

.. code-block:: python

   >>> from fitness_tools.exercise.rm_estimator import RM_Estimator
   >>> new_reps = RM_Estimator(175.0, 10, 6)
   >>> new_reps.estimate_weight(base=5)
   200.0


If you are trying to estimate your one rep max use the weight from 5 or less repetitions for best results.

Percentages of your one rep max are within ± 0.5 to 2% depending on your training status.
