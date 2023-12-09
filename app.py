from flask import Flask, render_template
from pprint import pprint
from openai import OpenAI
from apscheduler.schedulers.background import BackgroundScheduler
from Alta.API_alta_openaiFunc import fetch_data_from_openai
from Alta.alta_selenium_snowtotals import get_alta_snow_totals
from Alta.alta_selenium_forecast import get_alta_forecast

app = Flask(__name__)

alta_openai = fetch_data_from_openai()
alta_snow_totals = get_alta_snow_totals()
alta_forecast = get_alta_forecast()

def fetch_data():
    global alta_openai, alta_snow_totals, alta_forecast
    alta_openai = fetch_data_from_openai()
    alta_snow_totals = get_alta_snow_totals()
    alta_forecast = get_alta_forecast()

scheduler = BackgroundScheduler()
scheduler.add_job(fetch_data, 'interval', minutes=1)
scheduler.start()

@app.route('/')

def home():
    return render_template('home.html', 
                           alta_openai=alta_openai,
                           alta_12hr = alta_snow_totals['12hr'],
                           alta_24hr = alta_snow_totals['24hr'],
                           alta_forecast = alta_forecast
                           )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

