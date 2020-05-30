import json
import pandas as pd
import sys, getopt



def test (input_file,output_file):
    print ("Input File: ", input_file)
    print ("Input File: ", output_file)
    df = pd.read_json (input_file,orient = "split")
    
    # Removing Null Values
    df = df.dropna()
    
    #Converting Tenor and Yield to Float for calculation
    new = df["tenor"].str.split(" ", n = 1, expand = True) 
    new_yield = df["yield"].str.split("%", n = 1, expand = True) 
    df["yield"] = new_yield[0].astype("float")
    df["tenor"] = new[0].astype("float")
    
    #Spliting the dataset by type 
    corporate_df = df.loc[df["type"] == "corporate",:]
    goverment_df = df.loc[df["type"] == "government",:]
    
    # Iterating Corporate Dataframe to find the nearest goverment bond in terms of tenure
    for index, row in corporate_df.iterrows():
        temp_df = pd.DataFrame()
        temp_df = goverment_df.copy().reset_index()
        temp_df["difference"] = temp_df["tenor"] - row["tenor"]
        temp_df["difference"] = temp_df["difference"].abs()
        
        min_diff = pd.DataFrame()
        min_diff = temp_df.loc[temp_df["difference"] == temp_df["difference"].min(),:]
        if len(min_diff) > 1:
            max_amount_outstanding = min_diff["amount_outstanding"].max()
            min_diff = min_diff.loc[min_diff["amount_outstanding"] == max_amount_outstanding,:]
            
        min_diff.loc[0,"corporate_id"] = row["id"]
        min_diff.loc[0,"corporate_type"] = row["type"]
        min_diff.loc[0,"corporate_tenor"] = row["tenor"]
        min_diff.loc[0,"corporate_yield"] = row["yield"]
        min_diff.loc[0,"corporate_amount_outstanding"] = row["amount_outstanding"]
        
    
    # Find the difference in yield of government bonds and corporate bonds    
    min_diff.loc[:,"yield_difference"] = min_diff["corporate_yield"] - min_diff["yield"]
    final_df = min_diff[["id","corporate_id","yield_difference"]]
    final_df.loc[:,"yield_difference"] = final_df["yield_difference"]*100
    
    # Formatting output
    final_df.columns = ["government_bond_id","corporate_bond_id","spread_to_benchmark"]
    #print (final_df["spread_to_benchmark"])
    final_df.loc[:,"spread_to_benchmark"] = final_df["spread_to_benchmark"].astype("int")
    final_df.loc[:,"spread_to_benchmark"] = final_df["spread_to_benchmark"].astype("str") + " bps"
    out_list = final_df.to_dict('records')
    out = {}
    out["data"] = out_list
    with open(output_file, 'w') as fp:
        json.dump(out, fp)
    return out


if __name__ == "__main__":
   temp = test(sys.argv[1],sys.argv[2])