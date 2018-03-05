def lambda_handler(event, context):
    # TODO implement
    if event["messages"][0]["unstructured"]["text"] == "Hello":
        return "Hi, how can I help you with?"
    else:
        return "Hi, I am glad to help!"