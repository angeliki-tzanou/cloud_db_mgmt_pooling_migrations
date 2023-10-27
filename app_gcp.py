from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy import text

app_gcp = Flask(__name__)

gcp_db_uri = "mysql+mysqlconnector://root:tza504!!@34.170.238.2/ang"
engine_gcp = create_engine(gcp_db_uri)

# Configure SQLAlchemy engine for GCP
engine_gcp = create_engine(gcp_db_uri, pool_size=20, pool_timeout=3)

@app_gcp.route('/get_data')
def get_data():
    connection = engine_gcp.connect()
    patients_query = text("SELECT * FROM patients")
    patients_result = connection.execute(patients_query)

    medical_recs_query = text("SELECT * FROM medical_records")
    medical_recs_result = connection.execute(medical_recs_query)

    patients_data = [dict(row) for row in patients_result]
    medical_recs_data = [dict(row) for row in medical_recs_result]

    connection.close()

    return jsonify({'patients': patients_data, 'medical_records': medical_recs_data})

if __name__ == '__main__':
    app_gcp.run()
