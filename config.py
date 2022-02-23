from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
db = os.getenv('MYSQL_DB')

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{db}'
# print(DATABASE_CONNECTION_URI)
# print(os.environ['HELLO'])