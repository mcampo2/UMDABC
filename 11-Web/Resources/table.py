import pandas as pd
cities = pd.read_csv("cities.csv")
cities.to_html("table.html", index=False)