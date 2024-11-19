from flask import Flask, request, redirect, url_for, render_template
import groq

convo = []
groq_api_key="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"
client = groq.Client(api_key=groq_api_key)
def stream_response(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama3-8b-8192",
        max_tokens=5000,  # Adjust the number of tokens for the response as needed
        temperature=0.7  # Adjust the temperature for creativity level in response
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content
    # convo.append({'role': 'user', 'content': prompt})
    # response = ''
    # stream = ollama.chat(model='llama3.1:8b', messages=convo, stream=True)
    # for chunk in stream:
    #     response += chunk['message']['content']
    #     print(chunk['message']['content'], end='', flush=True)
    # convo.append({'role': 'assistant', 'content': response})
    # return response

app = Flask(__name__)
output_data = {
    'itinerary': '',
    'accommodation': '',
    'food': '',
    'adventures': '',
    'tourist_spots': ''
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plan_itinerary', methods=['GET', 'POST'])
def plan_itinerary():
    if request.method == 'POST':
        data = request.form.to_dict()
        prompt = f"Create a travel itinerary with the following details:\nDestination: {data['destination']}\nPreferences: {data['preferences']}\nBudget: {data['budget']}\nTravel Dates: {data['travel_dates']}\nCompanions: {data['companions']}\nSpecial Requirements: {data['special_requirements']}"
        itinerary = stream_response(prompt)
        output_data['itinerary'] = itinerary
        return redirect(url_for('show_itinerary'))
    return render_template('plan_itinerary.html')

@app.route('/accommodation', methods=['GET', 'POST'])
def accommodation():
    if request.method == 'POST':
        data = request.form.to_dict()
        prompt = f"Find accommodations for the destination '{data['destination']}' with the following details:\nBudget: {data['budget']}\nPreferences: {data['preferences']}"
        accommodation = stream_response(prompt)
        output_data['accommodation'] = accommodation
        return redirect(url_for('show_accommodation'))
    return render_template('find_accommodation.html')

@app.route('/food', methods=['GET', 'POST'])
def food():
    if request.method == 'POST':
        data = request.form.to_dict()
        prompt = f"Suggest food and beverages for the destination '{data['destination']}' with the following preferences: {data['preferences']}"
        food = stream_response(prompt)
        output_data['food'] = food
        return redirect(url_for('show_food'))
    return render_template('suggest_food.html')

@app.route('/adventures', methods=['GET', 'POST'])
def adventures():
    if request.method == 'POST':
        data = request.form.to_dict()
        prompt = f"Suggest adventure activities for the destination '{data['destination']}' with the following preferences: {data['preferences']}"
        adventures = stream_response(prompt)
        output_data['adventures'] = adventures
        return redirect(url_for('show_adventures'))
    return render_template('suggest_adventures.html')

@app.route('/tourist_spots', methods=['GET', 'POST'])
def tourist_spots():
    if request.method == 'POST':
        data = request.form.to_dict()
        prompt = f"List tourist spots for the destination '{data['destination']}' that match the following preferences: {data['preferences']}"
        tourist_spots = stream_response(prompt)
        output_data['tourist_spots'] = tourist_spots
        return redirect(url_for('show_tourist_spots'))
    return render_template('list_tourist_spots.html')

@app.route('/show_itinerary')
def show_itinerary():
    return render_template('itinerary.html', itinerary=output_data['itinerary'])

@app.route('/show_accommodation')
def show_accommodation():
    return render_template('accommodation.html', accommodation=output_data['accommodation'].replace('**',''))

@app.route('/show_food')
def show_food():
    return render_template('food.html', food=output_data['food'])

@app.route('/show_adventures')
def show_adventures():
    return render_template('adventures.html', adventures=output_data['adventures'])

@app.route('/show_tourist_spots')
def show_tourist_spots():
    return render_template('tourist_spots.html', tourist_spots=output_data['tourist_spots'])

if __name__ == '__main__':
    app.run(debug=True)