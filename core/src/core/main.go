package main

import (
	"postgres"
	"redis"
	//"types"
	"github.com/sirupsen/logrus"
	"config"
	"fmt"
)

func BackgroundConnector(
	pgAddr string,
	pgUser string,
	pgPass string,
	pgDatabase string,
	redisAddr string,
	redisPass string) (postgres.PgSess, redis.RedisSess, error){
	logrus.Info("[CONNECTOR] Start postgres connection.")

	postgresCli := postgres.PostgresCli(&postgres.PgSess{})
	pgSess, err := postgresCli.Connect(pgAddr, pgUser, pgPass, pgDatabase)

	redisCli := redis.RedisCli(&redis.RedisSess{})
	redisSess, err := redisCli.Connect(redisAddr, redisPass)

	return pgSess, redisSess, err
}

func Pipeline(){}

func main() {
	psSess, redisSess, err := BackgroundConnector(
		config.PostgresAddr, config.PostgresUser, config.PostgresPassword, config.PostgresDatabase, config.RedisAddr, config.RedisPass)

	if err != nil {
		panic(err)
	}

	fmt.Println(&psSess, &redisSess)

	logrus.Info("[CONNECTOR] Connection to postgres and redis - ok.")

	Pipeline()

}
