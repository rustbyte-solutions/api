import tomllib

with open("data/config.toml", "rb") as file:
    config = tomllib.load(file)

DATABASE = config["api"]["database"]
