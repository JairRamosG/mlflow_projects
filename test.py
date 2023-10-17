# conectar al 8787 para acceso al api

file:///home/ubuntu/projects/mlflow_projects/mlruns/0/74588070fbcd41428d077f567e282c19/artifacts/model

mlflow models serve -m file:///home/ubuntu/projects/mlflow_projects/mlruns/0/74588070fbcd41428d077f567e282c19/artifacts/model -p 8787 -h 0.0.0.0



# la mia
curl ec2-3-88-206-103.compute-1.amazonaws.com:8787/invocations -H 'Content-Type: application/json' -d '{"dataframe_split": {"columns":["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"],"data":[[17.99000,10.38000,122.80000,1001.00000,0.11840,0.27760,0.30010,0.14710,0.24190,0.07871,1.09500,0.90530,8.58900,153.40000,0.00640,0.04904,0.05373,0.01587,0.03003,0.00619,25.38000,17.33000,184.60000,2019.00000,0.16220,0.66560,0.71190,0.26540,0.46010,0.11890]]}}'
