import { Col, Row } from 'antd';
import Form from 'antd/lib/form/Form';
import FormDatePicker from 'components/FormDatePicker';
import FormInput from 'components/FormInput';
import FormInputNumber from 'components/FormInputNumber';
import FormSelect from 'components/FormSelect';
import {
  DESIGN_SCORE_OPTIONS,
  JACKUP_LABELS as labels,
  RIG_STATUS_OPTIONS,
  TOPSIDE_DESIGN_OPTIONS,
} from 'consts/rigs';
import { FormValues } from 'containers/UpdateJackupForm';
import { prettyPlaceholder, toLowerCaseFirstLetter } from 'utils/format';

const JackupGeneralStep = () => {
  return (
    <Form layout="vertical">
      <Row gutter={35}>
        <Col span={12}>
          <FormInput<FormValues>
            name="name"
            formItemProps={{ label: labels.name }}
            inputProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(labels.name)}`,
            }}
          />
          <FormInput<FormValues>
            name="manager"
            formItemProps={{ label: labels.manager }}
            inputProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(labels.manager)}`,
            }}
          />
          <FormInput<FormValues>
            name="design"
            formItemProps={{ label: labels.design }}
            inputProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(labels.design)}`,
            }}
          />
          <FormInput<FormValues>
            name="build_yard"
            formItemProps={{ label: labels.build_yard }}
            inputProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(labels.build_yard)}`,
            }}
          />
          <FormSelect<FormValues>
            name="rig_status"
            formItemProps={{ label: labels.rig_status }}
            options={RIG_STATUS_OPTIONS}
            selectInputProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(labels.rig_status)}`,
            }}
          />
          <FormDatePicker<FormValues>
            name="delivery_date"
            formItemProps={{ label: labels.delivery_date }}
            datePickerProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(
                labels.delivery_date,
              )}`,
            }}
          />
          <FormDatePicker<FormValues>
            name="special_survey_due"
            formItemProps={{ label: labels.special_survey_due }}
            datePickerProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(
                labels.special_survey_due,
              )}`,
            }}
          />
          <FormDatePicker<FormValues>
            name="end_of_last_contract"
            formItemProps={{ label: labels.end_of_last_contract }}
            datePickerProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(
                labels.end_of_last_contract,
              )}`,
            }}
          />
        </Col>
        <Col span={12}>
          <FormInputNumber<FormValues>
            name="months_in_operation_last_year"
            formItemProps={{ label: labels.months_in_operation_last_year }}
            inputNumberProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(
                labels.months_in_operation_last_year,
              )}`,
            }}
          />
          <FormInputNumber<FormValues>
            name="months_in_operation_last_3_years"
            formItemProps={{ label: labels.months_in_operation_last_3_years }}
            inputNumberProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(
                labels.months_in_operation_last_3_years,
              )}`,
            }}
          />
          <FormSelect<FormValues>
            name="topside_design"
            formItemProps={{ label: labels.topside_design }}
            options={TOPSIDE_DESIGN_OPTIONS}
            selectInputProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(
                labels.topside_design,
              )}`,
            }}
          />
          <FormSelect<FormValues>
            name="design_score"
            formItemProps={{ label: labels.design_score }}
            options={DESIGN_SCORE_OPTIONS}
            selectInputProps={{
              placeholder: `Enter ${toLowerCaseFirstLetter(
                labels.design_score,
              )}`,
            }}
          />
          <FormInputNumber<FormValues>
            name="day_rate"
            formItemProps={{ label: labels.day_rate }}
            inputNumberProps={{
              placeholder: prettyPlaceholder`Enter ${labels.day_rate}`,
            }}
          />
          <FormInputNumber<FormValues>
            name="spread_cost"
            formItemProps={{ label: labels.spread_cost }}
            inputNumberProps={{
              placeholder: prettyPlaceholder`Enter ${labels.spread_cost}`,
            }}
          />
          <FormInputNumber<FormValues>
            name="tugs_no_used"
            formItemProps={{ label: labels.tugs_no_used }}
            inputNumberProps={{
              placeholder: prettyPlaceholder`Enter ${labels.tugs_no_used}`,
            }}
          />
          <FormInputNumber<FormValues>
            name="jack_up_time"
            formItemProps={{ label: labels.jack_up_time }}
            inputNumberProps={{
              placeholder: prettyPlaceholder`Enter ${labels.jack_up_time}`,
            }}
          />
          <FormInputNumber<FormValues>
            name="jack_down_time"
            formItemProps={{ label: labels.jack_down_time }}
            inputNumberProps={{
              placeholder: prettyPlaceholder`Enter ${labels.jack_down_time}`,
            }}
          />
        </Col>
      </Row>
    </Form>
  );
};

export default JackupGeneralStep;
