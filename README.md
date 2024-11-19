<h1>AI-Powered Travel Planner</h1>
<p>
An AI-based travel planner web application that helps users plan itineraries, find accommodations, explore food options, and discover adventure activities and tourist spots.<br>
The app integrates Flask for the backend and uses the Ollama AI API to generate recommendations.
</p>

<h2>Features</h2>
<ul type=point>
<li>Travel Itinerary Creation: Generate detailed travel itineraries based on user preferences, budget, and travel dates.<br></li>
<li>Accommodation Finder: Find suitable accommodations within a specified budget and preferences.<br></li>
<li>Food Suggestions: Explore food and beverage options based on destination and preferences.<br></li>
<li>Adventure Recommendations: Discover adventure activities tailored to user interests.<br></li>
<li>Tourist Spots: Get a curated list of must-visit tourist attractions at the destination<br></li>
</ul>

<h2>Technologies Used</h2>
<ul type=point>
<li>Backend: Flask.<br></li>
<li>AI Model: Ollama for AI-based responses.<br></li>
<li>Frontend: HTML, CSS (rendered using Flask templates).<br></li>
</ul>

<h2>Prerequisites</h2>
<ul type=point>
<li>Python 3.8 or higher.<br></li>
<li>A code editor or IDE.<br></li>
</ul>

<h2>Project Structure</h2>
<pre>
travel-planner/<br>
	|-> templates/<br>
		|-> index.html<br>
		|-> plan_itinerary.html<br>
		|-> itinerary.html<br>
		|-> find_accommodation.html<br>
		|-> accommodation.html<br>
		|-> suggest_food.html<br>
		|-> food.html<br>
		|-> suggest_adventures.html<br>
		|-> adventures.html<br>
		|-> list_tourist_spots.html<br>
		|-> tourist_spots.html<br>
	|-> static/ <br>
		|-> images/<br>
			|-> #images in jpg format<br>
	|-> travel_plan.py<br>
	|-> travel_plan_groq.py<br>
	|-> groq.txt<br>
</pre>
