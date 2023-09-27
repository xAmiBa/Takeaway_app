# Takeaway App

This program simulates the user experience of Restaurant ordering system, allowing users to view the menu, add items to their basket, remove items from their basket, and place an order. It also utilizes the Twilio API to send order confirmation messages via text.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [What I Learned](#what-i-learned)

## Introduction

Takeaway App provides a menu with various categories of dishes and allows users to interact with the menu by viewing items, adding them to their basket, and placing orders. The program also supports the removal of items from the basket, generating a receipt for the order, and sending order confirmation messages using the Twilio API.

## Features

- Display the menu with items categorized as mains, sides, desserts, and drinks.
- View the basket, including the quantity and total cost of each item.
- Add items to the basket.
- Remove items from the basket.
- Generate a receipt for the order.
- Send an order confirmation via text message using the Twilio API.

## Usage

To use the program, run the provided Python script. The program will prompt the user to perform various actions, such as viewing the menu, managing their basket, and placing an order.

### Menu Options

1. **Show Menu**: Display the restaurant menu.
2. **Show My Basket**: Display the current items in the basket and the total cost.
3. **Order**: Add an item from the menu to the basket.
4. **Delete From Basket**: Remove an item from the basket.
5. **Checkout**: Confirm the order, generate a receipt, and send an order confirmation via text message using the Twilio API.

## What I Learned

In the development of this program, I have demonstrated the following concepts:

- **Test-Driven Development (TDD)**: The program follows a test-driven development approach, where tests were created first to validate the functionality of various components of the program.

- **Object-Oriented Programming (OOP)**: The code is organized using object-oriented programming principles, where classes (e.g., `Menu`, `Basket`, `Confirmation`) encapsulate the functionality related to their respective responsibilities.

- **Unit Testing with `unittest Mock()`**: Unit tests were implemented using the `unittest.mock.Mock` class to mock certain functionalities and isolate the code being tested from external dependencies.

- **Modularization and Code Reusability**: The program is modularized by splitting functionality into separate Python files (`menu.py`, `basket.py`, `confirmation.py`) to improve code organization and reusability.

- **Exception Handling**: The program handles exceptions to provide meaningful error messages and enhance user experience by gracefully handling errors such as an invalid menu item or an empty basket.

- **Usage of External Libraries (Twilio API)**: The program utilizes the Twilio API to send order confirmation messages via text, enhancing the user experience and providing real-time updates on their orders.

Feel free to explore and expand upon these concepts in your further development and projects. Happy coding!
