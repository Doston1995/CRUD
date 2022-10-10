import sqlalchemy


metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id",         sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("username",   sqlalchemy.String),
    sqlalchemy.Column("password",   sqlalchemy.String),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name",  sqlalchemy.String),
    sqlalchemy.Column("gender",     sqlalchemy.CHAR  ),
    sqlalchemy.Column("create_at",  sqlalchemy.String),
    sqlalchemy.Column("status",     sqlalchemy.CHAR  ),
)