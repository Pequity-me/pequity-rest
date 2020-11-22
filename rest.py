from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import time
from valuation_service import run_valuation
app = Flask(__name__)
api = Api(app)
db = 'companies.csv'




class Companies(Resource):
    def get(self):
        data = pd.read_csv(db)  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code
    
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('Email', required=True)  # add arguments
        parser.add_argument('Name', required=True)
        parser.add_argument('I_Industry', required=True)
        parser.add_argument('I_ValueofDebt', required=True)
        parser.add_argument('I_ValueofEquity', required=True)
        parser.add_argument('I_ValueofAssets', required=True)
        parser.add_argument('I_ValueofCash', required=True)
        parser.add_argument('I_TTMRevenue', required=True)
        parser.add_argument('I_T_1YearRevenue', required=True)
        parser.add_argument('I_T_2YearRevenue', required=True)
        parser.add_argument('I_FixedCost', required=True)
        parser.add_argument('I_TTMVariableCost', required=True)
        parser.add_argument('I_T_1YearVariableCost', required=True)
        parser.add_argument('I_T_2YearVariableCost', required=True)
        args = parser.parse_args()  # parse arguments to dictionary


        # create new dataframe containing new values
        new_data_dict = {
            'Timestamp' : str(int(time.time())),
            'Email': args['Email'],
            'Name': args['Name'],
            'I_Industry' : args['I_Industry'],
            'I_ValueofDebt': args['I_ValueofDebt'],
            'I_ValueofEquity': args['I_ValueofEquity'],
            'I_ValueofAssets': args['I_ValueofAssets'],
            'I_ValueofCash': args['I_ValueofCash'],
            'I_TTMRevenue': args['I_TTMRevenue'],
            'I_T_1YearRevenue': args['I_T_1YearRevenue'],
            'I_T_2YearRevenue': args['I_T_2YearRevenue'],
            'I_FixedCost': args['I_FixedCost'],
            'I_TTMVariableCost': args['I_TTMVariableCost'],
            'I_T_1YearVariableCost': args['I_T_1YearVariableCost'],
            'I_T_2YearVariableCost': args['I_T_2YearVariableCost'],
            'O_EnterpriseValueLow':'',
            'O_EnterpriseValueHigh':''
        }

        low,high = run_valuation(new_data_dict)
        new_data_dict['O_EnterpriseValueLow'] = low
        new_data_dict['O_EnterpriseValueHigh'] = high
        # read our CSV
        data = pd.read_csv(db)
        # add the newly provided values
        new_data = pd.DataFrame(new_data_dict , index=[0] )
        data = data.append(new_data, ignore_index=True)
        # save back to CSV
        data.to_csv(db, index=False)
        return {'data': {'O_EnterpriseValueLow':low,'O_EnterpriseValueHigh':high}}, 200  # return data with 200 OK

        args = parser.parse_args()  # parse arguments to dictionary

api.add_resource(Companies, '/companies')  # '/companies' is our entry point

if __name__ == '__main__':
     app.run(port='5002')
