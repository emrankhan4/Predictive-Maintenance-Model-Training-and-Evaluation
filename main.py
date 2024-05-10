import pickle
from fastapi import FastAPI
app = FastAPI()
model = pickle.load(open('model.pkl', 'rb'))
t = [297.7,	308.5,	1373.0,	56.7,	203.0,	0.0	,1.0]


