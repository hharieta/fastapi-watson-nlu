import os, operator, logging
from typing import Dict
from utils import deep_update
from fastapi import HTTPException
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features
from ibm_watson.natural_language_understanding_v1 import SentimentOptions, EmotionOptions, EntitiesOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_nlu_client() -> NaturalLanguageUnderstandingV1:
    apikey = os.getenv("NLU_APIKEY")
    url = os.getenv("NLU_URL")

    if not apikey or not url:
        raise ValueError("APIKEY and URL for NLU service are required")

    authenticator = IAMAuthenticator(apikey)
    nlu_client = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )

    nlu_client.set_service_url(url)
    return nlu_client


def api_response(
        nlu_client: NaturalLanguageUnderstandingV1,
        text: str, 
        languaje: str) -> Dict[str, any]:
    
    try:
        response = nlu_client.analyze(
            features=Features(
                sentiment=SentimentOptions(document=True),
                emotion=EmotionOptions(document=True),
                entities=EntitiesOptions(emotion=True, sentiment=True)
                ),
            text=text,
            return_analyzed_text=True,
            language=languaje,
            limit_text_characters=10000
        ).get_result()

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

    return response
    

def get_dominant_emotion(emotions: Dict[str, any]) -> str:
    return max(
        emotions['emotion']['document']['emotion'].items(), 
        key=operator.itemgetter(1))[0]


def add_dominant_emotion(emotions: Dict[str, any], dominant_emotion: str) -> Dict[str, any]:
    return deep_update(
        emotions,
        {
            "emotion": {
                "document": {
                    "emotion": {
                        "dominant_emotion": dominant_emotion
                    }
                }
            }
        }
    )


def emotion_analyzer(text: str, languaje: str) -> Dict[str, any]:

    nlu_client = get_nlu_client()

    try:
        emotions = api_response(nlu_client, text, languaje)
        dominant_emotion = get_dominant_emotion(emotions)
        emotions = add_dominant_emotion(emotions, dominant_emotion)

        logger.info(f"Successfully analyzed text with dominant emotion: {dominant_emotion}")

        return emotions
    
    except HTTPException as http_err:
        logger.error(f"HTTP exception occurred: {http_err.detail}")
        raise http_err
    except ValueError as ve:
        logger.error(f"Configuration error: {ve}")
        raise HTTPException(status_code=500, detail="Configuration error: " + str(ve))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
