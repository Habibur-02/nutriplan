import pandas as pd

def load_nutrition_data(path="data/nutrition.xlsx"):
    
    df = pd.read_excel(path)

    
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    
    if 'saturated_fat' in df.columns:
        df['saturated_fat'].fillna(0, inplace=True)

    
    object_columns = df.select_dtypes(include=['object']).columns.tolist()
    if object_columns:
        food_col = object_columns[0]
        object_columns = object_columns[1:]  

    
    def clean_value(x):
        if isinstance(x, str):
            return (
                x.replace('mg', '')
                 .replace('mcg', '')
                 .replace('mc', '')
                 .replace('IU', '')
                 .replace('g', '')
                 .strip()
            )
        return x

    
    for col in object_columns:
        df[col] = df[col].apply(clean_value)
        df[col] = pd.to_numeric(df[col], errors='coerce')  

    
    for col in ['vitamin_a', 'vitamin_d']:
        if col in df.columns:
            df[col] = df[col].apply(clean_value)
            df[col] = pd.to_numeric(df[col], errors='coerce')

   
    for col in df.columns:
        if col != 'name':  
            df[col].fillna(0, inplace=True)

    return df
