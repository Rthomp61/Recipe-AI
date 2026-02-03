# 🍳 Recipe AI

A Python web application that uses AI to generate creative recipes based on ingredients you have available. Reduce food waste and discover new meal ideas!

## Features

- **AI-Powered Recipe Generation**: Uses Google's Gemini AI to create custom recipes
- **Flexible Ingredient Input**: Add ingredients via text list or one-by-one
- **Dietary Filters**: Support for vegetarian, vegan, gluten-free, dairy-free, and nut-free diets
- **Cuisine Preferences**: Choose from various cuisine types (Italian, Mexican, Asian, etc.)
- **Customizable Servings**: Adjust recipe quantities for 1-8 servings
- **Download Recipes**: Save your generated recipes as text files
- **User-Friendly Interface**: Clean, intuitive Streamlit web interface

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Your API key is already configured in the `.env` file

## Running the App

Launch the Streamlit app with:
```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## How to Use

1. **Enter Your Ingredients**:
   - Choose "Text List" to paste multiple ingredients at once
   - Or use "One by One" to add ingredients individually

2. **Set Your Preferences** (in the sidebar):
   - Select any dietary restrictions
   - Choose a cuisine preference (optional)
   - Adjust the number of servings

3. **Generate Recipe**:
   - Click the "Generate Recipe" button
   - Wait for AI to create your custom recipe
   - Download or save the recipe for later

## Example Ingredients to Try

- Chicken breast, tomatoes, garlic, onion, rice
- Eggs, spinach, cheese, bell peppers
- Salmon, lemon, dill, potatoes
- Pasta, basil, olive oil, parmesan

## Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Google Gemini AI**: Recipe generation and creative suggestions
- **python-dotenv**: Environment variable management

## Environmental Impact

This app helps reduce food waste by:
- Creating recipes from ingredients you already have
- Maximizing use of available ingredients
- Reducing unnecessary grocery shopping
- Encouraging creative cooking with limited ingredients

## Future Enhancements

- Image recognition for ingredient detection via camera
- Recipe rating and favorites system
- Nutritional information calculation
- Shopping list generator for missing ingredients
- Recipe history and search functionality

---

Made with ❤️ to reduce food waste and inspire home cooking!
