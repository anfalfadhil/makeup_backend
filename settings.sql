-- settings.sql
CREATE DATABASE makeup;
CREATE USER makeupuser WITH PASSWORD 'makeup';
GRANT ALL PRIVILEGES ON DATABASE makeup TO makeupuser;