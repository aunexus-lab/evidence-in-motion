from src.ingest import load_data
from src.transform import clean_data
from src.validate import validate_data

def run():
    print("Running pipeline...")
    # data = load_data()
    # cleaned = clean_data(data)
    # validate_data(cleaned)
    print("Pipeline finished.")

if __name__ == "__main__":
    run()
