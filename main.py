from src.ship_input import get_player_ships
from src.logger import setup_logger

logger = setup_logger()

def main():
    logger.info("Game started")
    get_player_ships()
    generate_bot_ships()

if __name__ == "__main__":
    main()
