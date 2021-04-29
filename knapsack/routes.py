from flask import render_template
from knapsack.app import app
from knapsack.source.output import crossover_rate, mutation_rate
from knapsack.source import InputData as ip


@app.route("/", methods=['POST', 'GET'])
def index():
    if form.validate_on_submit():
        ipcrossover_rate = form.crossover.data
        ip.mutation_rate = form.mutation.data
        ip.max_value = form.max_value.data
        ip.min_value = form.min_value.data
    return render_template("index.html")

@app.route("/value", methods=['POST'])
def value():
    if form.validate_on_submit():
        crossover_rate = form.crossover.data
        mutation_rate = form.mutation.data
        