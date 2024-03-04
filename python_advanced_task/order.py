class Order: 
    id = 0
    def __init__(self, orderName, orderedPizza):
        self.orderedPizza = orderedPizza
        self.orderName = orderName
        self.status = False
        Order.id = Order.id + 1
    def setReadyToBeDelivered(self):
        self.status = True
    def isReadyForDelivery(self):
        return self.status
    def getOrderName(self):
        return self.orderName
    def orderStatus(self):
        statusStr = ""
        if self.status == False:
            statusStr = "Not ready"
        else:
            statusStr = "Ready"
        return statusStr
    def __del__(self):
        print("Order deleted!")

orders = {}

def appendNewOrder(order):
    orders[order.getOrderName()] = order
    for (k,v) in orders.items():
        print(k, v.orderName, v.orderedPizza)

def getOrderFromOrdersList(id_str):
    return orders.get(id_str)

def deleteOrderFromList(id_str):
    deleted = orders.pop(id_str)
    del deleted 
