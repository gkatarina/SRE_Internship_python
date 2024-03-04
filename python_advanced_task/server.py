#!/usr/local/bin/python3

import requests, pizzas, order, fastapi, token
from pydantic import BaseModel
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing_extensions import Annotated


class OrderModel(BaseModel):
    user: str
    pizza: str
    status: bool = False

app = fastapi.FastAPI()

security = HTTPBasic()

@app.get("/")
async def root():
    return {"message": "This is a test!"}
@app.get("/menu")
async def read_menu():
    return pizzas.pizza_menu
@app.post("/order")
async def createOrder(orderModel: OrderModel):
    print(orderModel.user)
    if orderModel.pizza not in pizzas.pizza_menu.values():
        print(orderModel.pizza)
    else:
        newOrder = order.Order(orderModel.user, orderModel.pizza)
        order.appendNewOrder(newOrder)
        # print(newOrder)
        return orderModel
@app.get("/status/{order_id}")
async def getStatus(order_id: str):
    print(order_id)
    myOrder = order.getOrderFromOrdersList(order_id)
    # myOrder = order.getOrderFromOrdersList(order_id)
    statusJson = {"status": myOrder.orderStatus()}
    if myOrder.status == False:
        myOrder.setReadyToBeDelivered()
    return statusJson

@app.delete("/order/{order_id}")
async def deleteIf(order_id: str):
    myOrder = order.getOrderFromOrdersList(order_id)
    if myOrder.status == True:
        return {"message": "Order ready, can't cancel it!"}
    else:
        order.deleteOrderFromList(order_id)
        return {"message": "Order cancelled!"} 


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}