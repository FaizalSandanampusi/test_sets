![CI/CD](https://github.com/FaizalSandanampusi/test_sets/workflows/Python%20Tests/badge.svg?label=passingcolor=greentimestamp=1730371659)

![CI/CD](https://github.com/FaizalSandanampusi/Assignment_Test/workflows/Python%20Tests/badge.svg?label=passing&color=green&timestamp=1729536353)

# Dictionary Utilities

This project is designed to provide tools for validating the structure and data types of nested dictionaries and merging multiple dictionaries. It consists of two modules: **Dictionary Validation** and **Dictionary Merging**. These utilities are particularly useful when working with JSON data in APIs, ensuring that data conforms to required structures and allowing for efficient aggregation of dictionary data.

### Dictionary Structure Validator
---

This module is designed to validate the structure and data types of nested dictionaries against a specified template. This is useful when dealing with JSON data in APIs, where you need to ensure that the data conforms to a required structure before processing it.

#### Features

- **Recursive Validation:** Handles deeply nested dictionaries.
- **Detailed Error Reporting:** Reports the first error encountered with specific information about:
  - Missing keys
  - Mismatched data types
  - Extra keys

#### Function Definition

```python
def validate(data, template):
    """
    Validates a nested dictionary against a template.
    
    Args:
        data: Dictionary to validate
        template: Template dictionary to validate against
        
    Returns:
        tuple: (bool, str) where bool indicates if valid and str contains error message
    """
```

- **Arguments:**
  - `data`: The dictionary to be validated.
  - `template`: The template dictionary which defines the required structure and data types for `data`.
  
- **Returns:** 
  - A tuple consisting of:
    - A boolean (`True` if `data` is valid, `False` otherwise).
    - An error message string (`''` if valid; otherwise, a message describing the mismatch).

#### Helper Function Definition

```python
def validate_recursive(d, t, path=""):
```

- **Purpose:** A helper function defined inside `validate` for recursive validation of nested dictionaries.
  
- **Arguments:**
  - `d`: The current level of `data` being validated.
  - `t`: The current level of `template` being checked against.
  - `path`: A string representing the nested key path, used to give context in error messages.

#### How It Works

1. **Key Comparison:**
   ```python
   data_keys = set(d.keys())
   template_keys = set(t.keys())
   ```
   - `data_keys` and `template_keys` are sets of keys in `d` and `t`, respectively.
   - These sets allow easy comparison to identify missing or extra keys.

2. **Checking Missing or Extra Keys:**
   ```python
   if data_keys != template_keys:
       ...
   ```
   - If `data_keys` and `template_keys` don’t match, it identifies either missing or extra keys.
   - It reports the first mismatched key in the format `mismatched keys: key_path`.

3. **Recursive Validation:**
   ```python
   for key in t:
       current_path = f"{path}.{key}" if path else key
       ...
   ```
   - This loop iterates over each key in `template` to check the structure and type for each key.
   - It calls `validate_recursive` if the value in `template` is a dictionary to continue validating at the next level of nesting.

4. **Type Checking:**
   ```python
   if not isinstance(d[key], t[key]):
       return False, f"bad type: {current_path}"
   ```
   - If the type of `data[key]` does not match the type specified in `template[key]`, it returns a `bad type` error.

5. **Final Result:**
   ```python
   return True, ""
   ```
   - If all keys and types match at the current level, `validate_recursive` returns `True` with an empty error message.

#### Starting the Validation

```python
return validate_recursive(data, template)
```
- The `validate` function initiates the validation by calling `validate_recursive` with the top-level `data` and `template`.


### Dictionary Merge Functions

#### Overview

Merging dictionaries is a common task in data processing, especially when aggregating counts or frequencies from various sources. 

This module provides two functions to merge multiple dictionaries: `merge_with_defaultdict` and `merge_with_counter`. Both functions allow for the aggregation of values from different dictionaries while ensuring that the resulting dictionary is sorted based on the combined frequencies of the keys.

The provided functions utilize Python's `collections` module to efficiently handle merging and counting operations.

### Function Definitions

#### `merge_with_defaultdict`

```python
def merge_with_defaultdict(*dicts):
    """
    Merges multiple dictionaries using defaultdict and returns a sorted dictionary.
    
    Args:
        *dicts: Variable number of dictionaries to merge.
        
    Returns:
        dict: Merged dictionary with combined frequencies, sorted by frequency in descending order.
    """
```

- **Arguments:**
  - `*dicts`: A variable number of dictionaries that you want to merge.
  
- **Returns:** A single dictionary containing the merged key-value pairs, sorted by frequency in descending order.

#### How It Works

The `merge_with_defaultdict` function works as follows:

1. **Initialization:** A `defaultdict` of type `int` is created to store the merged results. This allows for automatic initialization of keys with a default value of `0`.

2. **Aggregation:** The function iterates through each provided dictionary, updating the merged dictionary by adding the value for each key. If a key is encountered multiple times, its values are summed.

3. **Sorting:** The merged dictionary is converted to a regular dictionary and sorted by the frequency of values in descending order using the `sorted()` function.

#### Example Usage

```python
dict1 = {'a': 3, 'b': 5}
dict2 = {'b': 2, 'c': 7}
dict3 = {'a': 1, 'c': 1}

merged_dict = merge_with_defaultdict(dict1, dict2, dict3)
print(merged_dict)
```

### Merged Output

For the above example, the output will be:

```json
{
    "c": 8,
    "b": 7,
    "a": 4
}
```

#### `merge_with_counter`

```python
def merge_with_counter(*dicts):
    """
    Merges multiple dictionaries using Counter and returns a sorted dictionary.
    
    Args:
        *dicts: Variable number of dictionaries to merge.
        
    Returns:
        dict: Merged dictionary with combined frequencies, sorted by frequency in descending order.
    """
```

- **Arguments:**
  - `*dicts`: A variable number of dictionaries to be merged.

- **Returns:** A dictionary containing the merged key-value pairs, sorted by frequency in descending order.

#### How It Works

The `merge_with_counter` function operates as follows:

1. **Initialization:** A `Counter` object is created to facilitate counting the occurrences of keys.

2. **Updating Counts:** The function updates the `Counter` with each provided dictionary, automatically aggregating the values for any duplicate keys.

3. **Sorting:** The merged results are converted to a standard dictionary using `most_common()`, which returns a list of the keys sorted by their frequency.

#### Example Usage

```python
dict1 = {'a': 3, 'b': 5}
dict2 = {'b': 2, 'c': 7}
dict3 = {'a': 1, 'c': 1}

merged_dict_counter = merge_with_counter(dict1, dict2, dict3)
print(merged_dict_counter)
```

### Merged Output

For the above example, the output will be:

```json
{
    "c": 8,
    "b": 7,
    "a": 4
}
```

### Comparison of Functions

- **`merge_with_defaultdict`:** A more explicit approach using `defaultdict`, which provides automatic initialization of keys with a default value.
  
- **`merge_with_counter`:** Utilizes the `Counter` class for counting hashable objects, making it concise and efficient for counting operations.



## Testing

The project includes comprehensive test cases written in `pytest`. Each test case checks different validation scenarios, ensuring the correctness of both the validation and merging functions.

### Tests and Explanations for dictionary template validation

The tests are structured to verify the correctness of the `validate` function across various cases:

1. **`test_valid_data()`**
   - **Purpose:** Tests that the function returns `True` for a dictionary that perfectly matches the template structure and types.
   - **Expected Result:** `(True, '')`

2. **`test_missing_key()`**
   - **Purpose:** Checks if the function correctly identifies a missing key (`bio.birthplace.city`).
   - **Expected Result:** `(False, 'mismatched keys: bio.birthplace.city')`

3. **`test_bad_type()`**
   - **Purpose:** Validates that the function detects a type mismatch (`bio.dob.month` is `str` instead of `int`).
   - **Expected Result:** `(False, 'bad type: bio.dob.month')`

4. **`test_extra_key()`**
   - **Purpose:** Ensures that an extra key not specified in the template (`name.middle`) is flagged.
   - **Expected Result:** `(False, 'mismatched keys: name.middle')`

5. **`test_wrong_type_at_top_level()`**
   - **Purpose:** Checks for type mismatch at the top level (`user_id` should be `int`).
   - **Expected Result:** `(False, 'bad type: user_id')`

6. **`test_missing_top_level_key()`**
   - **Purpose:** Validates detection of a missing top-level key (`user_id`).
   - **Expected Result:** `(False, 'mismatched keys: user_id')`

7. **`test_additional_nested_key()`**
   - **Purpose:** Ensures an additional nested key (`bio.birthplace.postcode`) is correctly flagged.
   - **Expected Result:** `(False, 'mismatched keys: bio.birthplace.postcode')`

8. **`test_empty_dictionary()`**
   - **Purpose:** Checks if an empty dictionary fails due to missing keys.
   - **Expected Result:** `(False, 'mismatched keys: user_id')`

9. **`test_none_value()`**
   - **Purpose:** Ensures type mismatch is detected if a `None` value is used where a specific type (`str`) is expected (`name.last`).
   - **Expected Result:** `(False, 'bad type: name.last')`

10. **`test_correct_types_but_extra_keys()`**
    - **Purpose:** Checks for correct types but additional keys in the dictionary.
    - **Expected Result:** `(False, 'mismatched keys: bio.spouse')`

11. **`test_wrong_type_in_nested_dict()`**
    - **Purpose:** Validates that a nested type mismatch (list instead of str) is detected (`bio.birthplace.city`).
    - **Expected Result:** `(False, 'bad type: bio.birthplace.city')`



### Testing and Explanation for dictionary merge functions


1. **`test_merge_with_defaultdict_valid_data()`**
   - **Purpose:** Tests that the function successfully merges multiple dictionaries using `defaultdict`.
   - **Expected Result:** A correctly merged dictionary with frequencies.

2. **`test_merge_with_counter_valid_data()`**
   - **Purpose:** Tests that the function successfully merges multiple dictionaries using `Counter`.
   - **Expected Result:** A correctly merged dictionary with frequencies.

3. **`test_merge_with_empty_dicts()`**
   - **Purpose:** Ensures that merging empty dictionaries returns an empty dictionary.
   - **Expected Result:** `{}`

4. **`test_merge_with_no_common_keys()`**
   - **Purpose:** Validates merging dictionaries with no common keys.
   - **Expected Result:** Combined dictionary containing all keys.

---

### Running the Tests

To run the tests, ensure `pytest` is installed, then execute:

```bash
pytest tests/ --cov=src/
```

## GitHub Actions

This project includes GitHub Actions for continuous integration, which automates the process of testing the code every time changes are made. It runs tests on push or pull request events to the `main` branch, ensuring that code quality is maintained and that tests are always up-to-date.
