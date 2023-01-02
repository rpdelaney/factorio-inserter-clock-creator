Factorio Inserter Clock Creator ("ficc")
========================================

Generates factorio blueprints for inserter clocks. Automates an
algorithm from this `video guide <https://www.youtube.com/watch?v=kHvqxKLXs54>`__ by KnightElite.

Installation
------------

.. code:: console

   pip install ficc

Usage
-----

.. code:: console

   $ ficc --help
   usage: ficc [-h] --rate RATE [--stack STACK]

   Generates factorio blueprints for inserter clocks.

   options:
     -h, --help            show this help message and exit
     --rate RATE, -r RATE  Count of items to be carried per second (float) (default: None)
     --stack STACK, -s STACK
                           The item or inserter stack size, whichever is lower (default: 12)

Calculate how many items per second you need your inserter to move. (A
tool like `Rate Calculator <https://mods.factorio.com/mod/RateCalculator>`__ mod or
`Factorio Lab <https://factoriolab.github.io/>`__ is recommended.) Pass
that value to the ``--rate`` argument. For example, iron plates (as
shown in the `video guide <https://www.youtube.com/watch?v=kHvqxKLXs54>`__):

.. code:: console

   $ python3 -m ficc --rate '5.025'
   0eNq1U8tO5DAQ/JWopb2Z2YmZB+TKac97hFXkJB1okdhR2xkxO8q/b9sZHtICAxJIkSPb5arqcvsAVTfiwGQDFAeggD0UL9YU7JA9OQuFvshX20u9XW/kW10o6EyFnaCvOlffC7JBXzMNIaHhl/XIATmr43bWOs7Wi6VeZ1HDZz8zj7WzzeLG/g5GAJ7+YpHlWojQBgqEHorrA1jTo9AJ1gdjw1nt+oqsCY4FOThPs94BHqBYLpYK9uk/iR9irOddrSKBnac+ovM43DKiTSpJcl9SM2OJ65FCmubTn2lKxwO7rqzwzuxIxOV4S50UONsk26A4yCNyjGFutgo83VrTReixinnh7Eqsh/0QV3bEYRTMJDLq0YYd+wo5aquno4Yp3PUYqH43Av0VEUjNChibE9Ho5FlHmtPgxPmq2vmHA3/OoIy9Q0+ltMQ+lJ+JW4EbkM2xWX8IYu7H8rHRoLjcLCVLN4Zh/Bz39P9N6hc32WBNDfK717j6hk7Wbwd7tPQFqUpRg+FUVAE3o9abFSh4DjU+ixORNi68QT3sy/S6ypZdX5IVFiha03l8JfLzWO4/XWio4w==

If you don’t have full stack size research or your recipe has a limited
stack size, you will need to account for that. For example, if you
wanted to clock unloading Rocket Fuel out of a fully moduled and
beaconed Assembler 3:

.. code:: console

   $ python3 -m ficc --rate '0.4' --stack 10
   0eNq1U11vnDAQ/Ctopb45V3DIR3nNU5/zmFTIwJKsCjZam1OvJ/571+aSntQkl0iphADb45nZ8XoPzTDjxGQDVHuggCNUR3MKtsienIVKXxfl1Td9dXEpT3mtYDANDoK+GVz7U5Ad+pZpCgkN361HDshZG5ez3nGWb8osKvjsa+axdbbb3NvbYGTZ02+ssiIXGrSBAqGH6m4P1owoZIL1wdhw1rqxIWuCY0FOztOqtodfUOWbXMEufRdxQ4ztuqpVJLDr0Ed0EV8PjGiTSpLc1dStWOJ2ppCGxfJjWdL2wG6oG3w0WxJx2d7TIOWtNsl2KA6KiJxjlPLn6cGaISIPRawTZzfiPOymOLMlDrNgFlFRTy7sPDbIUVo9bzVM4XHEQO2bCejPSEBKVsDYnUhGJ8860pwGJ84X1c7fnfffDOrYOvRcSk/sQ/2RuBW4CdkcOvWLINZ2rJ/6TIxc5JKlm8M0f4x7+fck9dFJdthSh/zmMZb/oZH168EeLH1CqlLUZDgVVcH9rPVlCQqOQj2ZaOfCK8zTrk53q+7ZjTVZYYGqN4PHFxI/j9X+AU9dp/g=

Development
-----------

You need `poetry <https://python-poetry.org/>`__:

.. code:: console

   poetry install && poetry shell
