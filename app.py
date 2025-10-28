import streamlit as st
from textblob import TextBlob

# List of words we want to filter out
bad_words = ["hate", "stupid", "idiot", "dumb"]

# Title
st.title("Mood Detector for Kids! 😊")

# Add some friendly instructions
st.write("Share your thoughts and I'll tell you if they sound happy, sad, or neutral!")

# Input box
text = st.text_input("Type how you're feeling:", "I am happy!")

# Check if someone typed something
if text:
    # Check if the text has any bad words
    has_bad_words = any(word in text.lower() for word in bad_words)
    
    if has_bad_words:
        st.write("🤔 Please use kind words only!")
    else:
        # Analyze the mood
        blob = TextBlob(text)
        score = blob.sentiment.polarity
        
        # Show the result with emoji
        if score > 0:
            st.write("😀 That sounds happy!")
            st.balloons()  # This adds a fun animation!
        elif score < 0:
            st.write("😔 That sounds sad!")
        else:
            st.write("😐 That sounds neutral!")

# Add a fun teacher section
if st.checkbox("I'm a teacher!"):
    st.write("### How this works:")
    st.write("1. The app reads what you type")
    st.write("2. It checks if the words are happy or sad")
    st.write("3. It shows an emoji based on the mood!")