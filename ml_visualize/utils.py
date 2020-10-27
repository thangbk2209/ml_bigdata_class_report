import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns 

import matplotlib.pyplot as plt 

import pandas as pd 
from typing import List
import numpy as np


def plot_box(model: str, hidden_size: int):
    file_name = f"{model}_hidden_{hidden_size}"
    file_path = f"data/{file_name}.csv"
    df = pd.read_csv(file_path)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot()
    axe1 = sns.boxplot(data=df, ax=ax1)
    axe1.set_ylabel("Test classification error")
    axe1.set_xlabel("Number of layers")
    plt.savefig(f"result/{file_name}_boxplot.pdf")
    plt.show()


def plot_historgram(model: str, hidden_size: int, layer_size: int):
    pretraining_data = pd.read_csv(f"data/pretraining_{model}_hidden_{hidden_size}.csv")\
                         .iloc[layer_size]
    normal_data = pd.read_csv(f"data/{model}_hidden_{hidden_size}.csv")\
                        .iloc[layer_size]                     
    fig2 = plt.figure()
    ax2 = fig2.add_subplot()
    axe2 = sns.distplot(pretraining_data, ax=ax2, bins=30, kde=False, label='with pretraining')
    axe2 = sns.distplot(normal_data, ax=ax2, bins=30, kde=False, label='with out pretraining')
    axe2.set_ylabel("count")
    axe2.set_xlabel("test error")
    plt.legend(loc='best')
    plt.savefig('result/{model}_hidden_{hidden_size}_layer_{layer_size}_histogram.pdf')
    plt.show()
