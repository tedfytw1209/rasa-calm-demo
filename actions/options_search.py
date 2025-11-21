from typing import Any, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from actions.db import get_options_for_component


class OptionsSearch(Action):

    def name(self) -> str:
        return "action_options_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[str, Any]):
        component = tracker.slots.get("component")
        options = get_options_for_component(tracker.sender_id, component)
        options_list = "\n".join([o.stringify().strip('\n') for o in options])
        return [SlotSet("options_list", options_list)]