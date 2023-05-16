import logging
import time
import azure.functions as func
import aiohttp
import asyncio


async def async_post_requests(url, data):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(session.post(url, json=body)) for body in data]
        responses = await asyncio.gather(*tasks)
    return responses


async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    start_time = time.time()
    url = "http://localhost:7071/api/service"
    data = [{"name": "Subrat"}, {"name": "Sunil"}, {"name": "Sushri"}, {"age": 25}]
    res_list = await async_post_requests(url, data)
    for response in res_list:
        logging.info(response.status)
        txt = await response.text()
        logging.info(txt)
    end_time = time.time()
    return func.HttpResponse(
        f"Time taken to respond: {end_time-start_time}", status_code=200
    )
