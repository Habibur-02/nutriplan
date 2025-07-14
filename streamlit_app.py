
import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv
from app.data_loader import load_nutrition_data
from app.health_filter import recommend_food
from app.clustering import cluster_foods, get_similar_foods
from app.meal_planner import meal_plan

#  Google Gemini API Key (from .env file)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(
    api_key=GEMINI_API_KEY,
    transport='rest'  
)
#  Load and process data
df = load_nutrition_data()
df = cluster_foods(df)

#  Sidebar navigation
page = st.sidebar.selectbox("Select Page", ["Nutrition Recommendation", "Chatbot"])

if page == "Nutrition Recommendation":
    st.title("🍽️ SmartNutriPlan - AI Powered Nutrition App")

    #  Disease Based Recommendation
    st.header("🔍 Disease Based Recommendation")
    conditions = [
        "obesity", "type 2 diabetes", "high cholesterol (hyperlipidemia)",
        "hypertension (high blood pressure)", "non-alcoholic fatty liver disease (nafld)",
        "coronary artery disease (heart disease)", "stroke", "metabolic syndrome",
        "chronic kidney disease (early stage)", "gastroesophageal reflux disease (gerd)",
        "fatty liver (alcoholic / non-alcoholic)", "gout", "osteoporosis",
        "pcos (polycystic ovary syndrome)", "sleep apnea",
        "fatigue / chronic fatigue syndrome", "depression & anxiety"
    ]
    condition = st.selectbox("Select condition", conditions)
    if st.button("Recommend Foods"):
        recommendations = recommend_food(df, condition)
        st.write(recommendations)

    #  Meal Planner
    st.header("🥗 Meal Plan")
    target_cal = st.number_input("Target calories", min_value=500, max_value=4000, value=2000, step=50)
    meals = st.number_input("Number of meals", min_value=1, max_value=5, value=3)
    if st.button("Generate Meal Plan"):
        plan = meal_plan(df, target_calories=target_cal, meals=meals)
        st.write(plan)

    #  Similar Foods
    st.header("🤝 Similar Foods")
    food_input = st.text_input("Enter food name (example: almond)")
    if st.button("Find Similar Foods"):
        similar = get_similar_foods(df, food_input)
        st.write(similar)

elif page == "Chatbot":
    st.title("🤖 Nutrition Chatbot (Powered by Gemini)")
    user_question = st.text_input("Ask your nutrition question:")

    if st.button("Ask"):
        # Nutrition dataset context
        context = f"""
        Nutrition dataset sample:
        {df.head(10).to_string()}
        
        You are a certified nutrition expert. Provide accurate, science-backed answers about:
        - Food recommendations
        - Meal planning
        - Nutrient information
        - Dietary advice for medical conditions
        
        Answer concisely and cite sources when possible.
        """
        
        try:
            
            model = genai.GenerativeModel('gemini-1.0-pro')  
            
          
            response = model.generate_content(
                f"{context}\n\nQuestion: {user_question}",
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=1000,
                    temperature=0.7
                )
            )
            
            
            st.write("💬", response.text)
            
        except Exception as e:
            st.error(f"⚠️ Error getting response: {str(e)}")
            st.info("Note: Gemini has a free tier but may have rate limits")
