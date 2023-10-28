from flask import render_template
from sqlalchemy import create_engine, inspect

from app_gcp import app_gcp 

gcp_db_uri = "mysql+pymysql://root:tza504!!@34.170.238.2/ang"

engine = create_engine(gcp_db_uri)

@app_gcp.route('/')
def home():
    insp = inspect(engine)
    table_names = insp.get_table_names()
    return render_template('home.html', tables=table_names)






