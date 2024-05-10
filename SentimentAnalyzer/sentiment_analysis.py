""" 
    This module is used to analyze the sentiment of 
    a given text using the Watson Sentiment Analysis API. 
"""
import json
import requests
def sentiment_analyzer(text_to_analyse):
    """ 
        This function is used to analyze the sentiment of 
        a given text using the Watson Sentiment Analysis API.
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network'
    url += '/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=5)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {'label': label, 'score': score}
