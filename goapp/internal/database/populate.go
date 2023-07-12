package database

import (
	"github.com.br/devfullcycle/fc-ms-wallet/internal/entity"
	"github.com/ddosify/go-faker/faker"
)

type Populator struct {
	account_db AccountDB
	client_db  ClientDB
}

func NewPopulator(accountDb AccountDB, clientDb ClientDB) *Populator {
	return &Populator{
		account_db: accountDb,
		client_db:  clientDb,
	}
}

func newRandomClient(fakeClient faker.Faker) (*entity.Client, error) {
	return entity.NewClient(fakeClient.RandomPersonFirstName(), fakeClient.RandomEmail())
}

func (p *Populator) CreateDB() {
	db := p.account_db.DB
	db.Exec("Create table clients (id varchar(255), name varchar(255), email varchar(255), created_at date)")
	db.Exec("Create table accounts (id varchar(255), client_id varchar(255), balance int, created_at date)")
	db.Exec("Create table transactions (id varchar(255), account_id_from varchar(255), account_id_to varchar(255), amount int, created_at date)")
}

func (p *Populator) CleanDb() {
	p.account_db.DB.Exec("DROP TABLE IF EXISTS transactions")
	p.account_db.DB.Exec("DROP TABLE IF EXISTS accounts")
	p.account_db.DB.Exec("DROP TABLE IF EXISTS clients")
}

func (p *Populator) Populate() {
	fakeClient := faker.NewFaker()
	// loop 10 times
	var client *entity.Client
	var account *entity.Account
	var err error
	for i := 0; i < 10; i++ {
		client, err = newRandomClient(fakeClient)
		if err != nil {
			panic(err)
		}
		p.client_db.Save(client)

		account = entity.NewAccount(client)
		account.Credit(fakeClient.RandomFloatBetween(2, 50, 10000))
		p.account_db.Save(account)
	}
}
