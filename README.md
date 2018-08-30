# Euroscipy 2018 - Data Visualizations for the web with Altair and Vega(-Lite)

## Prerequisites

* demo notebook: `Python 3.6+`
* example web application: `Python 3.6+` and `Nodejs`

## Installation

Create a virtualenv and do

	pip install -r requirements.txt

## Starting the Notebook

	jupyter lab

## Javascript dependencies

	cd js
	npm install yarn
	yarn
	yarn serve

This will start a dev server on port http://localhost:8080.
(The actual frontend code is in `js/src/App.vue`)

In another shell in the root directory do

	export FLASK_APP=euroscipy_dataviz.web.wsgi
	flask run

Now go to http://localhost:8080
