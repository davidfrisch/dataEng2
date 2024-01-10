# cwltool cwl_scripts/2_get_data_set.cwl 
cwlVersion: v1.2
baseCommand: [/mnt/data/dataEng2/workflow_a_thing/venv/bin/python3.9, /mnt/data/dataEng2/workflow_a_thing/pipeline/2_get_training_test_set.py]
class: CommandLineTool

# No input parameters
inputs: []
  
outputs:
  X_train:
    type: File
    outputBinding:
      glob: "X_train.pkl"
  X_test:
    type: File
    outputBinding:
      glob: "X_test.pkl"
  y_train:
    type: File
    outputBinding:
      glob: "y_train.pkl"
  y_test:
    type: File
    outputBinding:
      glob: "y_test.pkl"
  target_names:
    type: File
    outputBinding:
      glob: "target_names.pkl"
  h:
    type: File
    outputBinding:
      glob: "h.pkl"
  w:
    type: File
    outputBinding:
      glob: "w.pkl"

  