import pandas as pd
import numpy as np

#Instructions

# You are supposed to clean the data using to make the data more readable.
# To accomplish this you can use the librairies learned during the lessons.


# 1. Drop Duplicated Rows and Only keep unique ones.
# 2. All Names Should Start with a [C]apital Letter  Alexender for example
# 3. All First Names Should Be written in Capital Letters
#   3.a  If name is null a name replace it by writing False
# 4. All SSN should be unique. can not be the same.
#   4.a If SSN does not exist write 000-00-0000
# 5. Remove all negative signs from the Test3 Column
#   5.a If test value is equal to Nan replace by Test Column mean.
# 6. The new file should be saved as CSV in the path folder
