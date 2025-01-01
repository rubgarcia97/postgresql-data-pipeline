#!/bin/bash

sudo apt update
sudo apt upgrade -y

#install postgresql with some additional tools 

sudo apt install -y postgresql postgresql-contrib

#create new user and database/table on public schema
sudo -u postgres psql -c "CREATE USER ruben WITH PASSWORD 'password33' CREATEDB CREATEROLE LOGIN SUPERUSER;"
sudo -u postgres psql -c "CREATE DATABASE ruben;"
sudo -u ruben psql -c "CREATE DATABASE cryptodb;"
sudo -u ruben psql -d cryptodb -c "CREATE TABLE cryptoklines (
    id VARCHAR(50) PRIMARY KEY,
    symbol VARCHAR(25) NOT NULL,
    openTime TIMESTAMP NOT NULL,
    openPrice FLOAT NOT NULL,
    highPrice FLOAT NOT NULL,
    lowPrice FLOAT NOT NULL,
    closePrice FLOAT NOT NULL,
    volume FLOAT NOT NULL,
    closeTime TIMESTAMP NOT NULL,
    assetVolume FLOAT NOT NULL,
    trades FLOAT NOT NULL,
    BaseAssetVolume FLOAT NOT NULL,
    QuoteAssetVolume FLOAT NOT NULL
);"
