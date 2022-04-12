import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_train(X_train,y_train, X_val, y_val, low_lim=0, high_lim=100, text_pos = .7):
    X_for_viz = X_train.sample(15, random_state=40)
    y_for_viz = y_train[X_for_viz.index]

    fig, ax = plt.subplots(figsize=(10, 10))
    sns.scatterplot(x=X_for_viz['Age'], y=X_for_viz['Fare'], hue=y_for_viz,
                    palette={0: 'red', 1: 'green'}, s=200, ax=ax)

    # Now let's take another sample

    # new_x = X_val.sample(1, random_state=33)
    new_x = pd.DataFrame(X_val.loc[484]).T
    new_x.columns = ['Age', 'Fare']
    new_y = y_val[new_x.index]

    print(new_x)
    sns.scatterplot(x=new_x['Age'], y=new_x['Fare'], color='blue', s=200, ax=ax, label='New', marker='P')
    ax.set_xlim(low_lim, high_lim)
    ax.set_ylim(low_lim, high_lim)
    plt.legend()

    #################^^^Old code^^^##############
    ####################New code#################

    # add annotations one by one with a loop
    for index in X_for_viz.index:
        ax.text(X_for_viz.Age[index] + text_pos, X_for_viz.Fare[index], s=index, horizontalalignment='left', size='medium',
                color='black', weight='semibold')


