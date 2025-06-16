from pydantic_settings import BaseSettings, SettingsConfigDict


class AppProperty(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    name: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        env_file_encoding="utf-8",
        extra="ignore"
    )


app_property = AppProperty()


class DatabaseProperty(BaseSettings):
    """
    Database configuration settings loaded from environment variables.
    """
    host: str | None = None
    port: int | None = None
    name: str | None = None
    user: str | None = None
    password: str | None = None
    schema_name: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="DB_",
        env_file_encoding="utf-8",
        extra="ignore"
    )


db_property = DatabaseProperty()


class LoggerSettings(BaseSettings):
    """
    Logger configuration loaded from environment variables.
    Includes logstash host/port and log level.
    """
    logstash_host: str | None = None
    logstash_port: int | None = None
    log_level: str = 'INFO'

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="LOGGER_",
        env_file_encoding="utf-8",
        extra="ignore"
    )


log_property = LoggerSettings()
