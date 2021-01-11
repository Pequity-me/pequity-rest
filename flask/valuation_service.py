import logging
import oct2py
from oct2py import octave


def run_valuation(args):    
    oc = oct2py.Oct2Py()
    oc.addpath('./PequityIntrinsicValuation')
    print(args)
    value_low,value_high,projected_revenue_series,projected_variable_cost_series,projected_cashflow_series, plot_period,error_code = oc.RunValuation( 
                                            args['I_Country'],
                                            args['I_Industry'],
                                            args['I_Debt'],
                                            args['I_NonCashAssets'],
                                            args['I_Cash'],
                                            args['I_YearlyFixedCost'],
                                            args['I_YearlyFinancialEntries'],
                                            verbose=True, nout=7
                                            )
    oc.exit()
    return value_low,value_high,projected_revenue_series,projected_variable_cost_series,projected_cashflow_series,plot_period,error_code

if __name__ == '__main__':
    #basic test case
    res = run_valuation({
                    'I_Country' : 'Egypt',
                    'I_Industry': 'Advertising',
                    'I_Debt': 200000,
                    'I_NonCashAssets':100000,
                    'I_Cash':200000,
                    'I_YearlyFixedCost':100000,
                    'I_YearlyFinancialEntries': [150000, 35000, 120000, 30000, 100000, 20000, 70000, 15000, 50000, 12000]
     })
    print(res)       
