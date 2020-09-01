from tensorflow import keras
from tensorflow_text import SentencepieceTokenizer
import time

### use siamese finetuned
print('\n\nLoading model ...\n')
start = time.time()
MODEL_DIR = 'models/ru_sentiment_clf/'
model = keras.models.load_model(MODEL_DIR)
print(f'\n model is loaded from {MODEL_DIR} \n')
print(f'it took {time.time()- start} seconds\n\n')

def get_sentiment(text, model = model, treshold = 0.5):
    pred = model.predict([text])
    score = pred[0][0]
    sentiment = 'positive' if score>treshold else 'negative'
    return sentiment, score