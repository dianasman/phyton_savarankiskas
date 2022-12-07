# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos

from modules.numbers.numbers import *

from modules.math.composition import composition as addition
from modules.math.division import division
from modules.math.subtraction import substraction
from modules.math.multiplication import multiplication

# Kitų failų ir žemiau esančio kodo nekeiskite
a = addition(one, four);
b = division(four, two);
c = substraction(three, two);
d = multiplication(five, two);

print(a);
print(b);
print(c);
print(d);
