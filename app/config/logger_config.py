import logging
import socket
from logging.handlers import RotatingFileHandler

from logstash_async.handler import AsynchronousLogstashHandler
from app.config.app_config import log_property, app_property


class LoggerFactory:

    @staticmethod
    def check_logstash_connection(host: str, port: int, timeout: int = 5) -> bool:
        """Verify connection to Logstash server."""
        try:
            with socket.create_connection((host, port), timeout):
                return True
        except OSError as e:
            print(f"Logstash connection failed: {e}")
            return False

    @staticmethod
    def get_logger(name: str = "uvicorn") -> logging.Logger:
        """
        Configures and returns a logger instance with a Logstash asynchronous handler.

        :param name: The name of the logger. Defaults to "uvicorn".
        :return: Configured logger instance.
        """
        # Create or retrieve the logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # Define the log format
        log_formatter = logging.Formatter(
            fmt=(
                f"%(asctime)s %(levelname)-5s %(process)d --- [{app_property.name}] [%(threadName)20s] %(module)s.%(funcName)s : %(message)s"
            )
        )

        # Validate Logstash configuration
        if not log_property.logstash_host or not log_property.logstash_port:
            print("Logstash host or port not configured. Async handler will not be added.")
            return logger

        # Verify and configure the asynchronous Logstash or fallback handler
        if LoggerFactory.check_logstash_connection(log_property.logstash_host, log_property.logstash_port):
            async_handler = AsynchronousLogstashHandler(
                host=log_property.logstash_host,
                port=log_property.logstash_port,
                database_path=None
            )
            async_handler.setFormatter(log_formatter)
            logger.addHandler(async_handler)
        else:
            fallback_handler = RotatingFileHandler("app_logs.log", maxBytes=5_000_000, backupCount=5)
            fallback_handler.setFormatter(log_formatter)
            logger.addHandler(fallback_handler)
            print("Failed to configure Logstash handler. Fallback handler added")

        return logger


log = LoggerFactory.get_logger()
log.info("Logger initialized successfully")
