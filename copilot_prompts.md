# GitHub Copilot Prompts for Documentation

This document contains example prompts that demonstrate how to effectively use GitHub Copilot for generating and improving code documentation. These prompts are designed to help developers create comprehensive, well-structured documentation with Copilot's assistance.

## Table of Contents

1. [Function Docstring Generation](#function-docstring-generation)
2. [Class Documentation](#class-documentation)
3. [Module-Level Documentation](#module-level-documentation)
4. [Type Hints and Comments](#type-hints-and-comments)
5. [README Generation](#readme-generation)
6. [API Documentation](#api-documentation)
7. [Code Comments](#code-comments)
8. [Error Handling Documentation](#error-handling-documentation)

## Function Docstring Generation

### Basic Function Docstring

**Prompt:**
```
Generate a comprehensive Google-style docstring for this function:

def calculate_compound_interest(principal, rate, time, compound_frequency=1):
    result = principal * (1 + rate/compound_frequency) ** (compound_frequency * time)
    return result
```

**Expected Output:**
```python
def calculate_compound_interest(principal, rate, time, compound_frequency=1):
    """
    Calculate compound interest for a given principal amount.
    
    This function computes the final amount after compound interest is applied
    over a specified time period with a given interest rate and compounding frequency.
    
    Args:
        principal (float): The initial amount of money invested or borrowed
        rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%)
        time (float): The time period in years
        compound_frequency (int, optional): Number of times interest is compounded
                                          per year. Defaults to 1 (annually).
    
    Returns:
        float: The final amount after compound interest is applied
        
    Examples:
        >>> calculate_compound_interest(1000, 0.05, 2, 4)
        1104.49
        
        >>> calculate_compound_interest(5000, 0.03, 10)
        6719.58
    """
    result = principal * (1 + rate/compound_frequency) ** (compound_frequency * time)
    return result
```

### Function with Complex Parameters

**Prompt:**
```
Add a NumPy-style docstring with detailed parameter descriptions and examples for this data processing function:

def process_user_data(users, filters=None, sort_by='name', ascending=True):
    # Function implementation here
    pass
```

### Function with Exception Handling

**Prompt:**
```
Generate a docstring that includes proper Raises section for this function that validates email addresses:

def validate_email_list(email_addresses):
    if not email_addresses:
        raise ValueError("Email list cannot be empty")
    
    for email in email_addresses:
        if '@' not in email:
            raise ValueError(f"Invalid email format: {email}")
    
    return True
```

## Class Documentation

### Basic Class Docstring

**Prompt:**
```
Create a comprehensive class docstring for this data structure:

class TaskManager:
    def __init__(self, max_tasks=100):
        self.tasks = []
        self.max_tasks = max_tasks
    
    def add_task(self, task):
        # Implementation
        pass
    
    def remove_task(self, task_id):
        # Implementation
        pass
```

### Class with Inheritance

**Prompt:**
```
Generate documentation for this class that inherits from a base class, including information about the inheritance relationship:

class DatabaseUser(BaseUser):
    def __init__(self, username, email, database_permissions):
        super().__init__(username, email)
        self.database_permissions = database_permissions
```

## Module-Level Documentation

### Module Header Documentation

**Prompt:**
```
Generate a comprehensive module docstring for a Python file that contains utilities for file processing, including author information, version, and usage examples.
```

### Package Documentation

**Prompt:**
```
Create an __init__.py docstring for a package called 'analytics' that provides data analysis tools, including information about submodules and main functionality.
```

## Type Hints and Comments

### Adding Type Hints

**Prompt:**
```
Add comprehensive type hints to this function signature and update the docstring accordingly:

def merge_dictionaries(dict1, dict2, overwrite=False):
    """Merge two dictionaries with optional overwrite behavior."""
    # Implementation here
    pass
```

**Expected Enhancement:**
```python
from typing import Dict, Any, Union

def merge_dictionaries(
    dict1: Dict[str, Any], 
    dict2: Dict[str, Any], 
    overwrite: bool = False
) -> Dict[str, Any]:
    """
    Merge two dictionaries with optional overwrite behavior.
    
    Args:
        dict1 (Dict[str, Any]): The base dictionary to merge into
        dict2 (Dict[str, Any]): The dictionary to merge from
        overwrite (bool, optional): Whether to overwrite existing keys. 
                                   Defaults to False.
    
    Returns:
        Dict[str, Any]: A new dictionary containing merged key-value pairs
    """
    # Implementation here
    pass
```

### Complex Type Annotations

**Prompt:**
```
Add proper type hints for this function that works with nested data structures:

def transform_nested_data(data, transformers, default_value=None):
    """Apply transformation functions to nested dictionary data."""
    # Implementation
    pass
```

## README Generation

### Project README Structure

**Prompt:**
```
Generate a comprehensive README.md structure for a Python library called "DataProcessor" that provides tools for cleaning and analyzing CSV data. Include sections for installation, usage examples, API reference, and contributing guidelines.
```

### Feature Documentation

**Prompt:**
```
Create a detailed feature description for a README that explains how to use a caching decorator in a Python library, including code examples and configuration options.
```

## API Documentation

### REST API Endpoint Documentation

**Prompt:**
```
Generate API documentation for this Flask route that handles user authentication:

@app.route('/api/auth/login', methods=['POST'])
def login():
    # Login implementation
    return jsonify({'token': 'example_token'})
```

### Function API Documentation

**Prompt:**
```
Create detailed API documentation for this public function that will be used by external developers:

def create_report(data_source, report_type, filters=None, format='pdf'):
    """Generate a report from the specified data source."""
    # Implementation
    pass
```

## Code Comments

### Inline Comments for Complex Logic

**Prompt:**
```
Add explanatory comments to this complex algorithm implementation:

def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
    
    return arr
```

### Algorithm Explanation Comments

**Prompt:**
```
Add step-by-step comments explaining this binary search implementation:

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

## Error Handling Documentation

### Exception Documentation

**Prompt:**
```
Generate comprehensive documentation for custom exceptions in this module:

class DataValidationError(Exception):
    pass

class DatabaseConnectionError(Exception):
    pass

class ConfigurationError(Exception):
    pass
```

### Error Handling Examples

**Prompt:**
```
Create documentation with examples showing proper exception handling for this file operation function:

def read_config_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Handle file not found
        pass
    except json.JSONDecodeError:
        # Handle invalid JSON
        pass
```

## Advanced Copilot Prompts

### Multi-Language Documentation

**Prompt:**
```
Generate bilingual documentation (English and Korean) for this function that processes international user data:

def process_international_users(users_data, localization_settings):
    # Implementation
    pass
```

### Performance Documentation

**Prompt:**
```
Add performance-focused documentation including time complexity, space complexity, and optimization notes for this sorting function:

def hybrid_sort(arr, threshold=10):
    if len(arr) <= threshold:
        return insertion_sort(arr)
    else:
        return quick_sort(arr)
```

### Security Documentation

**Prompt:**
```
Generate security-focused documentation for this authentication function, including security considerations and potential vulnerabilities:

def authenticate_user(username, password, session_data):
    # Authentication implementation
    pass
```

## Best Practices for Using Copilot with Documentation

### Effective Prompt Strategies

1. **Be Specific**: Include the exact function signature and context
2. **Specify Style**: Mention the documentation style you want (Google, NumPy, Sphinx)
3. **Request Examples**: Ask for usage examples and edge cases
4. **Include Context**: Provide information about the module or class context
5. **Ask for Completeness**: Request all sections (Args, Returns, Raises, Examples)

### Prompt Templates

#### General Function Documentation
```
Generate a comprehensive [STYLE]-style docstring for this Python function:

[FUNCTION_CODE]

Please include:
- Clear description of purpose
- All parameters with types and descriptions
- Return value description
- Usage examples
- Possible exceptions
```

#### Class Documentation Template
```
Create detailed documentation for this Python class:

[CLASS_CODE]

Include:
- Class purpose and usage
- Attribute descriptions
- Method summaries
- Inheritance information if applicable
- Usage examples
```

#### Module Documentation Template
```
Generate a module-level docstring for a Python file containing:

[MODULE_DESCRIPTION]

Include:
- Module purpose
- Main functions/classes
- Usage examples
- Author and version information
```

## Tips for Better Documentation with Copilot

1. **Iterative Improvement**: Start with basic prompts and refine based on output
2. **Context Provision**: Give Copilot context about the broader application
3. **Style Consistency**: Maintain consistent documentation style across your project
4. **Review and Edit**: Always review Copilot-generated documentation for accuracy
5. **Update Regularly**: Keep documentation current with code changes

## Common Copilot Documentation Patterns

### Pattern 1: Step-by-Step Documentation
```
# Prompt: "Add step-by-step comments explaining what each part of this function does"
```

### Pattern 2: Example-Driven Documentation
```
# Prompt: "Generate docstring with at least 3 different usage examples"
```

### Pattern 3: Error-Focused Documentation
```
# Prompt: "Document all possible exceptions and error conditions for this function"
```

### Pattern 4: Performance Documentation
```
# Prompt: "Add documentation explaining the time and space complexity of this algorithm"
```

This comprehensive guide should help developers effectively use GitHub Copilot to create high-quality documentation for their Python projects.