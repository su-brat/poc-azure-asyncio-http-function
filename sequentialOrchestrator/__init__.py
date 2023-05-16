import logging
import time
import requests
import azure.functions as func


def post_requests(url, data):
    responses = []
    for body in data:
        responses.append(requests.post(url, json=body))
    return responses


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    start_time = time.time()
    url = "http://localhost:7071/api/service"
    data = [{"name": "Subrat"}, {"name": "Sunil"}, {"name": "Sushri"}, {"age": 25}]
    res_list = post_requests(url, data)
    for response in res_list:
        logging.info(response.status_code)
        logging.info(response.text)
    end_time = time.time()
    return func.HttpResponse(
        f"Time taken to respond: {end_time-start_time}", status_code=200
    )
