from app.main import app
from modules.training.main import training

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = training()
    app.run()