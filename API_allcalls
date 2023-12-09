# Import necessary modules
from pprint import pprint
from openai import OpenAI
import json
import tweepy
import time

def load_snow_totals():
    try:
        with open('snow_totals.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
snow_totals = load_snow_totals()
pprint(snow_totals)

def get_and_tweet_roads():
    # Create an OpenAI client using your API key
    client = OpenAI(api_key='sk-')
    text = """this is for an art project. Please summarize, in a Tweet of no more than 280 characters, the traffic and 
    weather conditions depicted in pictures from traffic cameras along a road to the Alta ski resort.
    The road runs 3000 feet up a canyon. The URLs I feed you are pictures in order, from low elevation to high elevation.
    The tweet should provide a brief overview of the overall traffic situation. 
    The language should be very business-like and straightforward, the tone somewhat dry. Though a rare moment of dry humor is appropriate, please be tasteful and not too obvious.
    Note: When analyzing the image from [https://udottraffic.utah.gov/1_devices/aux17226.jpeg], treat it as a parking lot at '/SR-210 @ Alta/MP 12.16', focusing on its occupancy level. 
    For [https://udottraffic.utah.gov/1_devices/aux16270.jpeg], remember to describe it as a road.
    Treat this as if you are providing a neutral service. be descriptive.
    At night, do not comment on how full the parking lot is.
    do not put quotations around your response.
    please use most or all of the 235 characters. 
    """
    response = client.chat.completions.create(
      model="gpt-4-vision-preview",
      messages = [
        {
          "role": "user",
          "content": [
            {"type": "text", "text": text},
            # The following are image URLs for the model to analyze
            {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux14604.jpeg"}},
            {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16265.jpeg"}},
            {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16267.jpeg"}},
            {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16269.jpeg"}},
            {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux16270.jpeg"}},
            {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux17227.jpeg"}},
            {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux17228.jpeg"}},
            {"type": "image_url", "image_url": {"url": "https://udottraffic.utah.gov/1_devices/aux17226.jpeg"}},
          ],
        }
      ],
      max_tokens=400,
    )

    response_json = response.model_dump()

    gpt_tweet_text = response_json['choices'][0]['message']['content']
    pprint(gpt_tweet_text)

    hr12 = snow_totals['12hr']
    hr24 = snow_totals['24hr']

    print(hr12, hr24)

    tweet_text = f'Alta totals: 12 hr: {hr12}" 24 hr: {hr24}". {gpt_tweet_text}'
    # Twitter API Call  

    client = tweepy.Client(
        consumer_key='x6yJhx8rlVhEuAzTAnkDwbAOp',
        consumer_secret= 'wGceYpCL1C1zWAH33aHLluzecc8LJSVWCP8Pf8FHExkCGjapBq',
        access_token= '1730761586636111872-ZdVuUFapeNOrVr72Ur4w12D4cZlBNT',
        access_token_secret= 'mfFjqJT9w9JeTVN7oN6UpgVvermTEDPD2VPqE8YwsajOc')


    response = client.create_tweet(text=tweet_text)
    pprint(response)

    return

get_and_tweet_roads()
# save_roads_to_gcs()




# while True:
#     get_and_tweet_roads()
#     time.sleep(60)  # in seconds

