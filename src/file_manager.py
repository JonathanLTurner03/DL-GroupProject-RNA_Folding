import kaggle
import zipfile
import os
import shutil

class FileManager:

    def __init__(self):
        # Setting the root directories
        project_root = os.getcwd()
        kaggle_root = os.path.join(project_root, ".kaggle")
        self.kaggle_zip_dir = os.path.join(project_root, ".kaggle", "zip")
        self.kaggle_zip = os.path.join(self.kaggle_zip_dir, "stanford-rna-3d-folding.zip")
        self.kaggle_files = os.path.join(project_root, ".kaggle", "files")

        # Setup the Kaggle API
        self.kaggle_api = kaggle.KaggleApi()
        self.activated = True
        try:
            self.kaggle_api.authenticate()
        except:
            print(f'Please follow the link https://www.kaggle.com/docs/api to setup kaggle settings.json')
            self.activated = False

        if not os.path.exists(kaggle_root):
            os.mkdir(kaggle_root)

    def load_data(self):
        if os.path.exists(self.kaggle_files) and os.listdir(self.kaggle_files):
           print(f'Files located in: {self.kaggle_files}')
           return

        if os.path.exists(self.kaggle_zip_dir) and os.path.exists(self.kaggle_zip):
            print(f'Extracting files to dir: {self.kaggle_files}')
            self.extract_files()
            print(f'Deleting unneeded archive file.')
            self.clean_files()
            return

        print(f'Downloading files from Kaggle to {self.kaggle_zip_dir}')
        self.download_dataset()
        print(f'Extracting files to {self.kaggle_files}')
        self.extract_files()
        print(f'Deleting unneeded archive file.')
        self.clean_files()

    def clean_files(self):
        if os.path.exists(self.kaggle_zip_dir):
            shutil.rmtree(self.kaggle_zip_dir)
    def download_dataset(self):
        # Downloads the dataset
        if not os.path.exists(self.kaggle_zip_dir):
            os.mkdir(self.kaggle_zip_dir)

        self.kaggle_api.competition_download_files(competition="stanford-rna-3d-folding", path=self.kaggle_zip_dir)

    def extract_files(self):
        # Opens the zip download and extracts it if needed.
        with zipfile.ZipFile(self.kaggle_zip, 'r') as zip_ref:
            if not os.path.exists(self.kaggle_files):
                os.mkdir(self.kaggle_files)

            zip_ref.extractall(self.kaggle_files)