from moviepy.editor import AudioFileClip  
import speech_recognition as sr  
from sklearn.metrics.pairwise import cosine_similarity  
from sklearn.feature_extraction.text import TfidfVectorizer  
import nltk  
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords  
from nltk.stem import WordNetLemmatizer  
from nltk import pos_tag  
from nltk.corpus import wordnet  
  
# Download required NLTK resources  
nltk.download('punkt')  
nltk.download('stopwords')  
nltk.download('wordnet')  
nltk.download('averaged_perceptron_tagger')  
  
# Define input and output files  
import os  
input_files = [f for f in os.listdir('.') if f.endswith('.m4a')]
output_files = [f"output_{i+1}.wav" for i in range(len(input_files))]  
  
# Convert audio files to WAV format  
for input_file, output_file in zip(input_files, output_files):  
   audio = AudioFileClip(input_file)  
   audio.write_audiofile(output_file, codec="pcm_s16le")  
  
# Initialize speech recognition  
r = sr.Recognizer()  
audio_files = output_files  
recognized_text = []  
  
# Recognize text from audio files  
for file in audio_files:  
   with sr.AudioFile(file) as source:  
      audio_text = r.record(source)  
      try:  
        text = r.recognize_google(audio_text)  
        print(f'Converting audio transcripts into text for {file}...')  
        recognized_text.append(text)  
      except:  
        print(f'Sorry, unable to recognize text for {file}. Please try again...')  
        recognized_text.append('Error')  
  
# Print recognized text  
for i, text in enumerate(recognized_text):  
   print(f'Text {i+1}: {text}')  
  
def preprocess_text(text):  
   if isinstance(text, list):  
      text = ''.join(text)  
   # Tokenization  
   tokens = word_tokenize(text.lower())  
   # Removing stop words  
   stop_words = set(stopwords.words("english"))  
   filtered_tokens = [word for word in tokens if word not in stop_words]  
   return filtered_tokens  
  
def get_wordnet_pos(tag):  
   if tag.startswith("J"):  
      return wordnet.ADJ  
   elif tag.startswith("V"):  
      return wordnet.VERB  
   elif tag.startswith("N"):  
      return wordnet.NOUN  
   elif tag.startswith("R"):  
      return wordnet.ADV  
   else:  
      return wordnet.NOUN  
  
def calculate_cosine_similarity(text1, text2):  
   vectorizer = TfidfVectorizer()  
   tfidf_vectors = vectorizer.fit_transform([text1, text2])  
   cosine_sim = cosine_similarity(tfidf_vectors[0:1], tfidf_vectors[1:2])  
   return cosine_sim  
  
def main():  
   print("\nText Similarity Calculator")  
   print("==========================")  
   for i, text2 in enumerate(recognized_text):  
      text1 = "hello how are you"  # Use the first recognized text as the reference  
      similarity_score = calculate_cosine_similarity(text1, text2)  
      similarity_percentage = similarity_score * 100  
      print(f"\nSimilarity Percentage for Text {i+1}: {similarity_percentage.item():.2f}%")  
  
if __name__ == "__main__":  
   main()