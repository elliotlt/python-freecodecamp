class Category:
    def __init__(self, name):
        # Initialize a budget category with a name and an empty ledger list
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        # Add a deposit to the ledger as a dictionary with amount and description
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        # Withdraw an amount from the ledger if there are sufficient funds
        # The amount is stored as a negative number
        if self.check_funds(amount):  # Calls check_funds to verify balance
            self.ledger.append({"amount": -amount, "description": description})
            return True  # Return True if withdrawal is successful
        return False  # Return False if insufficient funds
    
    def get_balance(self):
        # Calculate and return the current balance by summing all amounts in the ledger
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, category):
        # Transfer funds to another category if sufficient funds are available
        # Calls withdraw to deduct amount and deposit to add it to the target category
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True  # Return True if transfer is successful
        return False  # Return False if insufficient funds
    
    def check_funds(self, amount):
        # Check if there are enough funds in the category
        return amount <= self.get_balance()  # Returns True if enough balance, False otherwise
    
    def __str__(self):
        # Return a formatted string representation of the category
        title = f"{self.name:*^30}\n"  # Title centered with *
        
        # Format ledger items: first 23 chars of description and amount right-aligned
        items = "".join(f"{item['description'][:23]:23}{item['amount']:7.2f}\n" for item in self.ledger)
        
        total = f"Total: {self.get_balance():.2f}"  # Display total balance
        return title + items + total  # Concatenate all parts into a single string

def create_spend_chart(categories):
    # Create a bar chart displaying spending percentages for each category
    title = "Percentage spent by category\n"
    
    # Calculate total withdrawals per category (only negative amounts are considered)
    withdrawals = [sum(-item['amount'] for item in cat.ledger if item['amount'] < 0) for cat in categories]
    total_spent = sum(withdrawals)  # Compute total spending across all categories
    
    # Calculate percentage spent per category rounded down to the nearest 10
    percentages = [int((spent / total_spent) * 100 // 10 * 10) for spent in withdrawals]
    
    # Construct the vertical bar chart with labels at intervals of 10
    chart = ""
    for i in range(100, -1, -10):  # Iterate from 100% down to 0%
        chart += f"{i:3}| " + "  ".join("o" if p >= i else " " for p in percentages) + "  \n"
    
    # Add separator line (two spaces past the final category column)
    separator = "    " + "-" * (3 * len(categories) + 1) + "\n"
    
    # Prepare category names for vertical alignment
    names = [list(cat.name) for cat in categories]  # Convert names to lists of characters
    max_length = max(len(cat.name) for cat in categories)  # Find longest category name
    names = [name + [" "] * (max_length - len(name)) for name in names]  # Pad names for alignment
    
    # Construct vertical labels for category names
    name_lines = ""
    for i in range(max_length):
        name_lines += "     " + "  ".join(name[i] for name in names) + "  \n"
    
    # Combine all parts into the final chart string
    return title + chart.rstrip("\n") + "\n" + separator + name_lines.rstrip("\n")

# Example usage
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food, clothing]))
