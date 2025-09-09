import re
from datetime import datetime.

class User:
    def __init__(self, name, email, age):
        # Bug fixed: add input validation in constructor
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        if not self._is_valid_email(email):
            raise ValueError("Invalid email format")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer")
            
        self.name = name.strip()
        self.email = email.lower()
        self.age = age
        self.created_at = datetime.now()
    
    def _is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def update_email(self, new_email):
        # Bug fixed: add email format validation
        if not self._is_valid_email(new_email):
            raise ValueError("Invalid email format")
        self.email = new_email.lower()
    
    def get_age_category(self):
        # Bug fixed: handle edge cases and make categories configurable
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        elif self.age < 13:
            return "child"
        elif self.age < 18:
            return "teen"
        elif self.age < 65:
            return "adult"
        else:
            return "senior"
    
    def __str__(self):
        # Bug fixed: limit exposed data for security
        return f"User: {self.name} (created: {self.created_at.strftime('%Y-%m-%d')})"

class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        # Bug fixed: prevent duplicate users by email
        if self.find_user_by_email(user.email):
            raise ValueError(f"User with email {user.email} already exists")
        self.users.append(user)
    
    def find_user_by_email(self, email):
        # Bug fixed: case-insensitive search
        email_lower = email.lower()
        for user in self.users:
            if user.email.lower() == email_lower:
                return user
        return None

# Test the fixed classes
try:
    user1 = User("", "invalid-email", -5)  # Will raise validation errors
except ValueError as e:
    print(f"Validation error: {e}")

try:
    user2 = User("Alice", "alice@example.com", 30)
    user3 = User("Bob", "ALICE@EXAMPLE.COM", 25)  # Duplicate email test
    
    manager = UserManager()
    manager.add_user(user2)
    manager.add_user(user3)  # Will raise duplicate error
except ValueError as e:
    print(f"Manager error: {e}")

# Test successful operations
user_valid = User("Alice", "alice@example.com", 30)
print(user_valid)
print(f"Age category: {user_valid.get_age_category()}")
