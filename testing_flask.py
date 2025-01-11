from flask import Flask, jsonify
import duckdb

app = Flask(__name__)

conn = duckdb.connect("school_data.duckdb")


@app.route("/high_grades")
def high_grades():
    query = """
    SELECT First_Name, Last_Name, AVG(Grade) AS Avg_Grade
    FROM students
    WHERE Grade > 75
    GROUP BY First_Name, Last_Name
    """
    result = conn.execute(query).fetchall()
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
