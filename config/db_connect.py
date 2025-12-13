import os 
from dotenv import load_dotenv 
from sqlalchemy import create_engine 

load_dotenv() 

def get_engine(): 
    """  
    - Centralized database access 
    - Configuration driven by .env 
    """
    user = os.getenv("DB_USER") 
    password = os.getenv("DB_PASSWORD") 
    host = os.getenv("DB_HOST") 
    port = os.getenv("DB_PORT") 
    db = os.getenv("DB_NAME") 

    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(url)

    return engine
 