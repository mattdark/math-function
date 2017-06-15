import re
import numpy as np
import matplotlib.pyplot as plt

def graph(string, x_range):
    replacements = {
        'sin' : 'np.sin',
        'cos' : 'np.cos',
        'tan' : 'np.tan',
        'exp': 'np.exp',
        'sqrt': 'np.sqrt',
        '^': '**',
    }
    allowed_words = [
        'x',
        'sin',
        'cos',
        'tan',
        'sqrt',
        'exp',
    ]
    ''' evaluates the string and returns a function of x '''
    # find all words and check if all are allowed:
    for word in re.findall('[a-zA-Z_]+', string):
        if word not in allowed_words:
            raise ValueError(
                '"{}" is forbidden to use in math expression'.format(word)
            )

    for old, new in replacements.items():
        string = string.replace(old, new)

    x = np.array(x_range)
    y = eval(string)
    plt.plot(x, y)
    plt.savefig('graph.png', bbox_inches='tight')
    plt.show()
    plt.gcf().clear()

formula = input('Function: ')
lower_limit = eval(input("Lower limit: "))
upper_limit = eval(input("Upper limit: "))
graph(formula, range(lower_limit, upper_limit))
