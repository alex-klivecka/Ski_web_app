# api_helper.py
import json
from pprint import pprint
from openai import OpenAI

def fetch_data_from_openai():
    # Create an OpenAI client using your API key
  client = OpenAI(api_key='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')
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
  response_json = response.model_dump_json()
  response_dict = json.loads(response_json)
  gpt_response_lcc = response_dict['choices'][0]['message']['content']

  return gpt_response_lcc

# gpt_repsonse_llc = fetch_data_from_openai()

# print(gpt_repsonse_llc)

# with open('data.json', 'w') as json_file:
#   json.dump(gpt_repsonse_llc, json_file)
# Save to a JSON file




