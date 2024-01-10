# cwltool cwl_scripts/main.cwl  --filename lfw-funneled.tgz --url http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz

cwlVersion: v1.2
class: Workflow

inputs:
  url: string
  filename: string

outputs: []

steps:
  1_download_data:
    run: 1_download_data.cwl
    in:
      url: url
      filename: filename
    out: []

  2_get_data_set:
    run: 2_get_data_set.cwl
    in: []
    out: [X_test, X_train, h, target_names, w, y_test, y_train]
  
  3_compute_pcs:
    run: 3_compute_pcs.cwl
    in:
      X_train_filepath: 2_get_data_set/X_train
      X_test_filepath: 2_get_data_set/X_test
      h_filepath: 2_get_data_set/h
      w_filepath: 2_get_data_set/w
    
    out: [X_train_pca_filepath, X_test_pca_filepath, eigenfaces_filepath]


  4_train_svm:
    run: 4_train_svm.cwl
    in:
      X_train_pca_filepath: 3_compute_pcs/X_train_pca_filepath
      y_train_filepath: 2_get_data_set/y_train

    out: [model]

  5_run_prediction:
    run: 5_run_prediction.cwl
    in:
      X_test_pca_filepath: 3_compute_pcs/X_test_pca_filepath
      clf_filepath: 4_train_svm/model
    
    out: [y_pred]

  6_evaluate:
    run: 6_plot_results.cwl
    in:
      X_test_pca: 3_compute_pcs/X_test_pca_filepath
      X_test: 2_get_data_set/X_test
      y_pred: 5_run_prediction/y_pred
      y_test: 2_get_data_set/y_test
      target_names: 2_get_data_set/target_names
      height: 2_get_data_set/h
      width: 2_get_data_set/w
      clf: 4_train_svm/model

    out: [plot]