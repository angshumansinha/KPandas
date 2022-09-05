import pandas as pd
class kpandas:
    def __init__(self):
        pass
    def sort_values(self,column_list,dataframe,action):
        if action=="ascending":
            df=pd.DataFrame(dataframe)
            df.sort_values(by=column_list,ascending=True,inplace=True)
            return df
        elif action=="descending":
            df=pd.DataFrame(dataframe)
            df.sort_values(by=column_list,ascending=False,inplace=True)
            return df
        else:
            print("Please read the docs carefully madam")
