# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset

from datetime import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.types import DomainDict



# class ActionQtdPeople(Action):

#     def name(self) -> Text:
#         return "action_calc_people"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         global qtd_people
#         qtd_people=tracker.get_slot("qtd_people")
#         # qtd_people = tracker.get_slot("qtd_people")
#         # qtd_people_2 = next(tracker.get_latest_entity_values("qtd_people"), None)                    
                                                             

#         if(int(qtd_people)<=0):
#             dispatcher.utter_message(text="entrada inválida :(")
#             return [SlotSet(key = "qtd_people", value = None)]
#         else:    
#             dispatcher.utter_message(text="entrada válida ;)")

#         return []



# class ActionValidadeTime(Action):

#     def name(self) -> Text:
#         return "action_val_time"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         global time
#         time=tracker.get_slot("time")   
#         # hora_min = datetime.strptime(time, '%H:%M')                
                                                             

#         try:
#             hora_min = datetime.strptime(time, '%H:%M') 
#             dispatcher.utter_message(text="entrada válida!")
            
#         except ValueError: 
#             dispatcher.utter_message(text="entrada inválida ;)")
#             return [SlotSet(key = "time", value = None)]
        
#         # if (hora_min>='23:59' or hora_min<='00:00'):
#         #     dispatcher.utter_message(text="entrada inválida ;)")
#         #     return [SlotSet(key = "time", value = None)]
#         # else:    
#         #     dispatcher.utter_message(text="entrada válida!")

#         return []









class ValidateChurrascariaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_churrascaria_form"
    
    def validate_qtd_people(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate qtd_people value."""

        # global qtd_people
        # qtd_people=tracker.get_slot("qtd_people")                                                                  
        # if(int(qtd_people)<=0): 
        print(slot_value)
        if(int(slot_value)<=0): 
            dispatcher.utter_message(text="entrada inválida qtd people :(")
            # return [SlotSet(key = "qtd_people", value = None)]
            return {"qtd_people": None}
        else:    
            dispatcher.utter_message(text="entrada válida ;)")
            return {"qtd_people": slot_value}

    def validate_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate time value."""

        # global time
        # time=tracker.get_slot("time")                                                         
        try:
            # hora_min = datetime.strptime(time, '%H:%M') 
            hora_min = datetime.strptime(slot_value, '%H:%M') 
            dispatcher.utter_message(text="entrada válida ;)")
            return {"time": slot_value}
            
        except ValueError: 
            dispatcher.utter_message(text="entrada inválida time :(")
            # return [SlotSet(key = "time", value = None)]
            return {"time": None}



class ActionResetSlots(Action):

    def name(self) -> Text:
        return "action_reset_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]





