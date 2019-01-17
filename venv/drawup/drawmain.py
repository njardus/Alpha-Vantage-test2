import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot


def drawtest(df, ticker):
    # Creating Close
    close = go.Scatter(
        x=df.index.values,
        y=df["Close"],
        mode="lines",
        name="Close",
        marker=dict(color='rgba(16, 112, 2, 0.8)'), # Green
        text=df.index.values)

    # Creating SMA15
    sma015 = go.Scatter(
        x=df.index.values,
        y=df["SMA015"],
        mode="lines",
        name="SMA 15",
        marker=dict(color='rgba(200, 0, 0, 0.8)'), # Red
        text=df.index.values)

    # Creating SMA50
    sma050 = go.Scatter(
        x=df.index.values,
        y=df["SMA050"],
        mode="lines",
        name="SMA 50",
        marker=dict(color='rgba(80, 26, 80, 0.8)'),  # Purple
        text=df.index.values)

    # Creating SMA200
    sma200 = go.Scatter(
        x=df.index.values,
        y=df["SMA200"],
        mode="lines",
        name="SMA 200",
        marker=dict(color='rgba(0, 0, 200, 0.8)'),  # Blue
        text=df.index.values)

    data = [close, sma015, sma050, sma200]
    layout = dict(title=ticker,
                  xaxis=dict(title='yyyyyy', ticklen=5, zeroline= False)
                  )

    file = "..\plots\close." + ticker + ".html"

    fig = dict(data=data, layout=layout)
    plot(fig, filename=file)

