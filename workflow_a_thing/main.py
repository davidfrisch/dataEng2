from pipeline.download_data import download_faces, extract_faces
from pipeline.compute_pca import compute_pca
from pipeline.get_training_test_set import get_training_test_set
from pipeline.train_svm import train_svm
from pipeline.plot_results import plot_results, plot_gallery, title
import pickle

if __name__ == "__main__":
    url = "http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz"
    file_name = "lfw-funneled.tgz"
    
    # 1. Download the dataset
    # input: url, file_name
    # output: file_name
    # download_faces(url, file_name)

    # 2. Extract the faces
    # input: file_name
    # output: None
    # extract_faces(file_name)

    # 3. Compute PCA
    # convert have the data images
    # input: None
    # output: X_train_pca, X_test_pca, eigenfaces
    # get_training_test_set()

    # 4. Train SVM
    # input: X_train, X_test, h, w
    # y_train = pickle.load(open("y_train.pkl", "rb"))
    # y_test = pickle.load(open("y_test.pkl", "rb"))
    # target_names = pickle.load(open("target_names.pkl", "rb"))
    

   
    # compute_pca()

    # X_train_pca = pickle.load(open("X_train_pca.pkl", "rb"))
    # X_test_pca = pickle.load(open("X_test_pca.pkl", "rb"))
    # eigenfaces = pickle.load(open("eigenfaces.pkl", "rb"))

    # 5. Plot results
    # input: X_test_pca, y_pred, y_test, target_names, h, w, clf
    # output: Write the results in the file
    # train_svm()
    # plot_results()
   