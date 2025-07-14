def get_years(start_col, end_col):
    min_start = start_col.min()
    max_end = end_col.max()
    return (int(min_start), int(max_end))

def replace_semicolon_with_linebreak(input_dataframe):
    '''Replace semicolon with linebreak in every element of the dataframe
    that is a string'''
    for col in input_dataframe.columns:
        if input_dataframe[col].dtype == 'object':
            input_dataframe[col] = input_dataframe[col].replace(';', '<br>', regex=True)
    return input_dataframe

def make_html_table_from_dataframe(input_dataframe):
    '''Make an html table from a dataframe'''
    # if len(input_dataframe.columns) > 3:
    #     input_dataframe = wrap_dataframe_column_values(
    #         replace_semicolon_with_linebreak(input_dataframe))
    # else:
    #     input_dataframe = replace_semicolon_with_linebreak(input_dataframe)
    input_dataframe = replace_semicolon_with_linebreak(input_dataframe)
    # # We name the axis and reset the index so that it appears in the table as a column
    input_dataframe.index.name = ''
    input_dataframe.reset_index(inplace=True)
    # input_dataframe = input_dataframe.to_html(index=False, escape=False)
    output = f"""
    <html>
    <head>
    <style> 
      table, th, td {{font-size:11pt; border:1px solid black; border-collapse:collapse; text-align:justify; 
      vertical-align:top; background-color: #ecf7f1; color: black;}}
      th, td {{padding: 5px;}}
      th {{background-color: #9cd1b4;}}
      tr td:first-child {{font-weight: bold;}}
    </style>
    </head>
    <body>
    {input_dataframe.to_html(index=False, escape=False)}
    </body>
    </html>
    """
    return output


def get_all_column_values(col):
    '''Get all unique values in a column'''
    if col.dtype == 'object':
        return col.unique().tolist()
    else:
        return col.dropna().unique().tolist()