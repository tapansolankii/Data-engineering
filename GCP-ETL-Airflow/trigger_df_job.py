from googleapiclient.discovery import build
import base64
import google.auth
import os
# function name entry point in GCL
def trigger_df_job():
 
    service = build('dataflow', 'v1b3')
    project = "project-cricket-de"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
         "jobName": "bq-load",  # Provide a unique name for the job
               "parameters": {
               "javascriptTextTransformGcsPath": "gs://**/udf.js",
               "JSONPath": "gs://**/bq.json",
               "javascriptTextTransformFunctionName": "transform",
               "outputTable": "Project-df-cric:cricket_dataset.icc_odi_batsman_ranking",
               "inputFilePattern": "gs://**/batsmen_rankings.csv",
               "bigQueryLoadingTemporaryDirectory": "gs://dataflow-metadata",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

trigger_df_job()
