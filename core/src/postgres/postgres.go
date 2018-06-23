package postgres

import(
	"github.com/go-pg/pg"
	//"github.com/go-pg/pg/orm"
	"../types"
)

type PostgresCli interface {
	Connect(pgAddr string, pgUser string, pgPass string, pgDatabase string) (PgSess, error)
	PersonsWriter(status string, group *types.Groups) error
	GroupWriter(status string) error
}

type PgSess struct{
	DbHandler *pg.DB
}

func (sess *PgSess) Connect(pgAddr string, pgUser string, pgPass string, pgDatabase string) (PgSess, error) {
	sess.DbHandler = pg.Connect(&pg.Options{
		Addr: pgAddr,
		User: pgUser,
		Password: pgPass,
		Database: pgDatabase,
	})

	defer sess.DbHandler.Close()
	return *sess, nil
}

func (sess *PgSess) PersonsWriter(status string, group *types.Groups) error {
	err := sess.DbHandler.Insert(&types.Persons{
		Status: status,
		CurrentGroup: group,
	})

	return err
}

func (sess *PgSess) GroupWriter(status string) error {
	err := sess.DbHandler.Insert(&types.Groups{
		Status: status,
	})

	return err
}
