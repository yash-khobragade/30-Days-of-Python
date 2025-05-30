# 📅 Day 3 – Lists, Tuples, Dictionaries, and Sets

## 🗒️ Topics Covered
- Lists: Slicing, Common Methods
- Tuples: Immutability
- Dictionaries: Key-Value Pairs
- Sets: Unique Unordered Elements

## 🎯 Challenge

🔧 Create a Python program that uses a **dictionary** to simulate a basic inventory system.

### 💻 Solution

```python
# Simple inventory system using a dictionary

# Create Inventory using Dictionary
inventory = {"Keyboards":12, "Mouse" : 40, "Monitor" : 6, "Laptop" : 10, "Printer" : 3}

# Add new item
inventory["Headphones"] = 15

# Update quantity
inventory["Mouse"] -= 5

# Remove item
del inventory["Printer"]

# Printing the Inventory
for key in inventory:
    print(key, "-", inventory[key])


```
📌 Progress

Day 3 completed ✅

#30DaysOfPython #IDC30DaysChallenge
