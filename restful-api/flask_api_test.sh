#!/bin/bash

# Test 1: Check if API is running
echo "Test 1: Check API status"
curl -X GET http://127.0.0.1:5000/
echo -e "\n"

# Test 2: Check API status endpoint
echo "Test 2: Check API status endpoint"
curl -X GET http://127.0.0.1:5000/status
echo -e "\n"

# Test 3: Get all usernames (should be empty at first)
echo "Test 3: Get all usernames"
curl -X GET http://127.0.0.1:5000/data
echo -e "\n"

# Test 4: Add a new user
echo "Test 4: Add a new user"
curl -X POST http://127.0.0.1:5000/add_user \
    -H "Content-Type: application/json" \
    -d '{"username": "john_doe", "name": "John Doe", "age": 30, "city": "New York"}'
echo -e "\n"

# Test 5: Get all usernames after adding a user
echo "Test 5: Get all usernames after adding a user"
curl -X GET http://127.0.0.1:5000/data
echo -e "\n"

# Test 6: Get a specific user
echo "Test 6: Get user john_doe"
curl -X GET http://127.0.0.1:5000/users/john_doe
echo -e "\n"

# Test 7: Try getting a non-existing user
echo "Test 7: Get non-existing user"
curl -X GET http://127.0.0.1:5000/users/unknown_user
echo -e "\n"

# Test 8: Try adding a user without a username
echo "Test 8: Add user without username"
curl -X POST http://127.0.0.1:5000/add_user \
    -H "Content-Type: application/json" \
    -d '{"name": "Jane Doe", "age": 25, "city": "Los Angeles"}'
echo -e "\n"

# Test 9: Try adding a duplicate user
echo "Test 9: Add duplicate user"
curl -X POST http://127.0.0.1:5000/add_user \
    -H "Content-Type: application/json" \
    -d '{"username": "john_doe", "name": "John Doe", "age": 30, "city": "New York"}'
echo -e "\n"

# Test 10: Add another user
echo "Test 10: Add another user"
curl -X POST http://127.0.0.1:5000/add_user \
    -H "Content-Type: application/json" \
    -d '{"username": "jane_doe", "name": "Jane Doe", "age": 25, "city": "Los Angeles"}'
echo -e "\n"

# Test 11: Get all usernames after adding multiple users
echo "Test 11: Get all usernames after adding multiple users"
curl -X GET http://127.0.0.1:5000/data
echo -e "\n"

# Test 12: Get the second user
echo "Test 12: Get user jane_doe"
curl -X GET http://127.0.0.1:5000/users/jane_doe
echo -e "\n"

# Test 13: Add a user without Content-Type header
echo "Test 13: Add user without Content-Type header"
curl -X POST http://127.0.0.1:5000/add_user \
    -d '{"username": "test_user", "name": "Test User", "age": 20, "city": "Miami"}'
echo -e "\n"
