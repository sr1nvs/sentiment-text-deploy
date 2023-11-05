import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import json

emotion_mapping = {
    0: "Sadness",
    1: "Joy",
    2: "Love",
    3: "Angry/Neutral",
    4: "Fear",
    5: "Surprise"
}

def classify_emotion(text_input):
    model = tf.keras.models.load_model('models/emotion.h5')

    tokenizer_config_path = 'models/restructured_config.json'

    with open(tokenizer_config_path, 'r') as json_file:
        tokenizer_config = json.load(json_file)
        word_index = tokenizer_config.get('word_index', {})

    tokenizer = Tokenizer(num_words=30000)
    tokenizer.word_index = word_index

    max_sequence_length = 100
    text_input_sequence = tokenizer.texts_to_sequences([text_input])
    text_input_sequence = pad_sequences(text_input_sequence, maxlen=max_sequence_length)

    predicted_class_probs = model.predict(text_input_sequence)[0]
    
    max_emotion_index = tf.argmax(predicted_class_probs).numpy()
    emotion_label = emotion_mapping[max_emotion_index]

    return emotion_label, predicted_class_probs

if __name__ == "__main__":
    print("Enter text to classify:")
    text_input = input()
    
    emotion_label, confidence_values = classify_emotion(text_input)
    
    print(f"The given text is classified as {emotion_label}.")
    
    print("Confidence values:")
    for emotion, confidence in enumerate(confidence_values):
        print(f"{emotion_mapping.get(emotion)}: {confidence:.4f}")
