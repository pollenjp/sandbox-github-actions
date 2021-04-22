from logging import getLogger

logger = getLogger

def main():
    logger.warning("warning")
    logger.info("info")

if __name__ == "__main__":
    main()
