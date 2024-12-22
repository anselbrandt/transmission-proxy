import os
from dotenv import load_dotenv

load_dotenv()

TRANSMISSION_USERNAME = os.getenv("TRANSMISSION_USERNAME")
TRANSMISSION_PASSWORD = os.getenv("TRANSMISSION_PASSWORD")

SSH_USERNAME = os.getenv("SSH_USERNAME")
SSH_PASSWORD = os.getenv("SSH_PASSWORD")

REMOTE_HOST = os.getenv("REMOTE_HOST")

REMOTE_ROOT_PATH = os.getenv("REMOTE_ROOT_PATH")
LOCAL_ROOT_PATH = os.getenv("LOCAL_ROOT_PATH")

ROOT_PATH = os.getenv("ROOT_PATH")
