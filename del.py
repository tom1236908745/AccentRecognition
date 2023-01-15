import constants
import shutil
from pathlib import Path

if __name__ == '__main__':
    feature_file = Path('features/')
    model_file = Path('models/')
    testing_data = Path('testing_data/')
    if Path.exists(feature_file):
        shutil.rmtree(feature_file)
    if Path.exists(model_file):
        shutil.rmtree(model_file)
    if Path.exists(testing_data):
        shutil.rmtree(testing_data)
