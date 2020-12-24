
# pequity-rest

REST API for pequity

# installation and execution

## Installation of the service 

To build the service containers and bring them up
```
docker-compose build
docker-compose up
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

<http://127.0.0.1:5002/companies>

<http://127.0.0.1:5002/companies?Name=Ahmed&Email=a@a.b&I_Industry=Advertising&I_ValueofDebt=300000&I_ValueofEquity=1000000&I_ValueofAssets=200000&I_ValueofCash=50000&I_TTMRevenue=100000&I_T_1YearRevenue=120000&I_T_2YearRevenue=150000&I_FixedCost=50000&I_TTMVariableCost=30000&I_T_1YearVariableCost=40000&I_T_2YearVariableCost=50000>
