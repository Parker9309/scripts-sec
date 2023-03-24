import pandas as pd

# Carregar os logs JSON
logs_json = "logs-peso.json"
logs_df = pd.read_json(logs_json)

# Salvar os dados em um arquivo Excel
output_excel = "logs-peso.xlsx"
logs_df.to_excel(output_excel, index=False)
