-- Create Database
CREATE DATABASE Utibu_db;

-- Use Database
USE UtibuHealth;

-- Create Tables
CREATE TABLE Medications
(
    MedicationID INT PRIMARY KEY,
    Name NVARCHAR(255) NOT NULL,
    StockLevel INT NOT NULL
);

CREATE TABLE Orders
(
    OrderID INT PRIMARY KEY,
    MedicationID INT NOT NULL,
    CustomerID INT NOT NULL,
    Quantity INT NOT NULL,
    OrderDate DATETIME NOT NULL,
    Status NVARCHAR(50) NOT NULL
);

CREATE TABLE Customers
(
    CustomerID INT PRIMARY KEY,
    Name NVARCHAR(255) NOT NULL,
    Email NVARCHAR(255) NOT NULL,
    Phone NVARCHAR(20) NOT NULL,
    Address NVARCHAR(255) NOT NULL
);

CREATE TABLE Payments
(
    PaymentID INT PRIMARY KEY,
    OrderID INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentDate DATETIME NOT NULL,
    PaymentMethod NVARCHAR(50) NOT NULL
);

-- Add more tables as needed...
