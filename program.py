from investpy.indices import get_index_historical_data as ge


df = ge('PHLX Swiss Franc', 'united states',
        from_date='01/01/2018', to_date='01/01/2019')
print(df.head())
