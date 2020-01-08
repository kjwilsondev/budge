# Postgres

## Commands

### Database Creation

Downloaded postgres.app
Downloaded PGAdmin

```os
psql
create database budge;
>> CREATE DATABASE
\q
```

### Killing Ports

```os
lsof -i :5432
kill -9 <PID>
```

### Psycopg2 Problems

[Symbol not found: \_PQencryptPasswordConn](https://stackoverflow.com/questions/57236722/what-does-import-error-symbol-not-found-pqencryptpasswordconn-mean-and-how-do)
