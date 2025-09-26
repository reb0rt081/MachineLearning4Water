import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor

class ModelHabitatges:
    def __init__(self, 
                 data_path="Informacio_Habitatges_Data.csv", 
                 model_path="XgbRegressorModel.pkl",
                 load_existing=False):
        """
        Initialize the ModelHabitatges.

        Args:
            data_path (str): Path to the dataset CSV.
            model_path (str): Path to save/load the model.
            load_existing (bool): If True, loads an existing model from model_path.
        """
        self.data_path = data_path
        self.model_path = model_path
        self.categorical_cols = [
            'Tipus_habitatge',
            'Rentavaixelles',
            'Us_banyera',
            'Tipus_descarrega'
        ]
        self.numerical_cols = [
            'Persones_habitatge',
            'Lavabos_habitatge',
            'Wc_diari',
            'Dutxes_diari',
            'Antiguitat_caldera',
            'Temps_aigua_calenta'
        ]
        self.target = 'Consum_mensual_m3'
        self.pipeline = None

        if load_existing:
            try:
                self.pipeline = joblib.load(self.model_path)
                print(f"Model loaded from {self.model_path}")
            except FileNotFoundError:
                print(f"No existing model found at {self.model_path}. Please train first.")

    def load_data(self):
        """
        Loads the data from the provided dataset CSV.

        """
        df = pd.read_csv(self.data_path)
        df.fillna({self.target: df[self.target].mean()}, inplace=True)
        X = df[self.categorical_cols + self.numerical_cols]
        y = df[self.target]
        return X, y

    def build_pipeline(self, advanced=False):
        """
        Loads the XGB regressor with the provided information.

        Args:
            advanced (bool): Wether we use or not an advanced XGBRegressor model.
        """
        preprocessor = ColumnTransformer(
            transformers=[('cat', OneHotEncoder(handle_unknown='ignore'), self.categorical_cols)],
            remainder='passthrough'
        )

        if advanced:
            model = XGBRegressor(
                n_estimators=500,
                learning_rate=0.05,
                max_depth=6,
                subsample=0.8,
                colsample_bytree=0.8,
                gamma=0,
                reg_alpha=0.1,
                reg_lambda=1,
                min_child_weight=3,
                objective='reg:squarederror',
                tree_method='hist',
                random_state=42
            )
        else:
            model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)

        self.pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('model', model)
        ])

    def evaluate(self, y_true, y_pred, title="Actual vs Predicted Values"):
        """
        Evaluates the Mean Squared Error and provides a plot that display Actual and Predicted values provided.

        Args:
            y_true: array of values for the real target.
            y_pred: array of values for the predicted target.
            title: optional title when ploting the result.
        """
        mse = mean_squared_error(y_true, y_pred)
        print(f'Mean Squared Error: {mse:.4f}')

        plt.figure(figsize=(8, 6))
        plt.scatter(y_true, y_pred, alpha=0.6)
        plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
        plt.xlabel("Actual")
        plt.ylabel("Predicted")
        plt.title(title)
        plt.grid(True)
        plt.show()

        return mse

    def train(self, advanced=False):
        """
        Train a new model and save it to disk.
        Args:
            advanced (bool): Use advanced hyperparameters if True.
        """
        X, y = self.load_data()
        self.build_pipeline(advanced=advanced)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.pipeline.fit(X_train, y_train)
        y_pred = self.pipeline.predict(X_test)
        mse = self.evaluate(y_test, y_pred, "Training Evaluation")
        joblib.dump(self.pipeline, self.model_path)
        print(f"Model saved to {self.model_path}")
        return mse

    def test(self):
        """
        Evaluate the model on the full dataset.
        """
        X, y = self.load_data()
        if self.pipeline is None:
            self.pipeline = joblib.load(self.model_path)
        y_pred = self.pipeline.predict(X)
        mse = self.evaluate(y, y_pred, "Testing Evaluation")

        compare_df = pd.DataFrame({'Actual_value': y, 'Predicted_value': y_pred})
        compare_df.to_csv('ActualVsPredictedValues.csv', index=False)
        print(compare_df.describe())
        return mse

    def predict(self,
                Persones_habitatge: float,
                Tipus_habitatge: float,
                Lavabos_habitatge: float,
                Rentavaixelles: float,
                Us_banyera: float,
                Wc_diari: float,
                Dutxes_diari: float,
                Antiguitat_caldera: float,
                Temps_aigua_calenta: float,
                Tipus_descarrega: float):
        """
        Make a prediction for a new household input.
        """
        if self.pipeline is None:
            self.pipeline = joblib.load(self.model_path)

        user_df = pd.DataFrame([{
            'Persones_habitatge': Persones_habitatge,
            'Tipus_habitatge': Tipus_habitatge,
            'Lavabos_habitatge': Lavabos_habitatge,
            'Rentavaixelles': Rentavaixelles,
            'Us_banyera': Us_banyera,
            'Wc_diari': Wc_diari,
            'Dutxes_diari': Dutxes_diari,
            'Antiguitat_caldera': Antiguitat_caldera,
            'Temps_aigua_calenta': Temps_aigua_calenta,
            'Tipus_descarrega': Tipus_descarrega
        }])

        expected_columns = self.categorical_cols + self.numerical_cols
        try:
            user_df = user_df[expected_columns]
        except KeyError as e:
            print(f"Error: Missing required column {e} in inputs.")
            return None

        predicted_value = self.pipeline.predict(user_df)
        print(f"Predicted Consum_mensual_m3: {predicted_value[0]:.4f}")
        return predicted_value
