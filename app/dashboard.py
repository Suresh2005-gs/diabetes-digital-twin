# Streamlit doctor dashboard

#python -c "import pandas as pd; [print(f, '\n', pd.read_csv(f'data/raw/{f}.csv', nrows=3).to_string(), '\n') for f in ['patients','conditions','observations','medications','encounters']]"
#I added nrows=3 so it reads only the first 3 rows and doesn't load the 173 MB file fully.