from flask import Flask, render_template

from euroscipy_dataviz.prediction_plot import load_predictions


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    # NOTE: for this example application we only have a small amount of data so
    # we can load it into memory on service start
    app.plot_data = load_predictions()

    from euroscipy_dataviz.web.api import api

    app.register_blueprint(api)

    return app
