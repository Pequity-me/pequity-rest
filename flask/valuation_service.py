import logging
import oct2py
from oct2py import octave


def run_valuation(args):    
    oc = oct2py.Oct2Py()
    oc.addpath('./PequityIntrinsicValuation')
    logging.debug(args)
    value_low,value_high = oc.RunValuation( args['I_Industry'],
                                            int(args['I_ValueofDebt']),
                                            int(args['I_ValueofEquity']),
                                            int(args['I_ValueofAssets']),
                                            int(args['I_ValueofCash']),
                                            int(args['I_TTMRevenue']),
                                            int(args['I_T_1YearRevenue']),
                                            int(args['I_T_2YearRevenue']),
                                            int(args['I_FixedCost']),
                                            int(args['I_TTMVariableCost']),
                                            int(args['I_T_1YearVariableCost']),
                                            int(args['I_T_2YearVariableCost']),
                                            verbose=True, nout=2
                                            )
    oc.exit()
    return value_low,value_high

if __name__ == '__main__':
    #basic test case
    res = run_valuation({
                    'I_Industry': 'Advertising',
                    'I_ValueofDebt': 300000,
                    'I_ValueofEquity': 1000000,
                    'I_ValueofAssets':200000,
                    'I_ValueofCash':50000,
                    'I_TTMRevenue':100000,
                    'I_T_1YearRevenue':120000,
                    'I_T_2YearRevenue':150000,
                    'I_FixedCost':50000,
                    'I_TTMVariableCost':30000,
                    'I_T_1YearVariableCost':40000,
                    'I_T_2YearVariableCost':50000
     })
    print(res)       
