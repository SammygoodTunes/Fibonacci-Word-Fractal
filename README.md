# Fibonacci-Word-Fractal
Recreation of the fractal obtained from the Fibonacci word.

Explanation:
===================

The Fibonacci word is a special sequence of binary digits, that can be determined using the line of slope 1/φ (φ being the golden ratio [phi approx. = 1.618]).


Using the given binary sequence, we can establish a fractal with the help of a list of rules and the OEDR:


For each digit at position k:

1- If the digit is equaled to 0, draw a line/segment forward (in the direction it's currently facing).


2- If the digit is equaled to 0, turn left 90° if k is even or right 90° if k is odd.


This program is still currently being developed on, and will receive updates in the near future.


Controls:
===================

[Space] -> Reset simulation


[Escape] -> Exit


Installation information:
===================

A "requirements" text file is provided within the repository.


To install the necessary library(ies) to run the script:

1- Open CMD or GitBash


2- Change the current directory to the project path (cd path\\to\\project)


3- Install the library(ies) for the "requirements.txt" file (pip install -r requirements.txt)


Development information:
===================

Developed by: SammygoodTunes


Library(ies) used: Pygame 2.0.1, PyAutoGUI 0.9.52
