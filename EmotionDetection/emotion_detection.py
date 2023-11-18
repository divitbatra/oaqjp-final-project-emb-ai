import requests
import json


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion_score = 0
    dominant_emotion = ''
    if response.status_code == 200:
        for emotion in emotion_dict:
            if dominant_emotion_score < emotion_dict[emotion]:
                dominant_emotion_score = emotion_dict[emotion]
                dominant_emotion = emotion
        return {
                'anger': emotion_dict['anger'],
                'disgust': emotion_dict['disgust'],
                'fear': emotion_dict['fear'],
                'joy': emotion_dict['joy'],
                'sadness': emotion_dict['sadness'],
                'dominant_emotion': dominant_emotion
                }  
    elif response.status_code == 500:
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
                }  