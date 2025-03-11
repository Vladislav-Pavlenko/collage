#
# from pymongo.server_api import ServerApi
# from pymongo import MongoClient
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# db_user = os.getenv('MONGODB_USER')
# db_password = os.getenv('MONGODB_PASSWORD')
# db_url = os.getenv('MONGODB_URL')
# db_name = os.getenv('MONGODB_DB')
# uri = f"mongodb+srv://{db_user}:{db_password}@{db_url}/{db_name}?retryWrites=true&w=majority&appName=My-contacts"
#
# client = MongoClient(uri, server_api=ServerApi('1'))
# db = client['my-contacts']
# contacts_collection = db['contacts']
# contacts = list(contacts_collection.find())
# print(1)
# print(contacts)
