# Recipe AI PRD

**Project:** Recipe AI - Smart Recipe Generator
**Owner:** Ray Thompson
**Date:** February 3, 2026

---

## Problem

Home cooks waste an average of $1,500/year on unused groceries that spoil, and spend 30+ minutes daily deciding what to cook. When people open their fridges, they see random ingredients but lack the inspiration or knowledge to combine them into a meal, leading to takeout orders, food waste, and environmental harm. Additionally, people with dietary restrictions struggle to find recipes that match both their available ingredients and their health needs.

**Supporting Context:**
- 40% of food in the US goes to waste, with the average household discarding 30-40% of purchased food
- "What's for dinner?" is asked 4.5 billion times per day in America
- 1 in 4 Americans has dietary restrictions (vegetarian, vegan, gluten-free, etc.)

---

## Opportunity

Enable home cooks to instantly transform their available ingredients into personalized, delicious recipes using AI, reducing food waste by 30% and saving families 20+ hours per month in meal planning time.

**Market Opportunity:**
- $10B meal kit market shows demand for cooking solutions
- 73% of consumers say they want to reduce food waste
- AI-powered food tech is projected to grow 25% annually through 2030
- Target: 100,000 users generating 1M+ recipes in Year 1

---

## Users & Needs

**Who:**

**Primary users:**
- Busy home cooks (ages 25-55) who want to reduce food waste and meal planning stress
- People with dietary restrictions seeking compatible recipes

**Secondary users:**
- College students with limited ingredients and budgets
- Environmental-conscious consumers focused on sustainability

**Needs:**

**Key user needs:**
- As a **home cook**, I need to **generate recipes from my available ingredients** because **I want to avoid food waste and save money on groceries**
- As a **busy parent**, I need to **quickly decide what to cook for dinner** because **I don't have time to browse cookbooks or search multiple websites**
- As a **person with dietary restrictions**, I need to **find recipes that match my health requirements** in order to **maintain my diet without extensive research**
- As an **environmentally-conscious consumer**, I need to **maximize use of ingredients I already have** because **I want to reduce my carbon footprint and food waste**
- As a **novice cook**, I need to **receive step-by-step cooking instructions** in order to **successfully prepare meals without culinary expertise**

---

## Proposed Solution

Recipe AI is a web-based application that uses Google's Gemini AI to instantly generate custom recipes based on user-provided ingredients. Users simply input what they have in their fridge (via text list or one-by-one), select dietary preferences and cuisine type, and receive a complete recipe with ingredients, instructions, cooking time, and description. The app prioritizes using as many available ingredients as possible to minimize waste.

**Top 3 MVP Value Props:**

1. **[The Vitamin] - Instant Recipe Generation**
   - Get a complete, personalized recipe in under 30 seconds using AI, maintaining the status quo of having meal options available

2. **[The Painkiller] - Zero Food Waste**
   - Eliminate the daily "what's for dinner?" stress and reduce grocery waste by creating recipes from what you already have, solving the biggest pain point

3. **[The Steroid] - Dietary Intelligence**
   - Automatically adapts recipes to dietary restrictions (vegan, gluten-free, etc.) and cuisine preferences, creating delightful personalized experiences

---

## Goals & Non-Goals

**Goals:**
- Enable users to generate recipes from available ingredients in under 60 seconds
- Reduce user food waste by 30% through maximized ingredient utilization
- Support 5+ dietary restrictions and 8+ cuisine types
- Achieve 70%+ user satisfaction with generated recipes
- Build a simple, intuitive interface that requires zero learning curve

**Non-Goals:**
- Nutritional calculation or calorie tracking (future enhancement)
- Recipe rating/favorites system (future enhancement)
- User accounts or recipe history (future enhancement)
- Image recognition for ingredient detection (future enhancement)
- Shopping list generation for missing ingredients (future enhancement)
- Social sharing or community features (future enhancement)

---

## Success Metrics

| Goal | Signal | Metric | Target |
|------|--------|--------|--------|
| Adoption | Users find the app useful | Weekly Active Users (WAU) | >10,000 WAU by Month 3 |
| Engagement | Users generate multiple recipes | Avg recipes per user per week | >3 recipes/user/week |
| Value | Recipes meet user needs | Recipe generation completion rate | >85% completion |
| Retention | Users return to app | 7-day retention rate | >40% |
| Quality | Generated recipes are satisfactory | User doesn't regenerate immediately | >70% accept first recipe |

---

## Requirements

Legend:
- **[P0]** = MVP for GA release
- **[P1]** = Important for delightful experience
- **[P2]** = Nice-to-have

---

### Use Case 1: Home Cook Needs Dinner Inspiration

**Context:** This is the primary use case. Users have ingredients but lack inspiration or knowledge to combine them. We're optimizing for speed and ease of use to reduce friction from "I have food" to "I have a recipe."

#### Ingredient Input
- **[P0]** User can input ingredients via free-form text list (comma or line-separated)
- **[P0]** User can add ingredients one-by-one with add/remove functionality
- **[P0]** User can see a count of ingredients ready for recipe generation
- **[P0]** User can clear all ingredients at once
- **[P1]** User can remove individual ingredients from the list
- **[P2]** User receives autocomplete suggestions for common ingredients

#### Preference Selection
- **[P0]** User can select dietary restrictions (Vegetarian, Vegan, Gluten-Free, Dairy-Free, Nut-Free)
- **[P0]** User can choose cuisine preference (Any, Italian, Mexican, Asian, Mediterranean, American, Indian, French)
- **[P0]** User can adjust number of servings (1-8 people)
- **[P1]** User preferences are clearly visible in a sidebar
- **[P2]** User preferences persist across sessions

#### Recipe Generation
- **[P0]** User can generate a recipe with a single button click
- **[P0]** Recipe generation completes in under 30 seconds
- **[P0]** User receives clear error message if no ingredients are provided
- **[P0]** User sees loading indicator while AI generates recipe
- **[P1]** User can regenerate a different recipe with the same ingredients
- **[P2]** User can provide feedback on recipe quality

---

### Use Case 2: User with Dietary Restrictions Needs Compliant Recipe

**Context:** Users with dietary restrictions need confidence that recipes match their health requirements. We're optimizing for safety and trust in AI recommendations.

#### Dietary Compliance
- **[P0]** Generated recipes respect all selected dietary restrictions
- **[P0]** Recipes clearly indicate which restrictions they follow
- **[P0]** AI does not suggest ingredients that violate selected restrictions
- **[P1]** Recipes include substitution suggestions for restricted ingredients
- **[P2]** User can save preferred restriction combinations as profiles

---

### Use Case 3: User Wants to Save or Share Recipe

**Context:** Users want to preserve recipes they like for future reference. We're optimizing for convenient access to generated content.

#### Recipe Output
- **[P0]** Recipe displays in clear, readable format with sections:
  - Recipe name
  - Ingredient list with quantities
  - Step-by-step instructions
  - Estimated cooking time
  - Brief description
- **[P0]** User can download recipe as a text file
- **[P1]** Recipe format is printer-friendly
- **[P2]** User can copy recipe to clipboard with one click
- **[P2]** User can email recipe to themselves

---

### Use Case 4: First-Time User Discovers the App

**Context:** New users need to understand what the app does and how to use it within 10 seconds. We're optimizing for clarity and immediate value.

#### Onboarding & Usability
- **[P0]** App clearly communicates its purpose in the header/title
- **[P0]** No login or account creation required to use core features
- **[P0]** App loads in under 3 seconds
- **[P0]** UI is intuitive with clear labels and icons
- **[P1]** Sidebar includes helpful tips for ingredient input
- **[P1]** App displays example ingredients to guide users
- **[P2]** First-time users see a brief tutorial or walkthrough

---

### Use Case 5: User Encounters Errors or Issues

**Context:** Technical issues should not block users from using the app. We're optimizing for reliability and clear error communication.

#### Error Handling
- **[P0]** User receives clear error messages if API fails
- **[P0]** User can retry recipe generation if it fails
- **[P0]** App gracefully handles missing or invalid API keys
- **[P1]** User sees specific error messages (not generic "something went wrong")
- **[P2]** App includes contact/support information for help

---

## Technical Requirements

#### Performance
- **[P0]** App loads in under 3 seconds on standard broadband
- **[P0]** Recipe generation completes in under 30 seconds
- **[P0]** App is responsive and works on desktop browsers
- **[P1]** App works on mobile browsers (responsive design)
- **[P2]** App caches common API responses to reduce costs

#### Security & Privacy
- **[P0]** API keys are stored securely in environment variables
- **[P0]** API keys are never exposed to client-side code
- **[P0]** .env files are excluded from version control
- **[P1]** App does not collect or store user data
- **[P2]** App includes privacy policy and terms of service

#### AI Integration
- **[P0]** App uses Google Gemini 2.5 Flash model for recipe generation
- **[P0]** AI prompts are optimized to maximize ingredient usage
- **[P0]** AI generates recipes with clear structure and formatting
- **[P1]** AI considers common pantry staples (salt, oil, etc.) as available
- **[P2]** AI provides cooking tips or variations in responses

---

## Appendix

**Designs:**
- Streamlit-based web interface with two-column layout
- Left column: Ingredient input and preferences
- Right column: Generated recipe display
- Sidebar: Dietary restrictions, cuisine, and servings

**Technologies Used:**
- Python 3.13
- Streamlit 1.40.1+
- Google Gemini AI (gemini-2.5-flash model)
- python-dotenv for environment management

**Meeting Notes:**
- Initial concept: Build practical app solving real-world problem (food waste)
- Selected from 10 app ideas based on environmental impact and AI integration
- Pivoted from "Smart Recipe Generator" to "Recipe AI" for brand clarity

**Other Resources:**
- GitHub Repository: https://github.com/Rthomp61/Recipe-AI
- Live App: http://localhost:8501 (local deployment)
- API Documentation: Google Gemini AI Documentation
