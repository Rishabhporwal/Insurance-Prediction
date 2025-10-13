import os
import pandas as pd
import joblib
from sklearn.linear_model import Lasso
from src.constant import ARTIFACTS_DIR, BEST_MODEL_PATH, MODELS_DIR
from src.logger.logger import logging

class ModelTrainer:

    def __init__(self):
        
        self.data_path = os.path.join(ARTIFACTS_DIR, 'all_processed.csv')
        self.model_out = BEST_MODEL_PATH
        self.preprocessor_path = os.path.join(ARTIFACTS_DIR, 'preprocessor.pkl')

    def train_and_save_model(self):

        logging.info("Starting model training...")
        df = pd.read_csv(self.data_path)
        logging.info("Processed data loaded successfully.")

        X = df.drop(columns=['charges'])
        y = df['charges']

        model = Lasso(alpha=0.01, max_iter=2000, random_state=1)
        model.fit(X, y)
        logging.info("Model training completed.")

        os.makedirs(MODELS_DIR, exist_ok=True)
        joblib.dump(model, self.model_out)
        logging.info(f"Trained model saved to {self.model_out}.")

        return self.model_out