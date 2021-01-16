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
        parser.add_argument('I_Revenue[0]', required=True)
        parser.add_argument('I_VariableCost[0]', required=True)
        parser.add_argument('I_Revenue[1]', required=True)
        parser.add_argument('I_VariableCost[1]', required=True)
        parser.add_argument('I_Revenue[2]')
        parser.add_argument('I_VariableCost[2]')
        parser.add_argument('I_Revenue[3]')
        parser.add_argument('I_VariableCost[3]')
        parser.add_argument('I_Revenue[4]')
        parser.add_argument('I_VariableCost[4]')
        parser.add_argument('I_Revenue[5]')
        parser.add_argument('I_VariableCost[5]')
        parser.add_argument('I_Revenue[6]')
        parser.add_argument('I_VariableCost[6]')
        parser.add_argument('I_Revenue[7]')
        parser.add_argument('I_VariableCost[7]')
        parser.add_argument('I_Revenue[8]')
        parser.add_argument('I_VariableCost[8]')
        parser.add_argument('I_Revenue[9]')
        parser.add_argument('I_VariableCost[9]')
        parser.add_argument('I_Revenue[10]')
        parser.add_argument('I_VariableCost[10]')
        parser.add_argument('I_Revenue[11]')
        parser.add_argument('I_VariableCost[11]')
        parser.add_argument('I_Revenue[12]')
        parser.add_argument('I_VariableCost[12]')
        parser.add_argument('I_Revenue[13]')
        parser.add_argument('I_VariableCost[13]')
        parser.add_argument('I_Revenue[14]')
        parser.add_argument('I_VariableCost[14]')
        parser.add_argument('I_Revenue[15]')
        parser.add_argument('I_VariableCost[15]')
        parser.add_argument('I_Revenue[16]')
        parser.add_argument('I_VariableCost[16]')
        parser.add_argument('I_Revenue[17]')
        parser.add_argument('I_VariableCost[17]')
        parser.add_argument('I_Revenue[18]')
        parser.add_argument('I_VariableCost[18]')
        parser.add_argument('I_Revenue[19]')
        parser.add_argument('I_VariableCost[19]')
        
        args = parser.parse_args()  # parse arguments to dictionary

        I_YearlyFinancialEntries = []
        I_YearlyFinancialEntries.append(args['I_Revenue[0]'])
        I_YearlyFinancialEntries.append(args['I_VariableCost[0]'])
        I_YearlyFinancialEntries.append(args['I_Revenue[1]'])
        I_YearlyFinancialEntries.append(args['I_VariableCost[1]'])

        if args['I_Revenue[2]'] is not None and args['I_VariableCost[2]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[2]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[2]'])

        if args['I_Revenue[3]'] is not None and args['I_VariableCost[3]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[3]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[3]'])

        if args['I_Revenue[4]'] is not None and args['I_VariableCost[4]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[4]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[4]'])

        if args['I_Revenue[5]'] is not None and args['I_VariableCost[5]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[5]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[5]'])

        if args['I_Revenue[6]'] is not None and args['I_VariableCost[6]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[6]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[6]'])

        if args['I_Revenue[7]'] is not None and args['I_VariableCost[7]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[7]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[7]'])

        if args['I_Revenue[8]'] is not None and args['I_VariableCost[8]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[8]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[8]'])

        if args['I_Revenue[9]'] is not None and args['I_VariableCost[9]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[9]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[9]'])

        if args['I_Revenue[10]'] is not None and args['I_VariableCost[10]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[10]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[10]'])

        if args['I_Revenue[11]'] is not None and args['I_VariableCost[11]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[11]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[11]'])

        if args['I_Revenue[12]'] is not None and args['I_VariableCost[12]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[12]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[12]'])

        if args['I_Revenue[13]'] is not None and args['I_VariableCost[13]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[13]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[13]'])

        if args['I_Revenue[14]'] is not None and args['I_VariableCost[14]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[14]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[14]'])

        if args['I_Revenue[15]'] is not None and args['I_VariableCost[15]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[15]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[15]'])

        if args['I_Revenue[16]'] is not None and args['I_VariableCost[16]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[16]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[16]'])

        if args['I_Revenue[17]'] is not None and args['I_VariableCost[17]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[17]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[17]'])

        if args['I_Revenue[18]'] is not None and args['I_VariableCost[18]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[18]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[18]'])

        if args['I_Revenue[19]'] is not None and args['I_VariableCost[19]'] is not None:
            I_YearlyFinancialEntries.append(args['I_Revenue[19]'])
            I_YearlyFinancialEntries.append(args['I_VariableCost[19]'])


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
