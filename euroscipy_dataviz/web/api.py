from flask import Blueprint, current_app, jsonify, request

from euroscipy_dataviz.prediction_plot import generate_plot


api = Blueprint("api", __name__, url_prefix="/api")


@api.after_request
def add_cors_header(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@api.route("/stores")
def available_stores():
    """
    Return a list of stores that can be used by the frontend to query data per store.
    
    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Vary: Accept
       Content-Type: application/json

       [
           {
               "id": "1000",
               "name": "Karlsruhe"
           },
           {
               "id": "1001",
               "name": "Trento"
           }
       ]

    """
    stores = current_app.plot_data.drop_duplicates(["store_id"])[
        ["store_id", "store_name"]
    ]
    return jsonify(stores.to_dict(orient="records"))


@api.route("/products")
def available_products():
    """
    Returns a list of products that can be used by the frontend to query data.
    
    **Example response**:

    .. sourcecode:: http

       HTTP/1.1 200 OK
       Vary: Accept
       Content-Type: application/json

       [
           {
               "product_id": "1000",
               "product_name": "Banana"
           },
           {
               "product_id": "1001",
               "product_name": "Apple"
           }
       ]

    """
    products = current_app.plot_data.drop_duplicates(["product_id"])[
        ["product_id", "product_name"]
    ]
    return jsonify(products.to_dict(orient="records"))


@api.route("/plot")
def get_plot():
    params = request.args
    df = current_app.plot_data
    store = params["store"]
    product = params["product"]
    date_from = params["from"]
    date_to = params["to"]
    qry = (
        f"store_id=='{store}' and product_id=='{product}' and "
        f"date >= '{date_from}' and date <= '{date_to}'"
    )
    df = df.query(qry)
    chart = generate_plot(df)
    return jsonify(chart.to_dict())
