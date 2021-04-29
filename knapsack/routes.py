from flask import render_template



@app.route("/", methods=['POST', 'GET'])
def index():
    render_template('index.html')

@app.route("/value", methods=['POST'])
def value():
    if form.validate_on_submit():
        crossover_rate = form.crossover.data
        mutation_rate = form.mutation.data
        