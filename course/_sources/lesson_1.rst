
..  shortname:: Lesson 1
..  description:: First lesson on modeling an airtrack.

.. setup for automatic question numbering.

.. qnum::
   :start: 1
   :prefix: sc-1-


Lesson 1: Modeling an Airtrack
==============================
Welcome to the first lesson of ...

We will be using Python ...


Using Print for Output
::::::::::::::::::::::
Let's begin by learning how to print some output to the screen. To do this, we will be using the keyword ``print`` followed by a space and then the desired content to be printed as output. We've provided an example right below; go ahead and click the run button to see the outcome of the program.

.. activecode:: Example-1
	:nocodelens:
	:caption: Print is life

	print "It's over"
	print 9000

And that's all there is to it, pretty simple right? We use quotations marks to tell the program to print exactly what is encapsulated between the two marks. We can also use the ``print`` keyword with numbers as shown on the second line in the program. When used without quotes, Python will instead evaluate whatever is on the right side of the keyword prior to printing.


Python as a Calculator
::::::::::::::::::::::
Well, what do you mean by evaluate? Consider a very simple mathematical expression such as 3 + 4. Of course we all know the outcome of this expression should equal to 7, and you know what, Python is smart enough to know this too. Go ahead and try it out:

.. activecode:: Example-2
	:nocodelens:
	:caption: Baby calculator

	print 3 + 4

At this point, we want to take a moment to identify and explain an important concept, ``whitespace``. This is the spacing between the math expression in the above example. We could write the line instead as ``print 3+4`` and it would achieve the same effect. Although it has no effect on the outcome of the program, whitespace is important because it allows us to group things and make the program much easier to read. 


Value Holders
:::::::::::::
Now something you might want to do is compute a value and store it some place. Actually, Python has just the feature to do so and we're going to call them value holders. So let's go ahead and continue with the expression that was used previously: 3 + 4. This could represent the number of people playing a game and suppose we might want to remember the computed value of 7 as "p" for the total number of players. In a program, it would look something like this:

::

	p = 3 + 4

If we were to read this command, we would say ``p gets 3 plus 4``. More precisely, p gets the value of everything on the right side of that gets operator (what looks like an equals sign). So the result of this is: p got 3 + 4. Meaning somewhere in the computer's memory there is a place labeled p that contains the result of that computation. 

Once this result has been stored, we can use it in the rest of the program. For example, if we wanted to print the value that is stored in p, we could write a simple program like so:

::

	p = 3 + 4
	print p

We could also use p in further computations:

::

	p = 3 + 4
	p = p + 1

In words, this would be read as ``p gets 3 plus 4`` and then ``p gets the stored value of p, plus 1``.  


.. activecode:: Example-3
	:nocodelens:
	:caption: Baby calculator


Drawing Dots
::::::::::::
So we could have the entire lesson and activities written using mathematical expressions and text, but wouldn't it be more exciting if we could draw a visual representation of what is actually being computed? We think so! And to do this, we will be using a small cartesian graph. << insert fancy picture of graph here? >>

If you recall, the x-axis runs horizontally and the y-axis vertically. A common use for a cartesian graph is to plot points and they are denoted as (x-coordinate, y-coordinate). We will be using the ``dot`` method to do so and it follows a simple syntax:



Starting Fresh with a Clear
:::::::::::::::::::::::::::

From Dots to a Line
:::::::::::::::::::

Applying a Slope
::::::::::::::::

Modeling Motion
:::::::::::::::

Airtrack
::::::::



copy code from previous active code box

what, why, how, try