# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os
COMET_API_KEY = os.getenv('COMET_API_KEY')
COMET_WORKSPACE = os.getenv('COMET_WORKSPACE')
COMET_PROJECT_NAME = os.getenv('COMET_PROJECT_NAME')