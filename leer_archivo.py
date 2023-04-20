import boto3
from datetime import datetime
from urllib.request import urlopen


def get_url_tiempo():
    return "https://www.eltiempo.com/"


def get_url_publimetro():
    return "https://www.elespectador.com/"


def get_boto():
    return boto3.client('s3')


def get_date():
    return datetime.today().strftime('%Y-%m-%d')


def get_html(url):
    with urlopen(url) as response:
        html = response.read()
    return html


def f():
    fecha_actual = get_date()
    html_tiempo = get_html(get_url_tiempo())
    html_publimetro = get_html(get_url_publimetro())
    s3 = get_boto()
    s3.put_object(Body=html_tiempo,
                  Bucket='',
                  Key="eltiempo-"+str(fecha_actual)+".html")
    s3.put_object(Body=html_publimetro,
                  Bucket='',
                  Key="publimetro-"+str(fecha_actual)+".html")
    return "hola"
