import boto3
from datetime import datetime
from bs4 import BeautifulSoup


def f():
    nombre = str(datetime.today().strftime('%Y-%m-%d'))
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('')
    
    obj_tiempo = bucket.Object(str("eltiempo-" + nombre + ".html"))
    body_tiempo = obj_tiempo.get()['Body'].read()
    
    obj_publimetro = bucket.Object(str("publimetro-" + nombre + ".html"))
    body_publimetro = obj_publimetro.get()['Body'].read()
    
    html_tiempo = BeautifulSoup(body_tiempo, 'html.parser')
    html_publimetro = BeautifulSoup(body_publimetro, 'html.parser')
    
    data_noticias_tiempo = html_tiempo.find_all('article')
    data_noticias_publimetro = html_publimetro.find_all('article')
    
    fecha_actual = datetime.today().strftime('%Y-%m-%d')
    linea_0 = "Name, Category, Link\n"
    for i in range(len(data_noticias_tiempo)):
        link = "eltiempo.com"+data_noticias_tiempo[i].find('a', class_='title page-link')['href']
        name = data_noticias_tiempo[i]['data-name'].replace(",","") 
        category = data_noticias_tiempo[i]['data-seccion']
        csv_tiempo = linea_0 + name + "," + \
            category + "," + \
            link + \
            "\n"
    for i in range(len(data_noticias_publimetro)):
        link = "publimetro.co" + data_noticias_publimetro[i].find('a')['href']
        name = (data_noticias_publimetro[i].find('a').text).replace(",","")
        category = link.split('/')[i]
        csv_publimetro = linea_0 + name + "," + \
            category + "," + \
            link + \
            "\n"
            
    boto3.client('s3').put_object(Body=linea_0, Bucket='casas-fina-20020503',
                                  Key=str(nombre+".csv"))
    boto3.client('s3').put_object(Body=linea_0, Bucket='casas-fina-20020503',
                                  Key=str(nombre+".csv"))
