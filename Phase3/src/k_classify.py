from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

def predict_one(X_train, X_val, y_train, y_val):
    """
    :param X_train:
    :param X_val:
    :param y_train:
    :param y_val:
    :return:
    """

    X_for_viz = X_train.sample(15, random_state=40)
    y_for_viz = y_train[X_for_viz.index]

    new_x = pd.DataFrame(X_val.loc[484]).T
    new_x.columns = ['Age', 'Fare']


    for k in range(1,11):
        knn = KNeighborsClassifier(n_neighbors = k)
        knn.fit(X_for_viz, y_for_viz)
        print(knn.predict(new_x))



