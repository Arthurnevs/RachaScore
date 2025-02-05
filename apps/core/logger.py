import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Define o nível de log

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)