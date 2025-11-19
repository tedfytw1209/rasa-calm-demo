from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import json

class ActionExportProtocolJson(Action):
    def name(self) -> Text:
        return "action_export_protocol_json"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        finish = tracker.get_slot("finish")
        if not finish:
            # Not finished yet; nothing to export
            dispatcher.utter_message(
                text="The protocol is not fully complete yet. We can keep working on it."
            )
            return []

        # Build a simple nested JSON structure.
        # For now, we only include eligibility – you can expand later.
        protocol = {
            "objectives": None,  # TODO: add once you implement objectives slots
            "eligibility": {
                "population": tracker.get_slot("eligibility_population"),
                "inclusion_criteria": tracker.get_slot("eligibility_inclusioncriteria"),
                "exclusion_criteria": tracker.get_slot("eligibility_exclusioncriteria"),
                "computable_phenotype": tracker.get_slot("eligibility_computablephenotype"),
                "population_evaluation": tracker.get_slot("eligibility_population_evaluation"),
            },
            "treatment_strategies": None,      # TODO
            "treatment_assignment": None,      # TODO
            "outcomes": None,                  # TODO
            "follow_up": None,                 # TODO
            "causal_contrasts": None,          # TODO
            "statistical_analysis": None       # TODO
        }

        json_str = json.dumps(protocol, indent=2, ensure_ascii=False)
        dispatcher.utter_message(text=f"Here is your current TTE protocol JSON:\n```json\n{json_str}\n```")

        return []
