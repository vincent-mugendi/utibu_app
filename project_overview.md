# Project Requirements

## Utibu Health Overview
- Utibu health caters to patients with chronic conditions such as HIV, diabetes, and hypertension.
- Stable patients can receive medication to last several months without needing a doctor's visit.
- Patients can refill prescriptions at the pharmacy without seeing a doctor.

## Pharmacist Inventory System
- The pharmacist uses an inventory system that manages medication stock, customer orders, sales, invoices, and payments.
- The system runs on Microsoft SQL Server and a legacy desktop application developed in Delphi.

## Client Requirements
- Clients wants registered customers to be able to make medication orders remotely via a mobile app.
- Orders should be confirmed based on current stock levels in the pharmacy's database.
- After confirmation, customers can pick up medication at the health facility or have it delivered.
- Payment can be made immediately or upon collection/receipt of medication.

## Required Solution
- Devise a solution comprising a mobile app that allows registered customers to:
  - Make orders for medication.
  - Check their statement.
  - Option to pay for the medication

## Database Integration
- Maintain the legacy database and system for face-to-face sales.
- Online orders should appear in the legacy database as well.

## Technical Constraints
- Reliable internet at the health facility, but no public IP address.
- Use any approach, technology, or tools as long as orders are eventually saved in the legacy database.
