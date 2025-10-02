import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment
env = environ.Env(
    DEBUG=(bool, False)  # casting
)

# Load .env
environ.Env.read_env(BASE_DIR / ".env")

# Read variables
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG",default=False)

DATABASES = {
      "default": env.db("DATABASE_URL")
}



    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': env("DB_NAME"),
    #     'USER': env("DB_USER"),
    #     'PASSWORD': env("DB_PASSWORD"),
    #     'HOST': env("DB_HOST", default="localhost"),
    #     'PORT': env("DB_PORT", default="5433"),
    # }