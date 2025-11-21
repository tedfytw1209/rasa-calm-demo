from typing import Any, Dict, List, Text

# High-level grouping: component -> list of CSV columns (as before)
COMPONENT_TO_COLUMNS: Dict[str, List[str]] = {
    "objectives": [
        "Objectives",
        "SampleSize",
        "DataSourceType",
    ],
    "eligibility": [
        "Population",
        "InclusionCriteria_norm",
        "ExclusionCriteria_norm",
        "Computablephenotype",
        "Population Evaluation",
    ],
    "treatment_strategies": [
        "TreatmentGroup",
        "ClinicalDomain",
        "DoseSchedule",
        "DoseSchedule_norm",
        "identify the exposure",
        "definitions of vaccinated status",
        "Context",
        "ComparatorGroup",
        "ComparatorDetails",
        "ExposureValidation",
        "GracePeriod",
    ],
    "treatment_assignment": [
        "IndexDate_norm",
        "Methods.Final",
        "MatchingCaliper",
        "PsVariables",
        "ConfounderSelection",
        "Observation Period",
        "SmdAfterEmulation",
        "SmdDetails",
        "UnmeasuredConfounders",
        "UnmeasuredConfounders Model",
        "Timealignment.Final",
    ],
    "outcomes": [
        "PrimaryOutcome",
        "outcomes definations",
        "Validation",
        "Codes",
        "CompetingRisks",
        "NegativeControls",
        "SecondaryOutcomes",
        "Secondary defination",
        "SafetyOutcomes",
    ],
    "follow_up": [
        "Start",
        "lag time",
        "End",
        "CensoringRules",
        "TreatmentSwitching",
        "MedianTime",
    ],
    "causal_contrasts": [
        "AnalysisApproach.Final",
    ],
    "statistical_analysis": [
        "Models.Final",
        "EffectMetrics.Final",
        "SensitivityAnalyses",
        "SubgroupAnalyses",
        "SubgroupModel",
        "MissingDataApproach",
        "MissingDataApproachOther",
        "Multiplicity",
        "Software",
    ],
}


# Derive a field key mapping like "eligibility.Population" -> "Population"
FIELD_TO_COLUMN: Dict[str, str] = {}
for component, cols in COMPONENT_TO_COLUMNS.items():
    for col in cols:
        key = f"{component}.{col}"
        FIELD_TO_COLUMN[key] = col