from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    MAIN_DB_URL: str
    SECRET_KEY: str
    TURS0_AUTH_TOKEN: str
    TURSO_ORG_NAME: str
    GROUP_AUTH_TOKEN: str

    class Config:
        env_file = ".env"


settings = Settings() #type: ignore
