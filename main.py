import pickle
import pydantic
import numpy as np
from fastapi import FastAPI
app = FastAPI()
model = pickle.load(open('model.pkl', 'rb'))
t = [297.7,	308.5,	1373.0,	56.7,203.0,	0.0	,1.0]

class Input_Data(pydantic.BaseModel):
    air_temperature: float
    process_tempature: float
    rotational_speed: float
    torque_nm: float
    tool_wear_min: float
    type_ : str


@app.get("/")
def read_root():
    return "to predict add predict to the end of the url"

@app.post("/predict")
def predict(data: Input_Data):
    en1=0
    en2=0
    if data.type_=='H':
        en1=1.0
        en2=0.0
    if data.type_=='L':
        en1=0.0
        en2=1.0
    print(model.predict([t]))
    # lst = np.array([data.air_temperature, data.process_tempature, data.rotational_speed, data.torque_nm, data.tool_wear_min, en1, en2])
    lst = [data.air_temperature, data.process_tempature, data.rotational_speed, data.torque_nm, data.tool_wear_min, en1, en2]
    # print(lst)
    # print(type(lst))
    # print(type(t))
    # return model.predict(lst)
    return f"{model.predict([lst])}"