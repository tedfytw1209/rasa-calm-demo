from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
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
        component_done_map: Dict[Text, Text] = {
            "objectives": "objectives_done",
            "eligibility": "eligibility_done",
            "treatment_strategies": "treatment_strategies_done",
            "treatment_assignment": "treatment_assignment_done",
            "outcomes": "outcomes_done",
            "follow_up": "follow_up_done",
            "causal_contrasts": "causal_contrasts_done",
            "statistical_analysis": "statistical_analysis_done",
        }

        unfinished_components: List[Text] = []

        for component, done_slot in component_done_map.items():
            done_value = tracker.get_slot(done_slot)
            if not done_value:
                unfinished_components.append(component)

        all_done = len(unfinished_components) == 0

        events: List[EventType] = [
            SlotSet("finish", all_done),
        ]

        # Optional: say something to the user (or keep it silent)
        if all_done:
            dispatcher.utter_message(
                text="You have completed all components of the TTE protocol."
            )
        else:
            next_component = unfinished_components[0]
            events.append(SlotSet("current_component", next_component))
            events.append(
                SlotSet("unfinished_components", ", ".join(unfinished_components))
            )

            dispatcher.utter_message(
                text=(
                    "Some components are still incomplete. "
                    f"Unfinished components: {', '.join(unfinished_components)}."
                )
            )

        return events
