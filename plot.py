#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def main():
    data = pd.read_csv('./datasets/simple.csv')



    plt.plot([0.0, 0.0], [0.0,4.0],color='black', linestyle='dashed')
    plt.plot([0.5, 0.5], [0.0,4.0],color='black')
    plt.plot([1.0, 1.0], [0.0,4.0],color='black',linestyle='dashed')

    for y in data['dx'].unique():
        plt.plot(data[data['dx'] == y]['x1'], data[data['dx'] == y]['x2'], 'o')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
