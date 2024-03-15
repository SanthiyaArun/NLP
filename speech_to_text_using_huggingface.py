# -*- coding: utf-8 -*-
"""Speech to text using huggingface.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q74L7pSBb0xHDQJ1QuvdMjiKlX41MVgB
"""

!pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# 
# from transformers import pipeline
# import streamlit as st
# 
# # Load the speech recognition pipeline using the Whisper model
# recognizer = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")
# 
# def transcribe_audio(audio_file):
#     try:
#         # Perform speech recognition on the audio file
#         transcript = recognizer(audio_file)
#         return transcript
#     except Exception as e:
#         return str(e)
# 
# def main():
#     st.title("Speech to Text with OpenAI Whisper")
#     st.write("Upload an audio file to transcribe.")
# 
#     audio_file = st.file_uploader("Upload Audio File", type=["mp3", "wav"])
# 
#     if audio_file is not None:
#         if st.button("Transcribe"):
#             st.write("Transcribing...")
# 
#             try:
#                 # Perform transcription
#                 transcript = transcribe_audio(audio_file)
#                 st.success("Transcription: {}".format(transcript))
#             except Exception as e:
#                 st.error("Error occurred during transcription: {}".format(str(e)))
# 
# if __name__ == "__main__":
#     main()
#

!streamlit run app.py & npx localtunnel --port 8501

