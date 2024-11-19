<h1>AI-Powered Travel Planner</h1>
An AI-based travel planner web application that helps users plan itineraries, find accommodations, explore food options, and discover adventure activities and tourist spots.<br>
The app integrates Flask for the backend and uses the Ollama AI API to generate recommendations.

<h2>Features</h2>
•	Travel Itinerary Creation: Generate detailed travel itineraries based on user preferences, budget, and travel dates.<br>
•	Accommodation Finder: Find suitable accommodations within a specified budget and preferences.<br>
•	Food Suggestions: Explore food and beverage options based on destination and preferences.<br>
•	Adventure Recommendations: Discover adventure activities tailored to user interests.<br>
•	Tourist Spots: Get a curated list of must-visit tourist attractions at the destination<br>

<h2>Technologies Used</h2>
<ol type='1'>
<li>Backend: Flask.<br></li>
<li>AI Model: Ollama for AI-based responses.<br></li>
<li>Frontend: HTML, CSS (rendered using Flask templates).<br></li>
</ol>
<h2>Prerequisites</h2>
•	Python 3.8 or higher.<br>
•	A code editor or IDE.<br>

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
