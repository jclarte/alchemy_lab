import os
from dotenv import load_dotenv

load_dotenv(".env")

name = os.getenv('NAME')
port = os.getenv('PORT')
assert name, "A NAME environment variable is required."
assert port, "A PORT environment variable is required."

pg_url = f"postgresql://{name}:{name}@localhost:{port}/{name}"
