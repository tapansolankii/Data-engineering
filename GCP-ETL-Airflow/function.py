from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "Project-df-cric"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
      {        "jobName": "bq-load",  # Provide a unique name for the job
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

