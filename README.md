# Amazon SP API (orders) to Google Sheets with Python
With the world taking a frog leap into the eCommerce world, more and more people start selling their products on Amazon. However, once you start hitting the mass scale and you have orders coming every minute, it can be hard to get a grasp of all the data. The basic Amazon dashboards are limited, and you will soon find yourself using proprietary tools charging hefty monthly subscriptions. In this video, I will show you how easy it is to integrate Amazon SP API (old Amazon MWS) with Google Sheets and collect data of your orders daily. We will use the Python programming language with some 3rd party libraries.

![miniatura7_Obszar roboczy 1-min](https://user-images.githubusercontent.com/32365708/125775369-b1a9fc4b-577b-4065-8fe1-3ca2428f2f82.png)

## YouTube link:
https://youtu.be/bHBFElmWRNg


## Watch full tutorial here
...

## Create .env and get client_secret.json from GCP
.env example
```buildoutcfg
REFRESH_TOKEN=Atzr|IwEBINTLp**********
LWA_APP_ID=amzn1.application-oa2-client.8c42******
CLIENT_SECRET=3483932*************************
AWS_ACCESS_KEY=AKIA***********
AWS_SECRET_KEY=M9aYP********************
ROLE_ARN=arn:aws:iam::957*******:role/******

GOOGLE_SHEETS_EMAIL=***********.iam.gserviceaccount.com
GOOGLE_SHEETS_ID=1bSoTWrE*******************
GOOGLE_WORKSHEET_NAME=*********
```

## Setup Python Virtual Environment
```buildoutcfg
pipenv install
pipenv shell
```
## Running Script

```buildoutcfg
python script.py
```

