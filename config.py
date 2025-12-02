def add_setting(settings_dict, key_value_tuple):
    key, value = key_value_tuple
    key = key.lower()
    value = value.lower()

    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings_dict, key_value_tuple):
    key, value = key_value_tuple
    key = key.lower()
    value = value.lower()

    if key not in settings_dict:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
    settings_dict[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings_dict, key):
    key = key.lower()
    if key not in settings_dict:
        return f"Setting not found!"
    
    del settings_dict[key]
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings):
    if not settings:
        return "No settings available."
    
    lines = ["Current User Settings:"]
    for key, value in settings.items():
        
        lines.append(f"{key.capitalize()}: {value.lower()}")
    
    return "\n".join(lines) + "\n"


test_settings = {'theme': 'dark','notifications':'enabled',
'volume':'high'}

test_settings = {'theme': 'dark','notifications':'enabled',
'volume':'high'}

print(view_settings(test_settings))