from dotenv import load_dotenv
import os

load_dotenv()
HOST, USER, PASSWORD, PORT, DB = (os.getenv("HOST"), os.getenv("USER"),
                                  os.getenv("PASSWORD"), os.getenv("PORT"), os.getenv("DB"))
print(HOST, USER, PASSWORD, PORT, DB)
print(type(HOST), type(USER), type(PASSWORD), type(PORT), type(DB))