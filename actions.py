# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import csv
from pathlib import Path
from typing import Any, Counter, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd




class ActionGetMovieOnGenre(Action):

    def name(self) -> Text:
        return "action_get_movie_on_genre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #getting the slot value and storing into the genres slot value
        genres_slot = tracker.get_slot('genres')
        #reading the csv file
        with open('C:/Users/titio/fyp/prototype/data/imdb_top_1000.csv', 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            #getting a list of movies matching the criteria
            output = [row for row in reader if row['Genre'][0].lower() == genres_slot]
        if output:
            #if the list is not null, return movie title
            reply = f"Here are some {genres_slot} Movies:"
            reply += "\n-" + "\n-".join([item['Series_Title'] for item in output])
            dispatcher.utter_message(reply)
        else:
            #if the list is empty, tell user that no matches were found
            dispatcher.utter_message(f"I couldn't find any {genres_slot} movies")


        
    




