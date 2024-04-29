# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

data = [
    "Transfer Learning",
    "Transformer",
    "CNN",
    "RNN",
    "LSTM",
    "Mamba",
    "Math",
    "English",
    "Science",
    "History"
] 

class ActionWhatToLearn(Action):

    def name(self) -> Text:
        return "action_what_to_learn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        number_of_courses = random.randint(1, len(data))
        courses = random.sample(data, number_of_courses)
        courses = ', '.join(courses)
        dispatcher.utter_message(f"Hôm nay anh/chị có thể học về: {courses}")
        return []
