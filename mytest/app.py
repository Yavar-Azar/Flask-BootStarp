import dash
import flask

app = dash.Dash(__name__)
app.layout = [
   # ... some  dash_core_components ...
   dcc.Graph(id='mygraph'),
]
server = app.server

@server.route('/post_data', methods=['GET', 'POST'])
def post_data():
    if request.method == 'POST':
        data = eval(request.data.decode('utf8'))


@app.callback(
    [Output('mygraph', 'figure')],
    [Input('mydropdown1', 'value'), ...],
)
def update_mygraph(mydropdown1_value, ...):
    # QUESTION: how to get data from post_data?
    # some elaboration on data based on dropdown values
    fig = px.scatter(data, x="x", y="y")
    return fig


if __name__ == '__main__':
    app.run_server()
