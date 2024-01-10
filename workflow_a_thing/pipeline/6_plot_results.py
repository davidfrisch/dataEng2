from matplotlib import pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from time import time
import pickle
import argparse

def plot_results(X_test_pca, y_pred, y_test, target_names, h, w, clf):
    
    print("Predicting people's names on the test set")
    t0 = time()
    y_pred = clf.predict(X_test_pca)
    print("done in %0.3fs" % (time() - t0))

    print(classification_report(y_test, y_pred, target_names=target_names))
    ConfusionMatrixDisplay.from_estimator(
        clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
    )
    plt.tight_layout()
    plt.show()


def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(" ", 1)[-1]
    true_name = target_names[y_test[i]].rsplit(" ", 1)[-1]
    return "predicted: %s\ntrue:      %s" % (pred_name, true_name)


def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())

    plt.savefig("results.png")
    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Plot results')
    parser.add_argument('--X_test_pca', type=str, help='Path to X_test_pca.pkl', default="X_test_pca.pkl")
    parser.add_argument('--y_pred', type=str, help='Path to y_pred.pkl', default="y_pred.pkl")
    parser.add_argument('--y_test', type=str, help='Path to y_test.pkl', default="y_test.pkl")
    parser.add_argument('--target_names', type=str, help='Path to target_names.pkl', default="target_names.pkl")
    parser.add_argument('--h', type=str, help='Height of the image', default="h.pkl")
    parser.add_argument('--w', type=str, help='Width of the image', default="w.pkl")
    parser.add_argument('--clf', type=str, help='Path to clf.pkl', default="clf.pkl")
    args = parser.parse_args()
    
    X_test_pca = pickle.load(open(args.X_test_pca, "rb"))
    X_test = pickle.load(open("X_test.pkl", "rb"))
    y_pred = pickle.load(open(args.y_pred, "rb"))
    y_test = pickle.load(open(args.y_test, "rb"))
    target_names = pickle.load(open(args.target_names, "rb"))
    h = pickle.load(open(args.h, "rb"))
    w = pickle.load(open(args.w, "rb"))
    clf = pickle.load(open(args.clf, "rb"))
    
    plot_results(X_test_pca, y_pred, y_test, target_names, h, w, clf)
    prediction_titles = [
        title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])
    ]
    plot_gallery(X_test, prediction_titles, h, w)

