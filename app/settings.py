from snowflake.snowpark import Session
import toml


with open("config.toml") as f:
    config = toml.load(f)


session = Session.builder.configs(config["connections"]["snowflake"]).create()