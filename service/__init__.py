import logging
import time
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    start_time = time.time()
    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")
    end_time = time.time()
    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully in {end_time-start_time}."
        )
    else:
        return func.HttpResponse(
            f"This HTTP triggered function executed in {end_time-start_time}. Pass a name in the query string or in the request body for a personalized response.",
            status_code=400,
        )
