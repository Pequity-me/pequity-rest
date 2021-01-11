from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse
import ast
import time
from valuation_service import run_valuation
app = Flask(__name__)
api = Api(app)




class ValuationCalculator(Resource):

    def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('Email', required=False)  # add arguments
        parser.add_argument('Name', required=False)
        parser.add_argument('I_Country', required=True)
        parser.add_argument('I_Industry', required=True)
        parser.add_argument('I_Debt', required=True)
        parser.add_argument('I_NonCashAssets', required=True)
        parser.add_argument('I_Cash', required=True)
        parser.add_argument('I_YearlyFixedCost', required=True)
        parser.add_argument('I_Revenue', required=True, action='append')
        parser.add_argument('I_Cashflow', required=True, action='append')
        args = parser.parse_args()  # parse arguments to dictionary

        I_YearlyFinancialEntries = [None]*(len(args['I_Revenue'])+len(args['I_Cashflow']))
        I_YearlyFinancialEntries[::2] = args['I_Revenue']
        I_YearlyFinancialEntries[1::2] = args['I_Cashflow']
        # create new dataframe containing new values
        new_data_dict = {
            'Timestamp' : str(int(time.time())),
            'Email': args['Email'],
            'Name': args['Name'],
            'I_Country' : args['I_Country'],
            'I_Industry' : args['I_Industry'],
            'I_Debt': int(args['I_Debt']),
            'I_NonCashAssets': int(args['I_NonCashAssets']),
            'I_Cash': int(args['I_Cash']),
            'I_YearlyFixedCost': int(args['I_YearlyFixedCost']),
            'I_YearlyFinancialEntries': [ int(numeric_string) for numeric_string in I_YearlyFinancialEntries ]
        }

        low,high,rev,var_cost,cashflow,period,err = run_valuation(new_data_dict)
        rev = list(rev[0])
        var_cost =list(var_cost[0])
        cashflow =list(cashflow[0])
        return jsonify({'O_EnterpriseValueLow':low,'O_EnterpriseValueHigh':high,
                        'O_ProjectedRevenueSeries':rev, 'O_ProjectedVariableCostSeries':var_cost,'O_ProjectedCashFlowSeries':cashflow,
                        'O_PlotPeriod':period, 'O_ErrorCode':err
                        })  # return data with 200 OK

api.add_resource(ValuationCalculator, '/valcalc')  # '/valcalc' is our entry point

if __name__ == '__main__':
     app.run()
