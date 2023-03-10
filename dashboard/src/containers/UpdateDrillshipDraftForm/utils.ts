import { DraftFormSteps } from 'consts/rigs';
import { UpdateCustomDrillship } from 'api/schema';
import {
  getCapacitiesValidationSchema,
  getGeneralValidationSchema,
  getOperationValidationSchema,
} from 'containers/UpdateDrillshipForm/schema';

export const stepValidationSchemas = {
  [DraftFormSteps.GENERAL]: getGeneralValidationSchema(false),
  [DraftFormSteps.CAPACITIES]: getCapacitiesValidationSchema(false),
  [DraftFormSteps.OPERATION]: getOperationValidationSchema(false),
};

export const stepFieldMap: {
  [key in DraftFormSteps]: (keyof UpdateCustomDrillship)[];
} = {
  [DraftFormSteps.GENERAL]: [
    'name',
    'manager',
    'design',
    'build_yard',
    'rig_status',
    'delivery_date',
    'special_survey_due',
    'end_of_last_contract',
    'months_in_operation_last_year',
    'months_in_operation_last_3_years',
    'design_score',
    'equipment_load',
    'topside_design',
    'drillfloor_efficiency',
    'day_rate',
    'spread_cost',
    'tugs_no_used',
    'draft',
  ],
  [DraftFormSteps.CAPACITIES]: [
    'quarters_capacity',
    'rig_water_depth',
    'variable_load',
    'hull_concept_score',
    'hull_design_eco_score',
    'dp',
    'dp_class',
    'draft_depth',
    'displacement',
    'hull_breadth',
    'hull_depth',
    'hull_length',
    'derrick_height',
    'derrick_capacity',
    'dual_derrick',
    'drawworks_power',
    'active_heave_drawwork',
    'cmc_with_active_heave',
    'ram_system',
    'total_cranes',
    'crane_capacity',
    'riser_on_board_outfitted',
    'riser_storage_inside_hull',
    'split_funnels_free_stern_deck',
    'total_bop_rams',
    'bop_diameter_wp_max',
    'bop_wp_max',
    'number_of_bop_stacks',
    'mudpump_quantity',
    'liquid_mud',
    'mud_total_power',
    'shaleshaker_total',
    'engine_power',
    'engine_quantity',
    'engine_total',
    'generator_power',
    'generator_quantity',
    'generator_total',
    'draft',
  ],
  [DraftFormSteps.OPERATION]: [
    'tripsaver',
    'offline_stand_building',
    'auto_pipe_handling',
    'dual_activity',
    'drilltronic',
    'dynamic_drilling_guide',
    'process_automation_platform',
    'automatic_tripping',
    'closed_bus',
    'scr',
    'hybrid',
    'hvac_heat_recovery',
    'freshwater_cooling_systems',
    'seawater_cooling_systems',
    'operator_awareness_dashboard',
    'hpu_optimization',
    'optimized_heat_tracing_system',
    'floodlighting_optimization',
    'vfds_on_aux_machinery',
    'draft',
  ],
};
