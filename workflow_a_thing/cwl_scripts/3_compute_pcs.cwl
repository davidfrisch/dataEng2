# cwltool cwl_scripts/3_compute_pcs.cwl --X_train_filepath X_train.pkl --X_test_filepath X_test.pkl --h_filepath h.pkl --w_filepath w.pkl
cwlVersion: v1.2
baseCommand: [/mnt/data/dataEng2/workflow_a_thing/venv/bin/python3.9, /mnt/data/dataEng2/workflow_a_thing/pipeline/3_compute_pca.py]
class: CommandLineTool

inputs: 
    X_train_filepath: 
        type: File
        inputBinding:
            position: 1
            prefix: --X_train_filepath
    X_test_filepath:
        type: File
        inputBinding:
            position: 2
            prefix: --X_test_filepath
    h_filepath:
        type: File
        inputBinding:
            position: 3
            prefix: --h_filepath

    w_filepath:
        type: File
        inputBinding:
            position: 4
            prefix: --w_filepath

outputs:
    X_train_pca_filepath:
        type: File
        outputBinding:
            glob: X_train_pca.pkl
    X_test_pca_filepath:
        type: File
        outputBinding:
            glob: X_test_pca.pkl
    eigenfaces_filepath:
        type: File
        outputBinding:
            glob: eigenfaces.pkl

# bash command would be
# python3.9 3_compute_pca.py --X_train_filepath X_train.pkl --X_test_filepath X_test.pkl --h_filepath h.pkl --w_filepath w.pkl
