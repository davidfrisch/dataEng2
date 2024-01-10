from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import loguniform
from sklearn.svm import SVC
from time import time
import pickle
import argparse

def train_svm(X_train_pca_filepath, y_train_filepath):
    X_train_pca = pickle.load(open(X_train_pca_filepath, "rb"))
    y_train = pickle.load(open(y_train_filepath, "rb"))

    print("Fitting the classifier to the training set")
    t0 = time()
    param_grid = {
        "C": loguniform(1e3, 1e5),
        "gamma": loguniform(1e-4, 1e-1),
    }
    clf = RandomizedSearchCV(
        SVC(kernel="rbf", class_weight="balanced"), param_grid, n_iter=10
    )
    clf = clf.fit(X_train_pca, y_train)
    print("done in %0.3fs" % (time() - t0))
    print("Best estimator found by grid search:")
    print(clf.best_estimator_)
    pickle.dump(clf, open("clf.pkl", "wb"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train SVM")
    parser.add_argument("--X_train_pca_filepath", type=str, default="X_train_pca.pkl")
    parser.add_argument("--y_train_filepath", type=str, default="y_train.pkl")
    args = parser.parse_args()
    train_svm(args.X_train_pca_filepath, args.y_train_filepath)