# импортируйте необходимую библиотеку
# ваш код здесь
from catboost import CatBoostClassifier
def load_churn_model(model_path: str):
    """Загружаем обученную модель оттока.
    Args:
        model_path (str): Путь до модели.
    """
    try:
        # ваш код здесь — загрузите модель
        model = CatBoostClassifier()
        model.load_model(model_path)
        
        print("Model loaded successfully")
    except Exception as e:
        print(f"Failed to load model: {e}")
    return model

if __name__ == "__main__":
    # вызовите функцию load_churn_model с нужным путём
    # ваш код здесь  
    # выведите параметры модели через print(f"Model parameter names: {}") 
    # ваш код здесь 
    model_path = "models/catboost_churn_model.bin"
    model = load_churn_model(model_path=model_path)
    print(f"Model parameter names: {model.get_params()}") 

