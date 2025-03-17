#import dataframe libraries, mathematics libraries
import pandas as pd #this library contains functions which can manipulate dataframes. 
import numpy as np #this library contains functions which deal with mathematical operations and functions.
import math
import re #importing re for regex

#visualisation libraries
import matplotlib.pyplot as plt
import seaborn as sns 

#preprocessing libraries
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

#for Linear Regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# For Regression Models
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.linear_model import LinearRegression, Lasso, Ridge, SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, VotingRegressor, HistGradientBoostingRegressor, GradientBoostingRegressor  
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.decomposition import PCA 
# Data Preprocessing
from sklearn.preprocessing import LabelEncoder, StandardScaler  # Encoding categorical variables and scaling numerical features
from sklearn.model_selection import train_test_split  # Splitting data into train and test sets

# Dimensionality Reduction
from sklearn.decomposition import PCA  # Principal Component Analysis for feature reduction

# Feature Selection
from sklearn.feature_selection import chi2, mutual_info_classif, SelectKBest  # Feature selection techniques

# Ensemble Learning Models
from sklearn.ensemble import RandomForestClassifier  # Used for feature importance in tree-based selection

# Recursive Feature Elimination
from sklearn.feature_selection import RFE  # Used for recursive feature elimination


import pickle




#Unpickle

# Encoder
ohe_file = r"OHE_census.pkl"


# Load the pickled object
with open(ohe_file, "rb") as file:
    OHE_model = pickle.load(file)

#---


# MinMax
MinMaxtransformer_pickle_file = r"MinMaxtransformer.pkl" 

# Load the pickled object
with open(MinMaxtransformer_pickle_file, "rb") as file:
    MinMax_model = pickle.load(file)

    
#---


# PCA
filename = r"rfr_remain_work_qty.p" 

# Load the pickled object
with open(filename, "rb") as file:
    rfr_model = pickle.load(file)
    
    



schdule = pd.read_csv('joined_TASK_RSRC_WBS_with pivot table on total time difference.csv')
schdule = schdule.drop(columns=['cstr_date','act_start_date','act_end_date','expect_end_date','cstr_type',
                                'suspend_date','resume_date','float_path','float_path_order',
                                'cstr_date2','cstr_type2','act_this_per_work_qty','act_this_per_equip_qty',
                                'external_early_start_date','external_late_end_date','create_user','update_user',
                                'role_id','shift_id','user_id','pobs_id','email_addr','employee_code','office_phone',
                                'other_phone','rsrc_title_name','def_qty_per_hr','cost_qty_type','ot_factor',
                                'unit_id','rsrc_notes','load_tasks_flag','level_flag','last_checksum','obs_id','phase_id',
                                'ev_user_pct','ev_etc_user_value','orig_cost','indep_remain_total_cost','ann_dscnt_rate_pct',
                                'dscnt_period_type','indep_remain_work_qty','anticip_start_date','anticip_end_date',
                                'ev_compute_type','ev_etc_compute_type','plan_open_state','act time difference',
                                'Unnamed: 112','Unnamed: 113','tmpl_guid'],axis=1)
schdule.dropna(subset = ['rsrc_id', 'parent_rsrc_id','guid'], how='any', inplace=True)
#DROP THE TARGET VARIABLE FOR THIS EXAMPLE:
schdule = schdule.drop(columns=['remain_work_qty'])





X = schdule[['task_name',
 'total_float_hr_cnt',
 'task_code',
 'wbs_name',
 'seq_num',
 'rem_late_end_date',
 'wbs_short_name',
 'late_end_date',
 'rem_late_start_date',
 'late_start_date',
 'reend_date',
 'target_start_date',
 'restart_date',
 'early_start_date',
 'task_id',
 'target_end_date',
 'early_end_date',
 'wbs_id',
 'parent_wbs_id',
 'guid']]
X=X.reset_index(drop = True)



##############################################################################
#splitting X values in to Categoric and Numerical data

numerical=[
'total_float_hr_cnt','seq_num','task_id']
categorical = ['task_name',
 'task_code',
 'wbs_name',
 'wbs_short_name',
 'wbs_id',
 'parent_wbs_id',
 'guid']

###############################################################################
#associating numerical and categorical data to train, test and validate

#if possible, we want to hand-pick our columns - depending on the number of columns we have
#split train data
X_train_numerical = X[numerical]
X_train_categorical_ohe = X[categorical]



#Train
X_train_normalized = MinMax_model.transform(X_train_numerical)
X_train_minmax = pd.DataFrame(X_train_normalized,columns=X_train_numerical.columns)
#X_train_minmax.head()


# Train
encoded_for_p_train = OHE_model.transform(X_train_categorical_ohe).toarray()
cols = OHE_model.get_feature_names_out(input_features=X_train_categorical_ohe.columns)
X_train_ohe = pd.DataFrame(encoded_for_p_train, columns=cols)



#Train
X_train_scaled_minmax = pd.concat([X_train_minmax,X_train_ohe], axis = 1)



y_test_pred = rfr_model.predict(X_train_scaled_minmax)


#resources = pd.read_csv('joined_TASK_RSRC_WBS_with pivot table on total time difference.csv')


results  = pd.concat([schdule.reset_index(), pd.DataFrame(y_test_pred, columns=['Pred_remainign work'])], axis=1)[['rsrc_short_name', 'Pred_remainign work']]

results.to_csv('results.csv')
