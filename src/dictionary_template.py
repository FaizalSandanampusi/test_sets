def validate(data, template):
    """
    Validates a nested dictionary against a template.
    
    Args:
        data: Dictionary to validate
        template: Template dictionary to validate against
        
    Returns:
        tuple: (bool, str) where bool indicates if valid and str contains error message
    """
    def validate_recursive(d, t, path=""):
        # Remove debug prints for production code
        data_keys = set(d.keys())
        template_keys = set(t.keys())
        
        # Check for missing or extra keys
        if data_keys != template_keys:
            # Always check template keys first in original order
            for key in t.keys():
                if key not in data_keys:
                    return False, f"mismatched keys: {path + key if path == '' else path + '.' + key}"
            
            # Then check for extra keys
            for key in d.keys():  # This might be the uncovered branch
                if key not in template_keys:
                    return False, f"mismatched keys: {path + key if path == '' else path + '.' + key}"
        
        # Check each key-value pair in template order
        for key in t:
            current_path = f"{path}.{key}" if path else key
            
            if isinstance(t[key], dict):
                # If template value is a dict, recurse
                if not isinstance(d[key], dict):
                    return False, f"bad type: {current_path}"
                result = validate_recursive(d[key], t[key], current_path)
                if not result[0]:  # This might be the uncovered line
                    return result
            else:
                # If template value is a type, check type match
                if not isinstance(d[key], t[key]):
                    return False, f"bad type: {current_path}"
        
        return True, ""
    
    return validate_recursive(data, template)
