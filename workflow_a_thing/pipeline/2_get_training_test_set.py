from time import time

import matplotlib.pyplot as plt
from scipy.stats import loguniform
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import pickle
import os

def get_training_test_set():
    lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

    # introspect the images arrays to find the shapes (for plotting)
    n_samples, h, w = lfw_people.images.shape

    # for machine learning we use the 2 data directly (as relative pixel
    # positions info is ignored by this model)
    X = lfw_people.data
    n_features = X.shape[1]

    # the label to predict is the id of the person
    y = lfw_people.target
    target_names = lfw_people.target_names
    n_classes = target_names.shape[0]

    print("Total dataset size:")
    print("n_samples: %d" % n_samples)
    print("n_features: %d" % n_features)
    print("n_classes: %d" % n_classes)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # dump the data
    pickle.dump(X_train, open("X_train.pkl", "wb"))
    pickle.dump(X_test, open("X_test.pkl", "wb"))
    pickle.dump(y_train, open("y_train.pkl", "wb"))
    pickle.dump(y_test, open("y_test.pkl", "wb"))
    pickle.dump(target_names, open("target_names.pkl", "wb"))
    pickle.dump(h, open("h.pkl", "wb"))
    pickle.dump(w, open("w.pkl", "wb"))

if __name__ == "__main__":
    get_training_test_set()