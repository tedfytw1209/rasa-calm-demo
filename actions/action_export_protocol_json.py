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
        # Build a nested JSON structure for all components
        protocol: Dict[str, Any] = {
            "objectives": {
                "objectives": tracker.get_slot("objectives_objectives"),
                "sample_size": tracker.get_slot("objectives_samplesize"),
                "data_source_type": tracker.get_slot("objectives_datasourcetype"),
            },
            "eligibility": {
                "population": tracker.get_slot("eligibility_population"),
                "inclusion_criteria": tracker.get_slot("eligibility_inclusioncriteria"),
                "exclusion_criteria": tracker.get_slot("eligibility_exclusioncriteria"),
                "computable_phenotype": tracker.get_slot("eligibility_computablephenotype"),
                "population_evaluation": tracker.get_slot("eligibility_population_evaluation"),
            },
            "treatment_strategies": {
                "treatment_group": tracker.get_slot("treatment_strategies_treatmentgroup"),
                "clinical_domain": tracker.get_slot("treatment_strategies_clinicaldomain"),
                "dose_schedule": tracker.get_slot("treatment_strategies_doseschedule"),
                "identify_the_exposure": tracker.get_slot("treatment_strategies_identify_the_exposure"),
                "definitions_of_vaccinated_status": tracker.get_slot("treatment_strategies_definitions_of_vaccinated_status"),
                "context": tracker.get_slot("treatment_strategies_context"),
                "comparator_group": tracker.get_slot("treatment_strategies_comparatorgroup"),
                "comparator_details": tracker.get_slot("treatment_strategies_comparatordetails"),
                "exposure_validation": tracker.get_slot("treatment_strategies_exposurevalidation"),
                "grace_period": tracker.get_slot("treatment_strategies_graceperiod"),
            },
            "treatment_assignment": {
                "index_date": tracker.get_slot("index_date"),
                "time_alignment": tracker.get_slot("timealignment"),
                "time_alignment_other": tracker.get_slot("timealignment_other"),
            },
            "outcomes": {
                "primary_outcome": tracker.get_slot("outcomes_primaryoutcome"),
                "outcomes_definitions": tracker.get_slot("outcomes_outcomes_definations"),
                "validation": tracker.get_slot("outcomes_validation"),
                "codes": tracker.get_slot("outcomes_codes"),
                "competing_risks": tracker.get_slot("outcomes_competingrisks"),
                "negative_controls": tracker.get_slot("outcomes_negativecontrols"),
                "secondary_outcomes": tracker.get_slot("outcomes_secondaryoutcomes"),
                "secondary_definition": tracker.get_slot("outcomes_secondary_defination"),
                "safety_outcomes": tracker.get_slot("outcomes_safetyoutcomes"),
            },
            "follow_up": {
                "start": tracker.get_slot("follow_up_start"),
                "lag_time": tracker.get_slot("follow_up_lag_time"),
                "end": tracker.get_slot("follow_up_end"),
                "censoring_rules": tracker.get_slot("follow_up_censoringrules"),
                "treatment_switching": tracker.get_slot("follow_up_treatmentswitching"),
                "median_time": tracker.get_slot("follow_up_mediantime"),
            },
            "causal_contrasts": {
                "analysis_approach": tracker.get_slot("causal_contrasts_analysisapproach"),
                "analysis_approach_other": tracker.get_slot("causal_contrasts_other"),
            },
            "statistical_analysis": {
                "models": tracker.get_slot("statistical_analysis_models"),
                "effect_metrics": tracker.get_slot("statistical_analysis_effectmetrics"),
                "sensitivity_analyses": tracker.get_slot("statistical_analysis_sensitivityanalyses"),
                "subgroup_analyses": tracker.get_slot("statistical_analysis_subgroupanalyses"),
                "subgroup_model": tracker.get_slot("statistical_analysis_subgroupmodel"),
                "missing_data_approach": tracker.get_slot("statistical_analysis_missingdataapproach"),
                "missing_data_approach_other": tracker.get_slot("statistical_analysis_missingdataapproachother"),
                "software": tracker.get_slot("statistical_analysis_software"),
            },
        }

        json_str = json.dumps(protocol, indent=2, ensure_ascii=False)
        dispatcher.utter_message(
            text=f"Here is your completed TTE protocol JSON:\n```json\n{json_str}\n```"
        )

        return []
