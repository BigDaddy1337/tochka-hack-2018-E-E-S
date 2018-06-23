package types

import()

type Groups struct{
	Id int64
	Name string
	PersonsType *PersonsType
	Status string
}

type PersonsType struct{
	Id int64
	Type string
	Section string
}

type Persons struct {
	Id int64
	TelegramId int64
	FirstName string
	LastName string
	PersonsType *PersonsType
	Status string
	CurrentGroup *Groups
}
