# Product Requirements Document

## Utibu Health Mobile App

### 1. Introduction
Utibu Health is a health facility that caters to patients with chronic conditions such as HIV, diabetes, and hypertension. The goal of the Utibu Health Mobile App is to provide a convenient way for registered customers to make medication orders and check their statements remotely.

### 2. Objectives
- Allow registered customers to make medication orders remotely.
- Enable customers to check their statements through the mobile app.
- Integrate with the legacy database system to ensure that online orders are saved and reflected in the database.

### 3. Features
#### 3.1 Medication Ordering
- Customers can browse and select medications from a list of available items.
- The app should indicate the availability of each medication based on the current stock in the pharmacy's database.
- Customers can add medications to their cart and place an order.

#### 3.2 Statement Checking
- Customers can view their current statement, including previous orders and payments.
- The statement should be updated in real-time to reflect any new orders or payments.

#### 3.3 Integration with Legacy System
- Implement RESTful APIs to communicate with the legacy database system.
- Ensure that online orders are saved and reflected in the legacy database.
- Maintain compatibility with the existing technology stack, including Microsoft SQL Server and the legacy desktop application developed in Delphi.

### 4. Technology Stack
- Frontend: React Native
- Backend: Python Flask
- Database: Microsoft SQL Server
- Integration: RESTful APIs

### 5. Security
- Implement secure communication protocols (e.g., HTTPS) to protect data in transit.
- Use OAuth for user authentication to enhance security.

### 6. Offline Support
- Implement offline capabilities in the mobile app to allow users to place orders and check statements even without internet connectivity.
- Use local storage to store data temporarily and sync with the server when online.

### 7. User Experience
- Design the app's UI/UX using Figma to ensure a modern and intuitive interface.

### 8. Timeline
- Day 1: Requirement Gathering and Planning
- Day 2-3: Development
- Day 4: Testing and Deployment

### 9. Constraints
- Reliable internet at the health facility, but no public IP address.
- Use any approach, technology, or tools as long as orders are eventually saved in the legacy database.
