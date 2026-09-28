import dotenv
import kaggle
import shutil
import os

class KaggleExtractor:
    def __init__(self, dataset_url):
        self.dataset_url = dataset_url
        self.api = kaggle.KaggleApi()
        self.api.authenticate()
    
    def download_file(self, file_name, path):
        self.api.dataset_download_file(
            dataset=self.dataset_url,
            file_name=file_name
        )
        try:
            output_path = os.path.join(path, file_name)
            if os.path.exists(output_path):
                os.remove(output_path)

            shutil.move(file_name, path)
        except Exception as e:
            print(f"Error removing existing file: {e}")

def run_extraction():
    dotenv.load_dotenv()

    extractor = KaggleExtractor(
        dataset_url=os.getenv('KAGGLE_DATASET')
    )

    extractor.download_file(
        file_name='car_evaluation.csv',
        path='data'
    )