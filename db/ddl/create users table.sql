create table
users
(
id bigserial,
password varchar(128),
name varchar(64),
email varchar(256),
hint varchar(64),
pass_default boolean,
administrator boolean
);