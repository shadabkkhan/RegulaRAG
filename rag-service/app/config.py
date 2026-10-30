from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    service_name: str  = "regula-rag"
    app_version: str = "0.1.0"

    model_config = SettingsConfigDict(
        env_prefix="REGULARAG_",
        env_file=".env",
        extra="ignore",
    )

settings = Settings()