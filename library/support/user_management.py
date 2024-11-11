import json

class User:
    def __init__(self, data=None):
        self.id = "0"
        self.tags = {"signed_up": False, "onboarded": False}
        self.rmo_applications = {}
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        self.date_of_birth = {"month": "", "day": "", "year": ""}
        self.gender = ""
        self.postal_code = ""

        if data:
            self.__dict__.update(data)

    def to_json(self):
        return self.__dict__
    
    def set_user(self, data):
        self.id = data["id"]
        self.tags = data["tags"]
        self.rmo_applications = data["rmo_applications"]
        self.email = data["email"]
        self.password = data["password"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.date_of_birth = data["date_of_birth"]
        self.gender = data["gender"]
        self.postal_code = data["postal_code"]
        self.__dict__.update(data)

    def __getattr__(self, attr):
        try:
            return self.__dict__[attr]
        except KeyError:
            raise AttributeError(f"'User' object has no attribute '{attr}'")

    def __setattr__(self, attr, value):
        if attr in self.__dict__:
            self.__dict__[attr] = value
        else:
            raise AttributeError(f"'User' object has no attribute '{attr}'")


def load_users(users_file='users.json'):
    """Loads users from a JSON file."""
    try:
        with open(users_file, 'r') as f:
            return [User(user) for user in json.load(f)]
    except FileNotFoundError:
        return []

def save_users(users, users_file='users.json'):
    """Saves users to a JSON file."""
    with open(users_file, 'w') as f:
        json.dump([user.to_json() for user in users], f, indent=2)


def search_json(users_file, criteria):
    """Searches for users based on provided criteria, navigating nested JSON structures.

    Args:
        users_file (str): Path to the JSON file containing users.
        criteria (list): List of dictionaries, each representing search criteria.
            Example: 
            [
                {"tags": {"signed_up": True, "onboarded": False}}, 
                {"email": "kev@@gmail.com"}, 
                {"date_of_birth.month": "January"}  # Nested attribute access
            ]

    Returns:
        list: List of User objects matching the criteria.
    """
    users = load_users(users_file)
    matching_users = []
    for user_data in users:  # Iterate over the list of user dictionaries
        user = User(user_data)  # Create a User object from each dictionary
        match = True
        for criterion in criteria:
            # Extract nested attribute path (e.g., "date_of_birth.month")
            nested_path = list(criterion.keys())[0]
            nested_value = list(criterion.values())[0]

            # Split the nested path into individual attributes
            attributes = nested_path.split('.')

            # Navigate through nested attributes
            current_value = user
            for attr in attributes:
                try:
                    current_value = getattr(current_value, attr)
                except AttributeError:
                    match = False
                    break  # Attribute not found, move to the next criterion

            # Compare the final nested value with the search value
            if match and current_value != nested_value:
                match = False

        if match:
            matching_users.append(user)

    return matching_users


def update_json(users_file, user_data):
    """Updates or creates a user in the users.json file.

    Args:
        users_file (str): Path to the JSON file containing users.
        user_data (dict): Dictionary containing user information.
    """
    users = load_users(users_file)
    user_id = user_data.get("id")

    if user_id == "":  # Create a new user if 'id' is empty
        max_id = 0
        for user_dict in users:
            if int(user_dict["id"]) > max_id:
                max_id = int(user_dict["id"])
        user_data['id'] = str(max_id + 1).zfill(3)  # Generate a new ID
        users.append(user_data)  # Add the new user to the list
    else:
        for i, user_dict in enumerate(users):  # Iterate over user dictionaries
            if user_dict["id"] == user_id:
                users[i] = user_data  # Update the user dictionary
                break
        else:  # User not found, add new (shouldn't happen if 'id' is not empty)
            users.append(user_data)

    save_users(users, users_file)