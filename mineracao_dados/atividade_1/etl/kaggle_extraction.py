import dotenv
dotenv.load_dotenv()

import kaggle
import shutil
import os

class KaggleExtractor:
    def __init__(self, dataset_url):
        self.dataset_url = dataset_url
        self.api = kaggle.KaggleApi()
        self.api.authenticate()
    
    def download_file(self, file_name, path, force=False):
        output_path = os.path.join(path, file_name)
        if os.path.exists(output_path) and not force:
            print(f"{output_path} already exists, skipping download.")
            return

        self.api.dataset_download_file(
            dataset=self.dataset_url,
            file_name=file_name
        )
        try:
            if os.path.exists(output_path):
                os.remove(output_path)

            shutil.move(file_name, path)
        except Exception as e:
            print(f"Error removing existing file: {e}")

def run_extraction(force=False):
    extractor = KaggleExtractor(
        dataset_url=os.getenv('KAGGLE_DATASET')
    )

    extractor.download_file(
        file_name='car_evaluation.csv',
        path='data',
        force=force
    )