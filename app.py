import os

# environment variable, default to 'local' if not found
env = os.getenv('ENVIRONMENT', 'local')

print(f"Namaste! I am running in the {env} environment!")
