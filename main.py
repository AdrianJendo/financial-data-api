from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("postgresql://localhost/[YOUR_DATABASE_NAME]")
    print("Hello World")
