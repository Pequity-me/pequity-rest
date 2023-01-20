
# pequity-rest

A python REST API for [pequity valuation matlab model](https://github.com/Pequity-me/PequityIntrinsicValuation)

# installation and execution

## Installation of the service 

To build the service containers and bring them up
```
docker-compose build
docker-compose up
```

## Misc

To view a container logs
```
docker logs --since=1h <container_id>
```

To delete dangling containers
```
docker image ls -f dangling=true
docker image rm $(docker image ls -f dangling=true -q)
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

<http://localhost/valcalc?I_Industry=Advertising&I_Country=Egypt&I_Debt=200000&I_NonCashAssets=100000&I_Cash=200000&I_YearlyFixedCost=100000&I_Revenue[0]=150000&I_VariableCost[0]=35000&I_Revenue[1]=120000&I_VariableCost[1]=30000&I_Revenue[2]=100000&I_VariableCost[2]=20000&I_Revenue[3]=70000&I_VariableCost[3]=15000&I_Revenue[4]=50000&I_VariableCost[4]=12000>
