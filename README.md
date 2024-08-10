# Talk2TextSim

You can run the code in vs code and pycharm.

# **Explanation:**

**Audio File Conversion:** 

It converts a list of input audio files in .m4a format to .wav format using the moviepy library.

**Speech Recognition:** 

It uses the speech_recognition library to recognize the text from the converted audio files.

**Text Preprocessing:** 

It preprocesses the recognized text by tokenizing, removing stop words, and converting to lowercase using the nltk library.

**Cosine Similarity Calculation:** 

It calculates the cosine similarity between the preprocessed text and a reference text ("hello how are you") using the sklearn library.

**Similarity Percentage Calculation:** 

It calculates the similarity percentage by multiplying the cosine similarity score by 100.

## The script consists of the following functions:

**preprocess_text:** 

preprocesses the text by tokenizing, removing stop words, and converting to lowercase.

**get_wordnet_pos:** 

determines the part-of-speech (POS) tag for a given word.

**calculate_cosine_similarity:** 

calculates the cosine similarity between two texts.

**main:** 

the main function that orchestrates the entire process.

## The script uses the following libraries:

**moviepy:** for audio file conversion

**speech_recognition:** for speech recognition

**nltk:** for text preprocessing and POS tagging

**sklearn:** for cosine similarity calculation

## The output looks like this:

> ![Capture](https://github.com/user-attachments/assets/866e6866-1c66-4f75-840f-a4a9589472f5)

> ![Capture 2](https://github.com/user-attachments/assets/f10d795b-8523-4005-8708-1c8bae3d87a7)

> ![Capture 3](https://github.com/user-attachments/assets/62412062-9874-46e5-9d80-0c9c9f3fd231)

> ![Capture 4](https://github.com/user-attachments/assets/abe63b0d-46e1-455f-a811-625ae2fbf0c1)
