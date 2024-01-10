# cwltool cwl_scripts/4_train_svm.cwl --X_train_pca_filepath X_train_pca.pkl --y_train_filepath y_train.pkl
cwlVersion: v1.2
baseCommand: [/mnt/data/dataEng2/workflow_a_thing/venv/bin/python3.9, /mnt/data/dataEng2/workflow_a_thing/pipeline/4_train_svm.py]
class: CommandLineTool

inputs: 
    X_train_pca_filepath:
        type: File
        inputBinding:
            position: 1
            prefix: --X_train_pca_filepath
    y_train_filepath:
        type: File
        inputBinding:
            position: 2
            prefix: --y_train_filepath

outputs:
    model:
        type: File
        outputBinding:
            glob: "clf.pkl"



