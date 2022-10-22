class my_functions(object):
    
    ## Function designed for changes dataset for the heat waves data
     def split_state_city(changes_df):
        #Step 1 - Split concatenated variable
        code = changes_df["Station"].str.split('_',expand=True)
        code.iloc[[15,16,22,23,29,31,40,41,42,43,44,46],1]=code.iloc[[15,16,22,23,29,31,40,41,42,43,44,46],2]
        code.iloc[[40],1] = code.iloc[[40],3]
        
        #Step 2 - Create new variables with city and state 
        changes_df["State"] = code[1]
        changes_df["Location"] = changes_df["Station"]

        #Step 3 - Select variables to include
        cols =['State','Location','Latitude','Longitude','Frequency Change','Duration Change','Season Change',
                'Intensity Change']
        changes_df=changes_df[cols]
        return changes_df