
# pequity-rest

REST API for pequity

# installation and execution

## Installation of the service 

To build the service containers and bring them up
```
docker-compose build
docker-compose up
```

To view a container logs
```
docker logs --since=1h <container_id>
```

## To just try the API locally 
Create the virtual env and install dep

```
python3 -m venv ./venv
pip3 install -r requirements.txt
```

Activate it and execute the service

```
source venv/bin/activate
python3 rest.py
```

# samples generated with postman

<http://127.0.0.1:5000/valcalc?Name=Ahmed&Email=a@a.b&I_Industry=Advertising&I_Country=Egypt&I_Debt=200000&I_NonCashAssets=100000&I_Cash=200000&I_YearlyFixedCost=100000&I_Revenue=150000&I_Cashflow=35000&I_Revenue=120000&I_Cashflow=30000&I_Revenue=100000&I_Cashflow=20000&I_Revenue=70000&I_Cashflow=15000&I_Revenue=50000&I_Cashflow=12000>
