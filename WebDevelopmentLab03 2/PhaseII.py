import streamlit as st
import random
import requests
from datetime import date

def fetch_affirmations():
    url = "https://raw.githubusercontent.com/annthurium/affirmations/main/affirmations.js"
    response = requests.get(url)
    json_start = response.text.find("[")
    json_end = response.text.rfind("]")
    if json_start != -1 and json_end != -1:
        json_data = response.text[json_start:json_end+1]
        affirmations_data = eval(json_data)
        return affirmations_data
    

def get_daily_affirmation():
    affirmations = fetch_affirmations()
    return random.choice(affirmations)

def get_message_from_color(color):
    color_ranges = {
        "Red": {"range": ["#ff0000", "#ff9999"], "message": "Red is often associated with passion and energy."},
        "Green": {"range": ["#00ff00", "#99ff99"], "message": "Green symbolizes growth, harmony, and freshness."},
        "Blue": {"range": ["#0000ff", "#9999ff"], "message": "Blue represents calmness, stability, and trust."},
        "Yellow": {"range": ["#ffff00", "#ffff99"], "message": "Yellow is the color of sunshine, happiness, and optimism."},
        "Orange": {"range": ["#ffa500", "#ffcc99"], "message": "Orange represents creativity, enthusiasm, and determination."},
        "Purple": {"range": ["#800080", "#cc99ff"], "message": "Purple is associated with royalty, ambition, and creativity."},
        "Pink": {"range": ["#ff69b4", "#ffccff"], "message": "Pink symbolizes love, affection, and femininity."},
        "Brown": {"range": ["#a52a2a", "#cc9966"], "message": "Brown represents stability, reliability, and earthiness."}
    }
    for color_name, color_data in color_ranges.items():
        if color in color_data["range"]:
            return color_data["message"]
    
    return "This color represents luck and blessings entering your life."



def main():
    st.title("Daily Affirmation & Day Feedback")
    
    st.image("https://source.unsplash.com/featured/?positivity", caption="Image for positivity", use_column_width=True)
    
    st.title("Daily Affirmation")
    affirmation = get_daily_affirmation()
    st.write(f"🌟 Today's affirmation is: **{affirmation}** 🌟")

    st.header("How is your day going?")
    day_feedback = st.text_area("Share your thoughts here", "")#NEW

    if st.button("Submit"):
        st.write("Thank you for sharing!")

    st.image("https://source.unsplash.com/featured/?thank+you", caption="Thank you image", use_column_width=True)
    
    st.title("Choose your color of the day")#NEW
    selected_color = st.color_picker("Pick a color", "#ff0000")
    message = get_message_from_color(selected_color)
    st.write(message)

    st.title("YouTube Video Player")
    
    youtube_url = "https://www.youtube.com/watch?v=yo1pJ_D-H3M"
    
   
    video_id = youtube_url.split("=")[-1]
    
    
    st.markdown(f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)#NEW

if __name__ == "__main__":
    main()

        
