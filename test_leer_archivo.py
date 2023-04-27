import boto3
from datetime import datetime
from leer_archivo import get_url_tiempo, get_boto, get_date, get_url_publimetro


def test_get_boto(mocker):
    mocker.patch("boto3.client")
    s3_mock = mocker.MagicMock()
    boto3.client.return_value = s3_mock
    s3 = get_boto()
    assert s3 == s3_mock


def test_get_date():
    dt = get_date()
    assert dt == datetime.today().strftime('%Y-%m-%d')


def test_get_url_tiempo():
    assert get_url_tiempo() == "https://www.eltiempo.com/"


def test_get_url_publimetro():
    assert get_url_publimetro() == "https://www.publimetro.co/"