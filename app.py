import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.5-flash')

def generate_recipe(ingredients, dietary_restrictions, cuisine_preference, servings):
    """
    Generate a recipe using Google's Gemini AI based on available ingredients
    """
    prompt = f"""
    You are a creative and practical chef assistant. Generate a delicious recipe using the following ingredients:

    Available Ingredients: {ingredients}

    Requirements:
    - Number of servings: {servings}
    {f"- Dietary restrictions: {', '.join(dietary_restrictions)}" if dietary_restrictions else "- No dietary restrictions"}
    {f"- Cuisine preference: {cuisine_preference}" if cuisine_preference != "Any" else ""}

    Please provide:
    1. Recipe name
    2. List of ingredients needed (with quantities)
    3. Step-by-step cooking instructions
    4. Estimated cooking time
    5. Brief description of the dish

    Try to use as many of the available ingredients as possible to minimize food waste.
    If some common pantry staples (salt, pepper, oil) are needed but not listed, you can include them.

    Format the response in a clear, easy-to-read manner with sections clearly labeled.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating recipe: {str(e)}"

def main():
    # Page configuration
    st.set_page_config(
        page_title="Recipe AI",
        page_icon="🍳",
        layout="wide"
    )

    # Header
    st.title("🍳 Recipe AI")
    st.subheader("Turn your fridge contents into delicious meals!")
    st.markdown("---")

    # Sidebar for preferences
    with st.sidebar:
        st.header("⚙️ Preferences")

        # Dietary restrictions
        st.subheader("Dietary Restrictions")
        dietary_restrictions = []
        if st.checkbox("Vegetarian"):
            dietary_restrictions.append("Vegetarian")
        if st.checkbox("Vegan"):
            dietary_restrictions.append("Vegan")
        if st.checkbox("Gluten-Free"):
            dietary_restrictions.append("Gluten-Free")
        if st.checkbox("Dairy-Free"):
            dietary_restrictions.append("Dairy-Free")
        if st.checkbox("Nut-Free"):
            dietary_restrictions.append("Nut-Free")

        # Cuisine preference
        st.subheader("Cuisine Preference")
        cuisine_preference = st.selectbox(
            "Select cuisine type",
            ["Any", "Italian", "Mexican", "Asian", "Mediterranean", "American", "Indian", "French"]
        )

        # Number of servings
        st.subheader("Servings")
        servings = st.slider("Number of servings", 1, 8, 2)

        st.markdown("---")
        st.info("💡 Tip: Enter ingredients you have on hand, and AI will create a recipe to minimize food waste!")

    # Main content area
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("📝 Your Ingredients")

        # Ingredient input method selection
        input_method = st.radio(
            "How would you like to input ingredients?",
            ["Text List", "One by One"]
        )

        ingredients_list = []

        if input_method == "Text List":
            ingredients_text = st.text_area(
                "Enter your ingredients (one per line or comma-separated)",
                height=200,
                placeholder="e.g.,\nchicken breast\ntomatoes\ngarlic\nonion\nrice"
            )
            if ingredients_text:
                # Handle both newline and comma separation
                ingredients_list = [
                    ing.strip()
                    for ing in ingredients_text.replace(',', '\n').split('\n')
                    if ing.strip()
                ]
        else:
            st.write("Add ingredients one at a time:")
            if 'ingredients' not in st.session_state:
                st.session_state.ingredients = []

            ingredient_input = st.text_input("Ingredient name")
            col_add, col_clear = st.columns([1, 1])

            with col_add:
                if st.button("➕ Add Ingredient") and ingredient_input:
                    st.session_state.ingredients.append(ingredient_input)
                    st.rerun()

            with col_clear:
                if st.button("🗑️ Clear All"):
                    st.session_state.ingredients = []
                    st.rerun()

            if st.session_state.ingredients:
                st.write("**Current ingredients:**")
                for idx, ing in enumerate(st.session_state.ingredients):
                    col_ing, col_remove = st.columns([4, 1])
                    with col_ing:
                        st.write(f"{idx + 1}. {ing}")
                    with col_remove:
                        if st.button("❌", key=f"remove_{idx}"):
                            st.session_state.ingredients.pop(idx)
                            st.rerun()

                ingredients_list = st.session_state.ingredients

        # Display ingredient count
        if ingredients_list:
            st.success(f"✅ {len(ingredients_list)} ingredients ready")

    with col2:
        st.header("🎯 Generated Recipe")

        # Generate recipe button
        if st.button("🚀 Generate Recipe", type="primary", use_container_width=True):
            if not ingredients_list:
                st.error("❌ Please enter at least one ingredient!")
            else:
                with st.spinner("🤖 AI is creating your recipe..."):
                    recipe = generate_recipe(
                        ", ".join(ingredients_list),
                        dietary_restrictions,
                        cuisine_preference,
                        servings
                    )

                    # Display the recipe
                    st.markdown("### Your Custom Recipe")
                    st.markdown(recipe)

                    # Download option
                    st.download_button(
                        label="📥 Download Recipe",
                        data=recipe,
                        file_name="my_recipe.txt",
                        mime="text/plain"
                    )

    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: gray;'>
            <p>Made with ❤️ using Streamlit and Google Gemini AI</p>
            <p>Helping reduce food waste, one recipe at a time! 🌍</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
