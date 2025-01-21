import os

if __name__ == "__main__":
    print(f"PYTHON_RUN_ENV is {os.getenv('PYTHON_RUN_ENV', '<Empty>')}")