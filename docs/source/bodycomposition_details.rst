Calculating Body Composition
============================

This is a collection of the most popular bodyfat percentage equations calculated by measuring various skinfold sites in millimeters.

Here is the typical workflow for calculating bodyfat percentage from skinfold sites:

1. Collect the measurements from the skinfold sites required by the equation you chose.  Appropriate skinfold sites can be found in the documentation_.
2. Calculate body density. 
3. Calculate bodyfat using the above body density value.    

Every subclass in this module inherits from the GenericCalculator class which has 5 methods that calculate bodyfat percentage from body density:

* brozek()
* ortiz()
* schutte()
* siri()
* wagner()

These methods are required to convert body density to bodyfat in all but one equation.

   **If you're unsure which calculation to use, chose siri() because it is generically applicable to most populations**.

Here is a hypothetical example.

A 40 year old female whose skinfold measurements in millimeters are:

* triceps = 7 
* biceps = 5 
* subscapular = 4
* suprailliac = 10

To instantiate classes in this module pass the following arguments in this order:

* Age
* Sex
* A list of skinfold measurements. Order does not matter.

.. code-block:: python

   >>> from composition.bodyfat import DurninWomersley
   >>> calc = DurninWomersley(40, 'female', (7, 5, 4, 10))
   >>> calc.body_density()

   # body density value

   1.046703631104186

   # pass the body density value to a bodyfat equation inherited from GenericCalculator

   >>> calc.siri(calc.body_density())
   22.9

According to the Durnin Womersley equation our hypothetical female's bodyfat is 22.9%.

As noted above, there is one equation that converts your measurements directly into bodyfat.  This is the JacksonPollock4Site class.

Lets do another run through.

A 25 year old male skinfold measurements in millimeters are:

* abdominal = 6 
* triceps = 6
* thigh = 8
* suprailiac = 6

.. code-block:: python

   >>> from composition.bodyfat import JacksonPollock4Site
   >>> calc = JacksonPollock4Site(25, 'male', (6, 5, 8, 6))

   # Calculates bodyfat directly

   >>> calc.body_fat()
   5.2

Our hypothetical male has a bodyfat percent of 5.2%.


.. _documentation:

   