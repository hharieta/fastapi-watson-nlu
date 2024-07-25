# FastAPI Endpoints with IBM Watson NLU

This repository contains a FastAPI application that utilizes IBM Watson Natural Language Understanding (NLU) for sentiment analysis and text classification.

Based on the [EmotionDetection](https://github.com/hharieta/EmotionDetection) project by the greatest [Inge Gatovsky](https://github.com/hharieta)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hharieta/fastapi-watson-nlu.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your IBM Watson NLU credentials by creating a `.env` file and adding the following:

```bash
API_KEY=your-api-key
URL=your-watson-nlu-url
```

4. Run the FastAPI application:

```bash
uvicorn app:app --reload
```

## Usage

Once the application is running, you can access the following endpoints:

- `localhost:8000/api/v2/analyze`: Analyzes the Emotions of a given text using IBM Watson NLU.
- `localhost:8000/api/v2/status`: Returns the status of the application.

**Curl Example**:

```bash
curl -X 'POST' \
  'http://localhost:8000/api/v2/analyze' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "I am glad this happened",
  "language": "en"
}'
```

**Postman Example**:

- Open Postman and create a new request.
- Set the request type to `POST`.
- Set the request URL to `http://localhost:8000/api/v2/analyze`.
- Configure the headers:
  - Key: `accept`, Value: `application/json`.
  - Key: `Content-Type`, Value: `application/json`.
- Config body:
  - Select `JSON` or `raw` from the dropdown.
  - Add the following JSON data:

    ```json
    {
    "text": "I am glad this happened",
    "language": "en"
    }
    ```

⚠️ **Note**: The `language` parameter is optional. If not provided, the default value is english.

**Language codes**: IBM Watson NLU uses ISO 639-1 code. for example englis: `en`. See the codes on [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

**Supported Languages**: Watch the supported languages at [IBM Watson NLU Language support](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-language-support).

## Limitations

- The application is limited to 10,000 text characters to analyze.
- API calls are limited to 5 per minute. If the limit is exceeded, the application will return a `429` status code. (I don not have a paid account, so I am using the free tier 🙊)

## Pytest

To run the tests, 

```text
tests
├── __init__.py
├── emotion_test.py
└── ratelimit_test.py
```

execute the following command:

```bash
pytest --import-mode=append
```

## Examples


### Analyze Emotions

**Request example for The Raven by Edgar Allan Poe**:

```json
{
  "text": "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore—     While I nodded, nearly napping, suddenly there came a tapping, As of some one gently rapping, rapping at my chamber door. “’Tis some visitor,” I muttered, “tapping at my chamber door—             Only this and nothing more.”      Ah, distinctly I remember it was in the bleak December; And each separate dying ember wrought its ghost upon the floor.     Eagerly I wished the morrow;—vainly I had sought to borrow     From my books surcease of sorrow—sorrow for the lost Lenore— For the rare and radiant maiden whom the angels name Lenore—             Nameless here for evermore.      And the silken, sad, uncertain rustling of each purple curtain Thrilled me—filled me with fantastic terrors never felt before;     So that now, to still the beating of my heart, I stood repeating     “’Tis some visitor entreating entrance at my chamber door— Some late visitor entreating entrance at my chamber door;—             This it is and nothing more.”      Presently my soul grew stronger; hesitating then no longer, “Sir,” said I, “or Madam, truly your forgiveness I implore;     But the fact is I was napping, and so gently you came rapping,     And so faintly you came tapping, tapping at my chamber door, That I scarce was sure I heard you”—here I opened wide the door;—             Darkness there and nothing more.      Deep into that darkness peering, long I stood there wondering, fearing, Doubting, dreaming dreams no mortal ever dared to dream before;     But the silence was unbroken, and the stillness gave no token,     And the only word there spoken was the whispered word, “Lenore?” This I whispered, and an echo murmured back the word, “Lenore!”—             Merely this and nothing more.      Back into the chamber turning, all my soul within me burning, Soon again I heard a tapping somewhat louder than before.     “Surely,” said I, “surely that is something at my window lattice;       Let me see, then, what thereat is, and this mystery explore— Let my heart be still a moment and this mystery explore;—             ’Tis the wind and nothing more!”      Open here I flung the shutter, when, with many a flirt and flutter, In there stepped a stately Raven of the saintly days of yore;     Not the least obeisance made he; not a minute stopped or stayed he;     But, with mien of lord or lady, perched above my chamber door— Perched upon a bust of Pallas just above my chamber door—             Perched, and sat, and nothing more.  Then this ebony bird beguiling my sad fancy into smiling, By the grave and stern decorum of the countenance it wore, “Though thy crest be shorn and shaven, thou,” I said, “art sure no craven, Ghastly grim and ancient Raven wandering from the Nightly shore— Tell me what thy lordly name is on the Night’s Plutonian shore!”             Quoth the Raven “Nevermore.”      Much I marvelled this ungainly fowl to hear discourse so plainly, Though its answer little meaning—little relevancy bore;     For we cannot help agreeing that no living human being     Ever yet was blessed with seeing bird above his chamber door— Bird or beast upon the sculptured bust above his chamber door,             With such name as “Nevermore.”      But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.     Nothing farther then he uttered—not a feather then he fluttered—     Till I scarcely more than muttered “Other friends have flown before— On the morrow he will leave me, as my Hopes have flown before.”             Then the bird said “Nevermore.”      Startled at the stillness broken by reply so aptly spoken, “Doubtless,” said I, “what it utters is its only stock and store     Caught from some unhappy master whom unmerciful Disaster     Followed fast and followed faster till his songs one burden bore— Till the dirges of his Hope that melancholy burden bore             Of ‘Never—nevermore’.”      But the Raven still beguiling all my fancy into smiling, Straight I wheeled a cushioned seat in front of bird, and bust and door;     Then, upon the velvet sinking, I betook myself to linking     Fancy unto fancy, thinking what this ominous bird of yore— What this grim, ungainly, ghastly, gaunt, and ominous bird of yore             Meant in croaking “Nevermore.”      This I sat engaged in guessing, but no syllable expressing To the fowl whose fiery eyes now burned into my bosom’s core;     This and more I sat divining, with my head at ease reclining     On the cushion’s velvet lining that the lamp-light gloated o’er, But whose velvet-violet lining with the lamp-light gloating o’er,             She shall press, ah, nevermore!      Then, methought, the air grew denser, perfumed from an unseen censer Swung by Seraphim whose foot-falls tinkled on the tufted floor.     “Wretch,” I cried, “thy God hath lent thee—by these angels he hath sent thee     Respite—respite and nepenthe from thy memories of Lenore; Quaff, oh quaff this kind nepenthe and forget this lost Lenore!”             Quoth the Raven “Nevermore.”      “Prophet!” said I, “thing of evil!—prophet still, if bird or devil!— Whether Tempter sent, or whether tempest tossed thee here ashore,     Desolate yet all undaunted, on this desert land enchanted—     On this home by Horror haunted—tell me truly, I implore— Is there—is there balm in Gilead?—tell me—tell me, I implore!”             Quoth the Raven “Nevermore.”      “Prophet!” said I, “thing of evil!—prophet still, if bird or devil! By that Heaven that bends above us—by that God we both adore—     Tell this soul with sorrow laden if, within the distant Aidenn,     It shall clasp a sainted maiden whom the angels name Lenore— Clasp a rare and radiant maiden whom the angels name Lenore.”             Quoth the Raven “Nevermore.”      “Be that word our sign of parting, bird or fiend!” I shrieked, upstarting— “Get thee back into the tempest and the Night’s Plutonian shore!     Leave no black plume as a token of that lie thy soul hath spoken!     Leave my loneliness unbroken!—quit the bust above my door! Take thy beak from out my heart, and take thy form from off my door!”             Quoth the Raven “Nevermore.”      And the Raven, never flitting, still is sitting, still is sitting On the pallid bust of Pallas just above my chamber door;     And his eyes have all the seeming of a demon’s that is dreaming,     And the lamp-light o’er him streaming throws his shadow on the floor; And my soul from out that shadow that lies floating on the floor             Shall be lifted—nevermore!",
  "language": "en"
}
```

**Response**:

```json
{
    "usage": {
      "text_units": 1,
      "text_characters": 6646,
      "features": 3
    },
    "sentiment": {
      "document": {
        "score": -0.632004,
        "mixed": "1",
        "label": "negative"
      }
    },
    "language": "en",
    "entities": [
      {
        "type": "Person",
        "text": "Lenore",
        "sentiment": {
          "score": -0.338845,
          "mixed": "1",
          "label": "negative"
        },
        "relevance": 0.954582,
        "emotion": {
          "sadness": 0.353997,
          "joy": 0.42867,
          "fear": 0.082587,
          "disgust": 0.006532,
          "anger": 0.00998
        },
        "count": 4,
        "confidence": 0.998531
      },
      {
        "type": "GeographicFeature",
        "text": "Nightly shore",
        "sentiment": {
          "score": -0.895883,
          "label": "negative"
        },
        "relevance": 0.57338,
        "emotion": {
          "sadness": 0.215464,
          "joy": 0.116113,
          "fear": 0.09215,
          "disgust": 0.041613,
          "anger": 0.012292
        },
        "count": 1,
        "confidence": 0.396321
      },
      {
        "type": "GeographicFeature",
        "text": "Night’s Plutonian shore",
        "sentiment": {
          "score": -0.809315,
          "label": "negative"
        },
        "relevance": 0.566144,
        "emotion": {
          "sadness": 0.228953,
          "joy": 0.354259,
          "fear": 0.072825,
          "disgust": 0.033044,
          "anger": 0.016511
        },
        "count": 1,
        "confidence": 0.130309
      },
      {
        "type": "Person",
        "text": "Madam",
        "sentiment": {
          "score": 0.720213,
          "label": "positive"
        },
        "relevance": 0.425421,
        "emotion": {
          "sadness": 0.127991,
          "joy": 0.346847,
          "fear": 0.107666,
          "disgust": 0.009068,
          "anger": 0.027072
        },
        "count": 1,
        "confidence": 0.963359
      },
      {
        "type": "Person",
        "text": "Doubting",
        "sentiment": {
          "score": -0.813998,
          "label": "negative"
        },
        "relevance": 0.413908,
        "emotion": {
          "sadness": 0.455318,
          "joy": 0.042944,
          "fear": 0.348338,
          "disgust": 0.003665,
          "anger": 0.006457
        },
        "count": 1,
        "confidence": 0.685848
      },
      {
        "type": "Time",
        "text": "midnight",
        "sentiment": {
          "score": -0.86748,
          "label": "negative"
        },
        "relevance": 0.40798,
        "emotion": {
          "sadness": 0.134522,
          "joy": 0.085251,
          "fear": 0.103739,
          "disgust": 0.006011,
          "anger": 0.109445
        },
        "count": 1,
        "confidence": 0.644079
      },
      {
        "type": "Number",
        "text": "one",
        "sentiment": {
          "score": -0.694174,
          "label": "negative"
        },
        "relevance": 0.365479,
        "emotion": {
          "sadness": 0.347826,
          "joy": 0.034769,
          "fear": 0.060945,
          "disgust": 0.125788,
          "anger": 0.074466
        },
        "count": 4,
        "confidence": 0.9984
      },
      {
        "type": "Person",
        "text": "Sir",
        "sentiment": {
          "score": 0.720213,
          "label": "positive"
        },
        "relevance": 0.326483,
        "emotion": {
          "sadness": 0.127991,
          "joy": 0.346847,
          "fear": 0.107666,
          "disgust": 0.009068,
          "anger": 0.027072
        },
        "count": 1,
        "confidence": 0.991395
      },
      {
        "type": "Person",
        "text": "craven",
        "sentiment": {
          "score": -0.895883,
          "label": "negative"
        },
        "relevance": 0.325041,
        "emotion": {
          "sadness": 0.215464,
          "joy": 0.116113,
          "fear": 0.09215,
          "disgust": 0.041613,
          "anger": 0.012292
        },
        "count": 1,
        "confidence": 0.682509
      },
      {
        "type": "Date",
        "text": "December",
        "sentiment": {
          "score": -0.632921,
          "label": "negative"
        },
        "relevance": 0.289353,
        "emotion": {
          "sadness": 0.418792,
          "joy": 0.0047,
          "fear": 0.142911,
          "disgust": 0.004732,
          "anger": 0.031847
        },
        "count": 1,
        "confidence": 0.874353
      },
      {
        "type": "Duration",
        "text": "a minute",
        "sentiment": {
          "score": -0.614232,
          "label": "negative"
        },
        "relevance": 0.280054,
        "emotion": {
          "sadness": 0.127709,
          "joy": 0.229446,
          "fear": 0.037672,
          "disgust": 0.010093,
          "anger": 0.036471
        },
        "count": 1,
        "confidence": 0.534958
      },
      {
        "type": "Location",
        "text": "Quaff, oh quaff",
        "sentiment": {
          "score": -0.981353,
          "label": "negative"
        },
        "relevance": 0.269068,
        "emotion": {
          "sadness": 0.476887,
          "joy": 0.057165,
          "fear": 0.033263,
          "disgust": 0.005294,
          "anger": 0.010591
        },
        "count": 1,
        "confidence": 0.104345
      },
      {
        "type": "Location",
        "text": "morrow",
        "sentiment": {
          "score": -0.714033,
          "mixed": "1",
          "label": "negative"
        },
        "relevance": 0.252763,
        "emotion": {
          "sadness": 0.35098,
          "joy": 0.537142,
          "fear": 0.04516,
          "disgust": 0.006254,
          "anger": 0.020569
        },
        "count": 1,
        "confidence": 0.32053
      },
      {
        "type": "Person",
        "text": "Raven",
        "sentiment": {
          "score": -0.682994,
          "label": "negative"
        },
        "relevance": 0.251641,
        "emotion": {
          "sadness": 0.292394,
          "joy": 0.293155,
          "fear": 0.08124,
          "disgust": 0.042988,
          "anger": 0.041771
        },
        "count": 1,
        "confidence": 0.436107
      },
      {
        "type": "Person",
        "text": "Prophet",
        "sentiment": {
          "score": -0.632788,
          "label": "negative"
        },
        "relevance": 0.178782,
        "emotion": {
          "sadness": 0.148805,
          "joy": 0.288454,
          "fear": 0.129026,
          "disgust": 0.020078,
          "anger": 0.063474
        },
        "count": 2,
        "confidence": 0.981271
      },
      {
        "type": "Person",
        "text": "Seraphim",
        "sentiment": {
          "score": 0,
          "label": "neutral"
        },
        "relevance": 0.177137,
        "emotion": {
          "sadness": 0.123072,
          "joy": 0.148778,
          "fear": 0.103906,
          "disgust": 0.020578,
          "anger": 0.026214
        },
        "count": 1,
        "confidence": 0.424413
      },
      {
        "type": "Person",
        "text": "Wretch",
        "sentiment": {
          "score": -0.981353,
          "label": "negative"
        },
        "relevance": 0.172934,
        "emotion": {
          "sadness": 0.476887,
          "joy": 0.057165,
          "fear": 0.033263,
          "disgust": 0.005294,
          "anger": 0.010591
        },
        "count": 1,
        "confidence": 0.512818
      },
      {
        "type": "Person",
        "text": "Tempter",
        "sentiment": {
          "score": -0.793968,
          "label": "negative"
        },
        "relevance": 0.151769,
        "emotion": {
          "sadness": 0.183974,
          "joy": 0.12621,
          "fear": 0.156215,
          "disgust": 0.013071,
          "anger": 0.027773
        },
        "count": 1,
        "confidence": 0.764221
      },
      {
        "type": "Location",
        "text": "Gilead",
        "sentiment": {
          "score": -0.793968,
          "label": "negative"
        },
        "relevance": 0.117457,
        "emotion": {
          "sadness": 0.183974,
          "joy": 0.12621,
          "fear": 0.156215,
          "disgust": 0.013071,
          "anger": 0.027773
        },
        "count": 1,
        "confidence": 0.839855
      }
    ],
    "emotion": {
      "document": {
        "emotion": {
          "sadness": 0.290143,
          "joy": 0.306887,
          "fear": 0.085799,
          "disgust": 0.027067,
          "anger": 0.041893,
          "dominant_emotion": "joy"
        }
      }
    },
    "analyzed_text": "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore—     While I nodded, nearly napping, suddenly there came a tapping, As of some one gently rapping, rapping at my chamber door. “’Tis some visitor,” I muttered, “tapping at my chamber door—             Only this and nothing more.”      Ah, distinctly I remember it was in the bleak December; And each separate dying ember wrought its ghost upon the floor.     Eagerly I wished the morrow;—vainly I had sought to borrow     From my books surcease of sorrow—sorrow for the lost Lenore— For the rare and radiant maiden whom the angels name Lenore—             Nameless here for evermore.      And the silken, sad, uncertain rustling of each purple curtain Thrilled me—filled me with fantastic terrors never felt before;     So that now, to still the beating of my heart, I stood repeating     “’Tis some visitor entreating entrance at my chamber door— Some late visitor entreating entrance at my chamber door;—             This it is and nothing more.”      Presently my soul grew stronger; hesitating then no longer, “Sir,” said I, “or Madam, truly your forgiveness I implore;     But the fact is I was napping, and so gently you came rapping,     And so faintly you came tapping, tapping at my chamber door, That I scarce was sure I heard you”—here I opened wide the door;—             Darkness there and nothing more.      Deep into that darkness peering, long I stood there wondering, fearing, Doubting, dreaming dreams no mortal ever dared to dream before;     But the silence was unbroken, and the stillness gave no token,     And the only word there spoken was the whispered word, “Lenore?” This I whispered, and an echo murmured back the word, “Lenore!”—             Merely this and nothing more.      Back into the chamber turning, all my soul within me burning, Soon again I heard a tapping somewhat louder than before.     “Surely,” said I, “surely that is something at my window lattice;       Let me see, then, what thereat is, and this mystery explore— Let my heart be still a moment and this mystery explore;—             ’Tis the wind and nothing more!”      Open here I flung the shutter, when, with many a flirt and flutter, In there stepped a stately Raven of the saintly days of yore;     Not the least obeisance made he; not a minute stopped or stayed he;     But, with mien of lord or lady, perched above my chamber door— Perched upon a bust of Pallas just above my chamber door—             Perched, and sat, and nothing more.  Then this ebony bird beguiling my sad fancy into smiling, By the grave and stern decorum of the countenance it wore, “Though thy crest be shorn and shaven, thou,” I said, “art sure no craven, Ghastly grim and ancient Raven wandering from the Nightly shore— Tell me what thy lordly name is on the Night’s Plutonian shore!”             Quoth the Raven “Nevermore.”      Much I marvelled this ungainly fowl to hear discourse so plainly, Though its answer little meaning—little relevancy bore;     For we cannot help agreeing that no living human being     Ever yet was blessed with seeing bird above his chamber door— Bird or beast upon the sculptured bust above his chamber door,             With such name as “Nevermore.”      But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.     Nothing farther then he uttered—not a feather then he fluttered—     Till I scarcely more than muttered “Other friends have flown before— On the morrow he will leave me, as my Hopes have flown before.”             Then the bird said “Nevermore.”      Startled at the stillness broken by reply so aptly spoken, “Doubtless,” said I, “what it utters is its only stock and store     Caught from some unhappy master whom unmerciful Disaster     Followed fast and followed faster till his songs one burden bore— Till the dirges of his Hope that melancholy burden bore             Of ‘Never—nevermore’.”      But the Raven still beguiling all my fancy into smiling, Straight I wheeled a cushioned seat in front of bird, and bust and door;     Then, upon the velvet sinking, I betook myself to linking     Fancy unto fancy, thinking what this ominous bird of yore— What this grim, ungainly, ghastly, gaunt, and ominous bird of yore             Meant in croaking “Nevermore.”      This I sat engaged in guessing, but no syllable expressing To the fowl whose fiery eyes now burned into my bosom’s core;     This and more I sat divining, with my head at ease reclining     On the cushion’s velvet lining that the lamp-light gloated o’er, But whose velvet-violet lining with the lamp-light gloating o’er,             She shall press, ah, nevermore!      Then, methought, the air grew denser, perfumed from an unseen censer Swung by Seraphim whose foot-falls tinkled on the tufted floor.     “Wretch,” I cried, “thy God hath lent thee—by these angels he hath sent thee     Respite—respite and nepenthe from thy memories of Lenore; Quaff, oh quaff this kind nepenthe and forget this lost Lenore!”             Quoth the Raven “Nevermore.”      “Prophet!” said I, “thing of evil!—prophet still, if bird or devil!— Whether Tempter sent, or whether tempest tossed thee here ashore,     Desolate yet all undaunted, on this desert land enchanted—     On this home by Horror haunted—tell me truly, I implore— Is there—is there balm in Gilead?—tell me—tell me, I implore!”             Quoth the Raven “Nevermore.”      “Prophet!” said I, “thing of evil!—prophet still, if bird or devil! By that Heaven that bends above us—by that God we both adore—     Tell this soul with sorrow laden if, within the distant Aidenn,     It shall clasp a sainted maiden whom the angels name Lenore— Clasp a rare and radiant maiden whom the angels name Lenore.”             Quoth the Raven “Nevermore.”      “Be that word our sign of parting, bird or fiend!” I shrieked, upstarting— “Get thee back into the tempest and the Night’s Plutonian shore!     Leave no black plume as a token of that lie thy soul hath spoken!     Leave my loneliness unbroken!—quit the bust above my door! Take thy beak from out my heart, and take thy form from off my door!”             Quoth the Raven “Nevermore.”      And the Raven, never flitting, still is sitting, still is sitting On the pallid bust of Pallas just above my chamber door;     And his eyes have all the seeming of a demon’s that is dreaming,     And the lamp-light o’er him streaming throws his shadow on the floor; And my soul from out that shadow that lies floating on the floor             Shall be lifted—nevermore!"
  }
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
