"""
This is a script to track products
"""
import json
def get_products_to_track():

    # load and read json file
    with open("products_to_track.json") as f:
        data = json.loads(f.read())

    # get products list
    products_to_track = []
    for company in data:
        products_to_track += data[company]

    return products_to_track