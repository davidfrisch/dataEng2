#  cwltool cwl_scripts/6_plot_results.cwl \
#    --X_test_pca X_test_pca.pkl \
#    --X_test X_test.pkl \
#    --y_pred y_pred.pkl \
#    --y_test y_test.pkl \
#    --target_names target_names.pkl \
#    --height h.pkl \
#    --width w.pkl \
#    --clf clf.pkl 
# 

cwlVersion: v1.2
baseCommand: [/mnt/data/dataEng2/workflow_a_thing/venv/bin/python3.9, /mnt/data/dataEng2/workflow_a_thing/pipeline/6_plot_results.py]
class: CommandLineTool

inputs: 
    X_test_pca:
        type: File
        inputBinding:
            position: 1
            prefix: --X_test_pca

    X_test:
        type: File
        inputBinding:
            position: 1
            prefix: --X_test
    y_pred:
        type: File
        inputBinding:
            position: 2
            prefix: --y_pred
    y_test:
        type: File
        inputBinding:
            position: 3
            prefix: --y_test
    target_names:
        type: File
        inputBinding:
            position: 4
            prefix: --target_names
    height:
        type: File
        inputBinding:
            position: 5
            prefix: --h

    width:
        type: File
        inputBinding:
            position: 6
            prefix: --w

    clf:
        type: File
        inputBinding:
            position: 7
            prefix: --clf

outputs:
    plot:
        type: File
        outputBinding:
            glob: results.png


