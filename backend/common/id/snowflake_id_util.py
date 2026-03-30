from snowflake import SnowflakeGenerator

flake = SnowflakeGenerator(instance=1)

def getId() -> int :
    return next(flake)