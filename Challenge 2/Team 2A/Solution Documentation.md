# Solution Documentation

## File Directory
The project is structured as follows:
```
Repository/
│-- .git/                 # Git repository tracking
│-- .Rproj.user/          # R project metadata
│-- app/                  # Application files
│-- data/                 # Data sources and processed datasets
│-- images/               # Generated plots and visualizations
│-- .gitignore            # Specifies files to ignore in Git
│-- Hack24.Rproj          # R project file
│-- clean_data.R          # Data cleaning and preprocessing
│-- clustering.R          # Risk clustering analysis
│-- Forecast_area_chart.R # Area chart visualization for cost forecasting
│-- Forecasting_pre_post_cost.R # Forecasting pre/post-factored costs
│-- hack_format_data.R    # Loads necessary R packages
│-- metric_calculation.R  # Computes risk-related metrics
│-- metric_visualisation.R # Visualizes calculated risk metrics
│-- predict_costs.R       # Predicts cost savings using machine learning
│-- rosa_test.r           # Test script
│-- test.R                # Test script
```

## Specific Files
### `clean_data.R`
This script loads, cleans, and processes risk and mitigation data, ensuring data integrity before analysis.

### `clustering.R`
Performs risk clustering based on co-occurrence within projects, applies hierarchical clustering, and calculates centrality measures and mitigation effectiveness.

### `Forecast_area_chart.R`
Creates area charts to visualize pre-factored and post-factored costs over time, using ARIMA forecasting models for predictions.

### `Forecasting_pre_post_cost.R`
Forecasts pre/post-factored costs and generates bar charts and category-wise breakdowns of cost trends.

### `hack_format_data.R`
Loads necessary R packages required for data processing, modeling, and visualization.

### `metric_calculation.R`
Computes key risk-related metrics, including:
- Risk velocity (speed of escalation)
- Mitigation success rates
- Emergence rates of new risks
- Probability and cost drift over time
- Resolution rates for risk closure

### `metric_visualisation.R`
Generates visualizations for risk metrics, including:
- Scatter plots & Sankey diagrams for risk velocity
- Bar charts & density plots for mitigation effectiveness
- Emergence rate trend graphs
- Probability & cost drift plots

### `predict_costs.R`
Predicts pre-mitigation and post-mitigation costs using a random forest model. It clusters risks, trains models, and estimates potential cost savings.

### `rosa_test.r`
A test script used for basic testing.

### `test.R`
A test script containing placeholder test values.

## Info Section
This documentation was created as part of Project:Hack – a hackathon run by Projecting Success for the Project Data Analytics community.
