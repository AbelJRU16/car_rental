CREATE DATABASE IF NOT EXISTS car_rental;
USE car_rental;

CREATE TABLE IF NOT EXISTS brand(
    id INT AUTO_INCREMENT not null,
    name varchar(50) not null unique,
    primary key(id)
);

CREATE TABLE IF NOT EXISTS car_status(
    id INT AUTO_INCREMENT not null,
    name varchar(20) not null unique,
    primary key(id)
);

CREATE TABLE IF NOT EXISTS car_type(
    id INT AUTO_INCREMENT not null,
    description varchar(20) not null,
    long_description varchar(1000) not null,
    rent_cost DECIMAL(10, 2) not null,
    primary key(id)
);

CREATE TABLE IF NOT EXISTS vehicle(
    id INT AUTO_INCREMENT not null,
    plate varchar(10) not null unique,
    id_brand INT not null,
    id_status INT not null,
    id_type INT not null,
    description varchar(20) not null,
    long_description varchar(1000) not null,
    primary key(id),
    FOREIGN key(id_brand) 
        REFERENCES brand(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN key(id_status) 
        REFERENCES car_status(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN key(id_type) 
        REFERENCES car_type(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS payment_method(
    id INT AUTO_INCREMENT not null,
    description varchar(50) not null unique,
    primary key(id)
);

CREATE TABLE IF NOT EXISTS client(
    id INT AUTO_INCREMENT not null,
    name varchar(100) not null,
    email varchar(100) not null unique,
    cellphone VARCHAR(20) NOT NULL,
    primary key(id)
);

CREATE TABLE IF NOT EXISTS employee(
    id INT AUTO_INCREMENT not null,
    name varchar(100) not null,
    email varchar(100) not null unique,
    cellphone VARCHAR(20) NOT NULL,
    user VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    primary key(id)
);

CREATE TABLE IF NOT EXISTS rent(
    id INT AUTO_INCREMENT not null,
    name varchar(100) not null,
    id_employee INT not null,
    id_client INT not null,
    id_vehicle INT not null,
    start_date DATETIME not null,
    end_date DATETIME not null,
    delivery_date DATETIME not null,
    cost DECIMAL(10,2) not null,
    primary key(id),
    FOREIGN key(id_employee) 
        REFERENCES employee(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN key(id_client) 
        REFERENCES client(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN key(id_vehicle) 
        REFERENCES vehicle(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS payment(
    id INT AUTO_INCREMENT not null,
    id_employee INT not null,
    id_rent INT not null,
    id_method INT not null,
    payment_date DATETIME NOT NULL,
    amount decimal(10,2) NOT NULL,
    primary key(id),
    FOREIGN key(id_employee) 
        REFERENCES employee(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN key(id_rent) 
        REFERENCES rent(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN key(id_method) 
        REFERENCES payment_method(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);