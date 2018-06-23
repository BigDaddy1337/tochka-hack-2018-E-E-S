package redis

import(
	"github.com/go-redis/redis"
)

type RedisCli interface {
	Connect(pgAddr string) (RedisSess, error)
}

type RedisSess struct{
	Client *redis.Client
}

func (sess *RedisSess) Connect(redisAddr string, redisPass string) (RedisSess, error) {
	sess.Client = redis.NewClient(&redis.Options{
		Addr:     redisAddr,
		Password: redisPass, // no password set
		DB:       0,  // use default DB
	})

	_, err := sess.Client.Ping().Result()
	return *sess, err
}
