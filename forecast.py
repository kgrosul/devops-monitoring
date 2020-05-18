import requests
import graphyte


from config import API, GRAPHITE, METRICS, PARAMS


def get_forecast():
    request = "{}/{}".format(API, "forecast")
    response = requests.get(request, PARAMS).json()
    return {metric: response['list'][0]['main'][metric] for metric in METRICS}


def send_forecast(forecast):
    sender = graphyte.Sender(GRAPHITE, prefix='weather')
    for (metric, value) in forecast.items():
        metric_name = "forecast.{}".format(metric)
        print(metric_name, value)
        sender.send(metric_name, value)


def main():
    send_forecast(get_forecast())


if __name__ == '__main__':
    main()