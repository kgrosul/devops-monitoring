import requests
import graphyte


from config import API, GRAPHITE, METRICS, PARAMS


def get_weather():
    request = "{}/{}".format(API, "weather")
    response = requests.get(request, PARAMS).json()
    return {metric: response['main'][metric] for metric in METRICS}


def send_weather(weather):
    sender = graphyte.Sender(GRAPHITE, prefix='weather')
    for (metric, value) in weather.items():
        metric_name = "real.{}".format(metric)
        print(metric_name, value)
        sender.send(metric_name, value)


def main():
    send_weather(get_weather())


if __name__ == '__main__':
    main()
