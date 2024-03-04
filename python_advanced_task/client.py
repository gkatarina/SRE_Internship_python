#!/usr/local/bin/python3

import argparse, requests, getpass

def checkStatusCode(requests):
    if requests.status_code != 200:
        raise(requests.raise_for_status())
    

url = "http://localhost:8000/"
# print(url)
parser = argparse.ArgumentParser(description='Order a pizza')

parser.add_argument('--menu', '-m', action= 'store_true', help='Displays the menu to the end user')
parser.add_argument('--order', '-o', nargs='+', action='store', help='Creates an order from the user')
parser.add_argument('--status', '-s', action='store', help='Checks the status of the order')
parser.add_argument('--cancel', '-c', action='store', help='User can cancel the order if the pizza is not made yet') 
parser.add_argument('--add', '-a',  help='Admin: add a new pizza to the menu')
parser.add_argument('--delete', '-d', help='Admin: delete the pizza from the menu')
parser.add_argument('--cancel_admin', '-u', help='Admin: cancel the order regardless of status')

args = parser.parse_args() #returns a namespace or an actual action if it exists

try:
    if args.menu == True:
        # for pizza in pizzas.pizza_menu:
        #     print(pizza)
        url += "menu"
        r = requests.get(url)
        checkStatusCode(requests=r)
        for key in r.json():
            print(r.json()[key]) 
    if args.order:
            url += "order"
            query = {"user" : args.order[0], "pizza" : args.order[1]}
            r = requests.post(url, json=query)
            checkStatusCode(requests=r)
            if r.json() == None:
                print("Pizza doesn't exist in the menu. Try again..")
            # print(args.order[0])
            # # newOrder = order.Order(args.order)
            # print(newOrder.orderedPizza)
            #request ka serveru...
    if args.status:
        url += "status/" + args.status
        r = requests.get(url)
        checkStatusCode(requests=r)
        for key in r.json():
            print(r.json()[key])
    if args.cancel: 
        url += "order/" + args.cancel
        response = requests.delete(url)
        # checkStatusCode(requests=response)
        for k in response.json():
            print(response.json()[k])
    if args.add:
        url += 'users/me'
        password = getpass.getpass('Password: ')
        data = {'key': args.add[0]}
        response = requests.get(url, auth=('username', password))
        for k in response.json():
            print(response.json()[k])
    if args.delete: 
        url += 'users/me'
        password = getpass.getpass('Password: ')
        data = {'key': args.delete[0]}
        response = requests.get(url, auth=('username', password))
        for k in response.json():
            print(response.json()[k])
    if args.cancel_admin:
        url += 'users/me'
        password = getpass.getpass('Password: ')
        data = {'key': args.cancel_admin[0]}
        response = requests.get(url, auth=('username', password))
        for k in response.json():
            print(response.json()[k])
except requests.exceptions.HTTPError as e:
    print("Error" + str(e))