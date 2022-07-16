import json
import fastavro
import awswrangler as wr

def lambda_handler(event, context):
    print(fastavro.__version__)
    print(wr.__version__)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
