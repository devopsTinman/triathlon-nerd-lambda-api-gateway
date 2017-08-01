def lambda_handler(event, context):
	print("in lambda handler")
	
	resp = {
		"statusCode": 200,
		"headers": {
			"Access-Control-Allow-Origin": "*",
		},
		"body": "DevOps Tinman"
	}