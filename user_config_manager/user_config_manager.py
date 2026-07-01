settings = {
    'theme': 'dark',
    'notifications': 'enabled'
}

def add_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"""Setting '{key}' already exists! 
Cannot add a new setting with this name."""
    

test = add_setting(settings, ('Theme', 'Light'))
print(test)