from flask import Flask, render_template, jsonify, request
import pandas as pd
import logging
import os  # Import the os module

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def load_stock_symbols():
    try:
        df = pd.read_excel('stock_names.xlsx')
        return df['Stock'].tolist()
    except Exception as e:
        app.logger.error(f"Error loading stock symbols: {str(e)}")
        return []

def load_industries():
    try:
        df = pd.read_excel('Stocks_top_Perf.xlsx')
        industries = df['Industry'].dropna().unique().tolist()
        return industries
    except Exception as e:
        app.logger.error(f"Error loading industries: {str(e)}")
        return []

stock_symbols = load_stock_symbols()

@app.route('/')
def index():
    return render_template('index.html', stock_symbols=stock_symbols)

@app.route('/get_stock_symbols')
def get_stock_symbols():
    return jsonify(stock_symbols)

@app.route('/get_industries')
def get_industries():
    industries = load_industries()
    return jsonify(industries)

@app.route('/get_top_performers', methods=['GET'])
def get_top_performers():
    industry = request.args.get('industry')
    if not industry:
        return jsonify({'error': 'Industry not specified'}), 400

    # Log the file path before attempting to read the Excel file
    excel_file_path = 'Stocks_top_Perf.xlsx'
    app.logger.info(f"Attempting to read Excel file from path: {os.path.abspath(excel_file_path)}")

    try:
        df = pd.read_excel(excel_file_path)
        industry_data = df[df['Industry'] == industry]
        top_performers = industry_data.nlargest(3, 'Return over 3years')[['Name', 'Return over 3years', 'Market Capitalization']]
        top_performers_dict = top_performers.to_dict(orient='records')
        return jsonify(top_performers_dict)
    except Exception as e:
        app.logger.error(f"Error fetching top performers data: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
