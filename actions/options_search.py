from typing import Any, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from actions.db import get_options_for_field

class OptionsSearch(Action):

    def name(self) -> str:
        return "action_options_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[str, Any]):
        tte_field = tracker.slots.get("tte_field")
        if not tte_field:
            dispatcher.utter_message(
                text=(
                    "I couldn't detect which protocol field you want options for. "
                    "Please specify one, such as eligibility, treatment_assignment, outcomes, etc."
                )
            )
            return [SlotSet("option_search_finish", False)]
        options = get_options_for_field(tte_field)
        if not options:
            dispatcher.utter_message(
                text=(
                    "I couldn't identify which specific subcomponent you want options for. "
                    "Please mention something like 'eligibility population', "
                    "'dose schedule', or 'time alignment new-user design'."
                )
            )
            return [SlotSet("option_search_finish", False)]
        options_list = "\n".join([o.stringify().strip('\n') for o in options])
        return [SlotSet("options_list", options_list), SlotSet("option_search_finish", True)]