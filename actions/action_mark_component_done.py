from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionMarkComponentDone(Action):
    def name(self) -> Text:
        return "action_mark_component_done"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        current_component = tracker.get_slot("current_component")
        events: List[Dict[Text, Any]] = []

        component_to_slot = {
            "objectives": "objectives_done",
            "eligibility": "eligibility_done",
            "treatment_strategies": "treatment_strategies_done",
            "treatment_assignment": "treatment_assignment_done",
            "outcomes": "outcomes_done",
            "follow_up": "follow_up_done",
            "causal_contrasts": "causal_contrasts_done",
            "statistical_analysis": "statistical_analysis_done",
        }

        if current_component in component_to_slot:
            done_slot = component_to_slot[current_component]
            events.append(SlotSet(done_slot, True))

        return events
