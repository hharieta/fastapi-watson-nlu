# We will test the emotion_analyzer function in the analyzer/emotions.py file
import sys
import os
import unittest
import operator
from typing import Dict
from unittest.mock import patch, MagicMock
# Add the path to the sys.path for execute 
# python /tests/emotion_test.py in the root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analyzer import emotion_analyzer


def get_dominant_emotion(emotions: Dict[str, any]) -> str:
        # print(emotions["emotion"]["document"]["emotion"].items())

        return max(
            emotions['emotion']['document']['emotion'].items(), 
            key=operator.itemgetter(1))[0]
        


class TestSentimentAnalyzer(unittest.TestCase):
    @patch('analyzer.emotions.get_nlu_client')
    @patch('analyzer.emotions.api_response')

    def test_sentiment_analyzer(self, mock_emotion_response, mock_get_nlu_client):

        mock_nlu_client = MagicMock()
        mock_get_nlu_client.return_value = mock_nlu_client

        mock_emotion_response.side_effect = [
            {"emotion": {
                "document": {
                    "emotion": {
                        "joy": 0.6,
                        "anger": 0.1,
                        "disgust": 0.1,
                        "sadness": 0.1,
                        "fear": 0.1
                        }
                    }
                }
            },
            {"emotion": {
                "document": {
                    "emotion": {
                        "joy": 0.2,
                        "anger": 0.5,
                        "disgust": 0.1,
                        "sadness": 0.1,
                        "fear": 0.1
                        }
                    }
                }
            },
            {"emotion": {
                "document": {
                    "emotion": {
                        "joy": 0.1,
                        "anger": 0.2,
                        "disgust": 0.4,
                        "sadness": 0.2,
                        "fear": 0.1
                        }
                    }
                }
            },
            {"emotion": {
                "document": {
                    "emotion": {
                        "joy": 0.1,
                        "anger": 0.1,
                        "disgust": 0.2,
                        "sadness": 0.4,
                        "fear": 0.2
                        }
                    }
                }
            },
            {"emotion": {
                "document": {
                    "emotion": {
                        "joy": 0.1,
                        "anger": 0.2,
                        "disgust": 0.1,
                        "sadness": 0.1,
                        "fear": 0.5
                        }
                    }
                }
            }
        ]

        result_1 = emotion_analyzer('I am glad this happened', 'en')
        self.assertEqual(get_dominant_emotion(result_1), 'joy')

        result_2 = emotion_analyzer('I am really mad about this', 'en')
        self.assertEqual(get_dominant_emotion(result_2), 'anger')

        result_3 = emotion_analyzer('I feel disgusted just hearing about this', 'en')
        self.assertEqual(get_dominant_emotion(result_3), 'disgust')

        result_4 = emotion_analyzer('I am so sad about this', 'en')
        self.assertEqual(get_dominant_emotion(result_4), 'sadness')

        result_5 = emotion_analyzer('I am really afraid that this will happen', 'en')
        self.assertEqual(get_dominant_emotion(result_5), 'fear')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
