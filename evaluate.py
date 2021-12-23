"""Evaluates the skill score for the WPD Data Challenge (Part 1)

Usage:
    1. Place the truth file (MW_Staplegrove_CB905_MW_target_variable_half_hourly_max_min_real_power_MW_september.csv) 
    in the same folder as this script 
    2. Ensure your submission file has the correct headers and rows (see competition instructions) and then run:

    python evaluate.py [your_submission_file.csv]

Output:
    Prints the skill score relative to the benchmark
"""
import sys
import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

submission_answer_file = sys.argv[1]
truth_file = "MW_Staplegrove_CB905_MW_target_variable_half_hourly_max_min_real_power_MW_september.csv"
# This is the RMSE for the benchmark (taking the 30 minute average as both the max and min)
benchmark = 0.3814225068702593

truth = pd.read_csv(truth_file)
pred = pd.read_csv(submission_answer_file)

# Rather than fiddle with date formats, we just check there are the right number of rows
# and assume they are in the correct order
if len(pred) == len(truth):
    merged = truth.merge(pred, left_index=True, right_index=True, suffixes = ('_true', '_pred'), how = 'left')
else:
    raise Exception("The submitted file does not have the right number of rows. Please ensure it matches the template")

# Calculate combined RMSE for max and min
result = sqrt(mean_squared_error(merged['value_min_true'], merged['value_min_pred'])
            + mean_squared_error(merged['value_max_true'], merged['value_max_pred']))

# Convert into skill score
result = result / benchmark

if(np.isnan(result)):
    result = 999

print(f'skill_score: {result}')