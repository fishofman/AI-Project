import pandas

def get_tax():
    tax_data = pandas.read_csv("2024_sales_tax.csv",index_col='state')

    #get the users desire state
    name = input('What state are you in? ').upper()
    try:
        state = tax_data.loc[name] 
    except:
        print("ERROR: state invalid")
        exit()

    #get the users desired mode
    mode = input("Max or Avg? ").upper()
    if(mode == 'MAX'):
        tax = state['max_combined_rate']
    elif(mode == 'AVG'):
        tax = state['avg_combined_rate']
    else:
        print("ERROR: mode invalid")
        exit()

    return tax