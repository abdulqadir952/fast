from fastapi import FastAPI, Request,Response
from matplotlib import pyplot as plt
from fastapi.responses import StreamingResponse
import io
import numpy as np
import test
app = FastAPI()

@app.post("/Summation")
async def Summation(info : Request):
    req_info = await info.json()
    a = int(req_info["a"])
    b = int(req_info["b"])
    return {
        "status" : "SUCCESS",
        "Sum" : str(a+b)
    }
@app.post("/getPieChart")
async def getPieChart(info : Request):
    cars = []
    data = []
    req_info = await info.json()
    for i in range(len(req_info["Request"])):
        cars.append(req_info["Request"][i]["Name"])
        data.append(req_info["Request"][i]["Value"])
    fig = plt.figure(figsize =(10, 7))
    plt.pie(data, labels = cars)
    img = io.BytesIO()              # create file-like object in memory to save image without using disk
    plt.savefig(img, format='png')  # save image in file-like object
    img.seek(0)

    return StreamingResponse(content=img, media_type="image/jpeg")
    # return img.seek(0) 




# @app.get("/credentials")
# async def getCred():
#     obj=test.main()
#     return {
#         "status" : "SUCCESS",
#         "array" : obj
#     }
