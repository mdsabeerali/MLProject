# It keeps a record of what your program is doing.
# Instead of just using print(), we use a logger to write messages in a file.
# Helps you know what happened if something goes wrong.
"""
Benefits:
✅ Helps you see what happened step by step.
✅ Easier to debug when your code crashes.
✅ You can track model runs even after the program stops.
✅ Makes your project look professional and well-maintained.
"""
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH, 
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,

)
