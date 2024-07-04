from airtable import (get_rota_for_day,
get_employee_data,
get_floor_data,
get_task_data,
get_unavailability_data)

from flask import Flask, request, jsonify, make_response
import datetime
import os



# Airtable setup
api_key = os.getenv('AIRTABLE_API_KEY')
base_id = os.getenv('AIRTABLE_BASE_ID')

# Airtable tables



# Main validation logic
def validate_rota():
  validate_start_times(rota=rota_data)






if __name__ == "__main__":
  print("rota_data: \n".upper(), rota_data)
  print("employee_data: \n".upper(), employee_data)
  print("floor_data: \n".upper(), floor_data)
  print("task_data: \n".upper(), task_data)
  print("unavailability_data: \n".upper(), unavailability_data)








date = "2023-01-20"
rota_data = get_rota_for_day(date)
employee_data = get_employee_data()
floor_data = get_floor_data()
task_data = get_task_data()
unavailability_data = get_unavailability_data(date)

# Check all start times are from 9 and 16 (inclusive)
def validate_start_times(rota, earliest_start_time=9, latest_start_time=16):
  for assignment in rota:
    assert earliest_start_time <= assignment[3] <= latest_start_time, "START TIME ERROR: Start time must be between 9 and 16"
  print("SUCCESSFUL START TIMES!")


#Check Each employee is assigned at most one task per time slot
def validate_only_one_task_at_a_time():
  for e in employees:
      for t in range(9, 17):
          model.Add(sum(assignments[(e, t, task)]
                        for task in floor_data['Tasks List'] if task in employees[e]['Tasks']) <= 1)



# Check Each employee should have 1 and only 1 hour-long break every day
def validate_break_exists_and_duration(number_of_breaks=1, duration=1):
  for e in employees:
      model.Add(sum(breaks[(e, t)] for t in range(11, 15)) == 1)

# Check break start times are between 11 and 14 (inclusive)
def validate_break_time_start(breaks):
  for t in breaks:
    assert t >= 11 and t <15
    breaks = {}
    for e in employees:
        for t in range(11, 15):  # Breaks between 11am and 3pm
            breaks[(e, t)] = model.NewBoolVar(f'break_{e}_{t}')


# Check All tasks on a floor should have the required number of employees assigned throughout the day
def validate_enough_employees_assigned():
  for task in floor_data['Tasks List']:
      for t in range(9, 17):
          model.Add(sum(assignments[(e, t, task)] for e in employees if task in employees[e]['Tasks']) ==
                    task_data[task]['Employees Required'])


# Check Each employee should not perform any given task for more than 2 back-to-back hours
def validate_back_to_back_hours(max_back_to_back=2):
  for e in employees:
    for task in floor_data['Tasks List']:
        if task in employees[e]['Tasks']:
            for start_time in range(9, 15):  # Check from 9 am to 2 pm (for 3-hour windows)
                model.Add(sum(assignments[(e, t, task)]
                              for t in range(start_time, start_time + 3)) <= 2)




