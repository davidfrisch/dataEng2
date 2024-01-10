cwlVersion: v1.2
baseCommand: [python3, /mnt/data/dataEng2/workflow_a_thing/pipeline/1_download_data.py]
class: CommandLineTool

inputs:
  url:
    type: string
    inputBinding:
      position: 1
      prefix: --url

  filename:
    type: string
    inputBinding:
      position: 2
      prefix: --filename


outputs: []


  