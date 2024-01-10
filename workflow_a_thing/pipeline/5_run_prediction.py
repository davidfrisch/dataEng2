import pickle
import argparse

def run_prediction(clf_filepath, X_test_pca_filepath):
    
    clf = pickle.load(open(clf_filepath, "rb"))
    X_test_pca = pickle.load(open(X_test_pca_filepath, "rb"))

    y_pred = clf.predict(X_test_pca)

    pickle.dump(y_pred, open("y_pred.pkl", "wb"))

if __name__ == "__main__":
      parser = argparse.ArgumentParser(description='Run prediction')
      parser.add_argument('--clf_filepath', type=str, help='Path to clf.pkl', default="clf.pkl")
      parser.add_argument('--X_test_pca_filepath', type=str, help='Path to X_test_pca.pkl', default="X_test_pca.pkl")
      args = parser.parse_args()
      
      run_prediction(args.clf_filepath, args.X_test_pca_filepath)