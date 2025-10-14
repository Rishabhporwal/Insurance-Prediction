# Insurance Prediction

## Overview
This project aims to predict insurance charges based on various factors such as age, BMI, smoking status, and other demographic information. It utilizes machine learning techniques to build a predictive model, providing insights for insurance companies or individuals to estimate insurance costs.

## Table of Contents
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Features
- Predicts insurance charges using machine learning models.
- Supports data preprocessing, feature engineering, and model evaluation.
- Includes visualizations for data analysis and model performance.
- Built with Python and popular libraries like Pandas, Scikit-learn, and Matplotlib.

## Dataset
The dataset used in this project is the [Insurance Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance) from Kaggle. It contains the following features:
- **age**: Age of the primary beneficiary.
- **sex**: Gender of the beneficiary (male/female).
- **bmi**: Body Mass Index.
- **children**: Number of children covered by the insurance.
- **smoker**: Smoking status (yes/no).
- **region**: Residential area in the US (northeast, southeast, southwest, northwest).
- **charges**: Individual medical costs billed by health insurance.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rishabhporwal/Insurance-Prediction.git
   cd Insurance-Prediction
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes dependencies like:
   - pandas
   - numpy
   - scikit-learn
   - matplotlib
   - seaborn

4. **Download the dataset**:
   - Download the dataset from [Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance).
   - Place the `insurance.csv` file in the `data/` directory.

## Usage
1. **Preprocess the data**:
   Run the data preprocessing script to clean and prepare the dataset:
   ```bash
   python scripts/preprocess.py
   ```

2. **Train the model**:
   Train the machine learning model using:
   ```bash
   python scripts/train_model.py
   ```

3. **Make predictions**:
   Use the trained model to make predictions:
   ```bash
   python scripts/predict.py
   ```

4. **Visualize results**:
   Generate visualizations for data analysis and model performance:
   ```bash
   python scripts/visualize.py
   ```

## Model Details
- **Algorithm**: The project uses regression models such as Linear Regression, Random Forest, or Gradient Boosting (specified in `train_model.py`).
- **Evaluation Metrics**: Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² Score.
- **Feature Engineering**: Categorical variables (e.g., sex, smoker, region) are encoded using one-hot encoding or label encoding.
- **Preprocessing**: Handles missing values, scales numerical features, and removes outliers if necessary.

## Results
- The model achieves an R² score of approximately [insert typical R² score, e.g., 0.85] on the test set.
- Visualizations of feature importance and prediction errors are available in the `plots/` directory.
- Detailed performance metrics are logged in `logs/evaluation.txt`.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

Please ensure your code follows the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
