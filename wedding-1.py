from typing import List
import numpy as np
import random
boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']

wedding = []

while len(wedding)<16:
    b=random.choice(boys)
    g=random.choice(girls)
    if b not in wedding:
        wedding.append(b)
    if g not in wedding:
        wedding.append(g)    
print(wedding)







