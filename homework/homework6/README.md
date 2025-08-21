# Stage 6: Data Preprocessing

This project cleans and preprocesses a raw dataset to prepare it for analysis or modeling. The cleaning process includes filling missing values, dropping missing rows, and normalizing the data.

## Cleaning Strategy

1.Drop missing values: Removing rows where the ‘age’ column has missing values.
Assumption: Missing values in ‘age’ are not recoverable, and removing these rows does not significantly impact the dataset’s integrity.

2.Fill Missing Values with Median:Filling missing values in the ‘income’ and ‘score’ columns with their respective median values.
Assumption: Missing values in ‘income’ and ‘score’ are randomly distributed, and the median is a robust measure to handle potential outliers.

3.Min–Max Normalization: Scale numeric features to [0,1] for downstream models that are sensitive to feature scales.
Assumption: Normalizing these features ensures they are on a comparable scale, which is beneficial for downstream analysis or machine learning models.
