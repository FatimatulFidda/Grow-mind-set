import streamlit as st
from PIL import Image
import random

# App Title and Header
st.set_page_config(page_title="Mindset Growth", page_icon="🌱", layout="wide")
st.title("🌱 Mindset Growth App")
st.subheader("Develop a Positive and Growth-Oriented Mindset")

# Sidebar for Navigation
st.sidebar.header("Navigation")
options = ["Home", "Daily Affirmations", "Mindfulness Exercises", "Journaling", "Resources", "Quotes"]
choice = st.sidebar.radio("Go to", options)

# Home Page
if choice == "Home":
    st.image("https://teacherbooker.com/wp-content/uploads/2017/10/Blog-pic-growth-mindset.jpg", use_container_width=True)
    st.write("### Welcome to Mindset Growth")
    st.write(
        "This app helps you cultivate a growth mindset through affirmations, mindfulness, and journaling. Stay positive and keep growing!"
    )

# Daily Affirmations
elif choice == "Daily Affirmations":
    st.write("## 🌟 Daily Affirmations")
    affirmations = [
        "I am capable of achieving great things.",
        "Challenges help me grow and learn.",
        "I embrace change and welcome new opportunities.",
        "I am confident, strong, and resilient.",
        "Every day, I become a better version of myself.",
        "I believe in my ability to succeed."
    ]
    st.write("### Today's Affirmation:")
    st.success(random.choice(affirmations))

# Mindfulness Exercises
elif choice == "Mindfulness Exercises":
    st.write("## 🧘‍♀️ Mindfulness Exercises")
    st.write("Try these exercises to stay present and reduce stress:")
    exercises = [
        "1. Take 5 deep breaths, inhaling through the nose and exhaling through the mouth.",
        "2. Focus on the sensations of your body for 1 minute.",
        "3. Observe your surroundings and name 5 things you can see.",
        "4. Close your eyes and listen to your breathing for 2 minutes.",
        "5. Smile and think about one thing you're grateful for."
    ]
    for ex in exercises:
        st.write(f"- {ex}")

# Journaling
elif choice == "Journaling":
    st.write("## 📖 Journaling")
    journal_entry = st.text_area("Write your thoughts and reflections:")
    if st.button("Save Entry"):
        st.success("Your journal entry has been saved! Keep expressing yourself.")

# Resources
elif choice == "Resources":
    st.write("## 📚 Resources")
    st.write("Here are some useful resources for mindset growth:")
    st.markdown("- [Growth Mindset TED Talk](https://www.ted.com)")
    st.markdown("- [Mindfulness Meditation Guide](https://www.mindful.org)")
    st.markdown("- [Book: Mindset by Carol Dweck](https://www.goodreads.com/book/show/40745.Mindset)")
    st.markdown("- [Free Guided Meditations](https://www.headspace.com)")

# Motivational Quotes
elif choice == "Quotes":
    st.write("## 💡 Inspirational Quotes")
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "Do what you can, with what you have, where you are. - Theodore Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
    ]
    st.write(random.choice(quotes))

# Footer
st.markdown("---")
st.write("Made By Fatima Tul Fidda | Stay positive and keep growing! 🌿")