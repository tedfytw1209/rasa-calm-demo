from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import json

class ActionCheckFinishPipeline(Action):
    def name(self) -> Text:
        return "action_check_finish_pipeline"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # If you want to require ALL components to be completed:
        required_done_slots = [
            "objectives_done",
            "eligibility_done",
            "treatment_strategies_done",
            "treatment_assignment_done",
            "outcomes_done",
            "follow_up_done",
            "causal_contrasts_done",
            "statistical_analysis_done",
        ]

        all_done = True
        for s in required_done_slots:
            if not tracker.get_slot(s):
                all_done = False
                break

        # Set finish slot
        events = [SlotSet("finish", all_done)]

        # Optional: say something to the user (or keep it silent)
        if all_done:
            dispatcher.utter_message(
                text="You have completed all components of the TTE protocol."
            )
        else:
            dispatcher.utter_message(
                text="Some components are still incomplete. Let's continue."
            )

        return events
