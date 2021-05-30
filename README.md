# MySQL

## Documentation

- [Tutorial](https://www.w3schools.com/mysql/default.asp)
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
- [Docker for Desktop](https://www.docker.com/products/docker-desktop)
- [MySQL sample](https://www.mysqltutorial.org/mysql-sample-database.aspx)

### Create local MySQL instance using Docker

```bash
docker run --name database-mysql -e MYSQL_ROOT_PASSWORD=secret -d -p 3306:3306 mysql:8.0
```

### TODO

- [x] What are DB and why we need them
- [x] MySQL Data Types
- [x] CREATE/DROP DATABASE
- [x] CREATE/DROP TABLE
- [x] SELECT
- [x] WHERE
- [x] AND, OR, NOT
- [x] ORDER BY
- [x] INSERT INTO
- [x] NULL values
- [x] UPDATE
- [x] DELETE
- [x] LIMIT
