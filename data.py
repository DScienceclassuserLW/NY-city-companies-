#to try out git, posting a file or two...

import pandas as pd
from flask import Flask
from flask import request

#implement Flask API functions to return list of ...
# crunchbase companies based in New York, (not necessarily starting with Ac)

#take user input, to return list of json objects from (using Crunchbase not Webhose?) 
#where the 'title' fields contain the query string

#the csv file is named, "crunchbase_odm_orgs.csv"
#comma delimited

#import the data into df
df = pd.read_csv("crunchbase_odm_orgs.csv")

#limit to New York city
df_NY = df[df['city'] == 'New York'] #filter on city is exactly 'New York'

#convert to html
ny_html = df_NY.to_html()

###########################################################
app = Flask("NY Companies")

@app.route("/")
def index():
    hmtl_str = ny_html
    return hmtl_str

# Run the Flask development server (optional for this cell)
app.run(host='localhost', port=5005)

############################################################

