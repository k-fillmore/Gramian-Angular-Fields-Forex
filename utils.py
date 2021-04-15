def select_df(df, window_size):
    dfList = []
    for row in df.itertuples():
        chart_size = row[0] - window_size
        graphDf = df.iloc[chart_size:row[0]]
        if graphDf.shape[0] != window_size:
            pass
        if graphDf.shape[0] == window_size:
            dfList.append(graphDf)
    return dfList
