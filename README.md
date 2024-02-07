# alembic-migration-test-for-pgsql

## Steps

1. Created 2 Database models in `models.py` file.
2. Created a migration script using `SCHEMA_NAME=test alembic revision --autogenerate -m "Initial Migration"` command.
3. Updated the migration script with the models using `SCHEMA_NAME=test alembic upgrade head` command.
4. Updated Salt column in `models.py` file.
5. Created a migration script using `SCHEMA_NAME=test alembic revision --autogenerate -m "Modify salt column in accoun table"` command.



## Environment
alembic              1.12.0
SQLAlchemy           2.0.21
psycopg2             2.9.9
Python 3.11.5
Darwin Shubhendras-MacBook-Pro.local 23.0.0 Darwin Kernel Version 23.0.0: Fri Sep 15 14:43:05 PDT 2023; root:xnu-10002.1.13~1/RELEASE_ARM64_T6020 arm64
macOS Sonoma 14.0
