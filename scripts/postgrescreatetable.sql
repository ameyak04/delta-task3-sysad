\c postgres;
CREATE TABLE student(name VARCHAR(255),password VARCHAR(255), hostel VARCHAR(255),room INT,mess INT,messpref INT);
COPY student from '/tmp/cleansd.txt' with delimiter ':';
