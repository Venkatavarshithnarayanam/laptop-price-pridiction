from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data
df = pd.read_csv("laptop_data.csv")

# Use correct column names from your file
companies = sorted(df['Company'].dropna().unique())
cpus = sorted(df['Cpu'].dropna().unique())
rams = sorted(df['Ram'].dropna().unique())

@app.route('/', methods=['GET', 'POST'])
def index():
    price = None
    if request.method == 'POST':
        company = request.form['company']
        cpu = request.form['cpu']
        ram = request.form['ram']

        filtered_df = df[(df['Company'] == company) &
                         (df['Cpu'] == cpu) &
                         (df['Ram'] == ram)]

        if not filtered_df.empty:
            price = round(filtered_df['Price'].mean(), 2)
        else:
            price = "No match found."

    return render_template('index.html', companies=companies, cpus=cpus, rams=rams, price=price)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
