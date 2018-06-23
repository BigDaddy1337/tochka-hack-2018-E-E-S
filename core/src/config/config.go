package config

import "os"

var (
	path = os.Getenv("PATH")
	PostgresAddr = "localhost:5431"//os.Getenv("PG_ADDR")
	PostgresUser = "test" //os.Getenv("PG_USER")
	PostgresPassword = "test"//os.Getenv("PG_PASS")
	PostgresDatabase = "test"//os.Getenv("PG_DB")
	RedisAddr = "localhost:6379"//os.Getenv("REDIS_ADDR")
	RedisPass = ""//os.Getenv("REDIS_PASS")
)
