# cwltool cwl_scripts/5_run_prediction.cwl --clf_filepath clf.pkl --X_test_pca_filepath X_test_pca.pkl
cwlVersion: v1.2
baseCommand: [/mnt/data/dataEng2/workflow_a_thing/venv/bin/python3.9, /mnt/data/dataEng2/workflow_a_thing/pipeline/5_run_prediction.py]
class: CommandLineTool

inputs: 
  clf_filepath: 
    type: File
    inputBinding:
      position: 1
      prefix: --clf_filepath

  X_test_pca_filepath:
    type: File
    inputBinding:
      position: 2
      prefix: --X_test_pca_filepath


outputs: 
  y_pred:
    type: File
    outputBinding:
      glob: y_pred.pkl


