from time import time
from sklearn.decomposition import PCA
import pickle
import argparse

def compute_pca(X_train_filepath, X_test_filepath, h_filepath, w_filepath):
    n_components = 150
  
    X_train = pickle.load(open(X_train_filepath, "rb"))
    X_test = pickle.load(open(X_test_filepath, "rb"))
    h = pickle.load(open(h_filepath, "rb"))
    w = pickle.load(open(w_filepath, "rb"))

    print(
        "Extracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0])
    )
    t0 = time()
    pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
    print("done in %0.3fs" % (time() - t0))

    eigenfaces = pca.components_.reshape((n_components, h, w))

    print("Projecting the input data on the eigenfaces orthonormal basis")
    t0 = time()
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)
    print("done in %0.3fs" % (time() - t0))

    pickle.dump(X_train_pca, open("X_train_pca.pkl", "wb"))
    pickle.dump(X_test_pca, open("X_test_pca.pkl", "wb"))
    pickle.dump(eigenfaces, open("eigenfaces.pkl", "wb"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute PCA")
    parser.add_argument("--X_train_filepath", type=str)
    parser.add_argument("--X_test_filepath", type=str)
    parser.add_argument("--h_filepath", type=str)
    parser.add_argument("--w_filepath", type=str)
    args = parser.parse_args()
    compute_pca(args.X_train_filepath, args.X_test_filepath, args.h_filepath, args.w_filepath)