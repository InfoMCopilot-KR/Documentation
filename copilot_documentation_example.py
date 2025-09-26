"""
GitHub Copilot Documentation Example Module

This module demonstrates best practices for writing documentation with GitHub Copilot's assistance.
It showcases various documentation techniques including:
- Comprehensive docstrings for modules, classes, and functions
- Type hints for better code clarity and IDE support
- Inline comments explaining complex logic
- Proper error handling documentation

Author: Created with GitHub Copilot assistance
Date: 2024
"""

from typing import List, Dict, Union, Tuple
import json
import logging
from dataclasses import dataclass
from enum import Enum


class DocumentationStyle(Enum):
    """
    Enumeration for different documentation styles supported.
    
    This enum defines the various documentation formats that can be generated
    or validated by the documentation utilities in this module.
    """
    GOOGLE = "google"
    NUMPY = "numpy"
    SPHINX = "sphinx"
    PYDOC = "pydoc"


@dataclass
class CodeDocumentation:
    """
    Data class representing code documentation metadata.
    
    This class encapsulates all the essential information needed to generate
    comprehensive documentation for a piece of code.
    
    Attributes:
        function_name (str): The name of the function or method
        description (str): Brief description of what the code does
        parameters (Dict[str, str]): Parameter names mapped to their descriptions
        return_type (str): Description of the return value
        examples (List[str]): List of usage examples
        raises (Dict[str, str]): Exception types mapped to descriptions
        style (DocumentationStyle): The documentation style to use
    """
    function_name: str
    description: str
    parameters: Dict[str, str]
    return_type: str
    examples: List[str]
    raises: Dict[str, str]
    style: DocumentationStyle = DocumentationStyle.GOOGLE


class DocumentationGenerator:
    """
    A utility class for generating and managing code documentation.
    
    This class provides methods to create, validate, and format documentation
    for Python code using various documentation standards. It's designed to work
    seamlessly with GitHub Copilot for enhanced productivity.
    """
    
    def __init__(self, default_style: DocumentationStyle = DocumentationStyle.GOOGLE):
        """
        Initialize the DocumentationGenerator with a default style.
        
        Args:
            default_style (DocumentationStyle): The default documentation style to use
                                              when no specific style is provided
        """
        self.default_style = default_style
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"DocumentationGenerator initialized with {default_style.value} style")
    
    def generate_docstring(self, doc_info: CodeDocumentation) -> str:
        """
        Generate a formatted docstring based on the provided documentation information.
        
        This method creates a well-formatted docstring according to the specified
        documentation style, including all necessary sections like parameters,
        return values, examples, and exceptions.
        
        Args:
            doc_info (CodeDocumentation): The documentation information containing
                                        all details needed for docstring generation
        
        Returns:
            str: A formatted docstring ready to be inserted into Python code
            
        Raises:
            ValueError: If the documentation info is incomplete or invalid
            TypeError: If doc_info is not a CodeDocumentation instance
            
        Examples:
            >>> generator = DocumentationGenerator()
            >>> doc_info = CodeDocumentation(
            ...     function_name="calculate_sum",
            ...     description="Calculate the sum of two numbers",
            ...     parameters={"a": "First number", "b": "Second number"},
            ...     return_type="The sum of a and b",
            ...     examples=["calculate_sum(2, 3)  # Returns 5"],
            ...     raises={}
            ... )
            >>> docstring = generator.generate_docstring(doc_info)
            >>> print(docstring)
            Calculate the sum of two numbers...
        """
        if not isinstance(doc_info, CodeDocumentation):
            raise TypeError("doc_info must be a CodeDocumentation instance")
        
        if not doc_info.function_name or not doc_info.description:
            raise ValueError("Function name and description are required")
        
        # Use the style specified in doc_info, or fall back to default
        style = doc_info.style or self.default_style
        
        # Generate docstring based on the selected style
        if style == DocumentationStyle.GOOGLE:
            return self._generate_google_style(doc_info)
        elif style == DocumentationStyle.NUMPY:
            return self._generate_numpy_style(doc_info)
        elif style == DocumentationStyle.SPHINX:
            return self._generate_sphinx_style(doc_info)
        else:
            # Default to Google style for unsupported styles
            self.logger.warning(f"Unsupported style {style}, using Google style")
            return self._generate_google_style(doc_info)
    
    def _generate_google_style(self, doc_info: CodeDocumentation) -> str:
        """
        Generate a Google-style docstring.
        
        Internal method to format documentation according to Google's Python
        style guide standards.
        
        Args:
            doc_info (CodeDocumentation): Documentation information to format
            
        Returns:
            str: Google-style formatted docstring
        """
        lines = [doc_info.description, ""]
        
        # Add parameters section if present
        if doc_info.parameters:
            lines.append("Args:")
            for param_name, param_desc in doc_info.parameters.items():
                lines.append(f"    {param_name}: {param_desc}")
            lines.append("")
        
        # Add return section if present
        if doc_info.return_type:
            lines.append("Returns:")
            lines.append(f"    {doc_info.return_type}")
            lines.append("")
        
        # Add raises section if present
        if doc_info.raises:
            lines.append("Raises:")
            for exception_type, exception_desc in doc_info.raises.items():
                lines.append(f"    {exception_type}: {exception_desc}")
            lines.append("")
        
        # Add examples section if present
        if doc_info.examples:
            lines.append("Examples:")
            for example in doc_info.examples:
                lines.append(f"    {example}")
        
        return "\n".join(lines).rstrip()
    
    def _generate_numpy_style(self, doc_info: CodeDocumentation) -> str:
        """
        Generate a NumPy-style docstring.
        
        Internal method to format documentation according to NumPy's
        documentation standards.
        
        Args:
            doc_info (CodeDocumentation): Documentation information to format
            
        Returns:
            str: NumPy-style formatted docstring
        """
        lines = [doc_info.description, ""]
        
        # Add parameters section
        if doc_info.parameters:
            lines.append("Parameters")
            lines.append("----------")
            for param_name, param_desc in doc_info.parameters.items():
                lines.append(f"{param_name} : type")
                lines.append(f"    {param_desc}")
            lines.append("")
        
        # Add returns section
        if doc_info.return_type:
            lines.append("Returns")
            lines.append("-------")
            lines.append("type")
            lines.append(f"    {doc_info.return_type}")
            lines.append("")
        
        # Add raises section
        if doc_info.raises:
            lines.append("Raises")
            lines.append("------")
            for exception_type, exception_desc in doc_info.raises.items():
                lines.append(f"{exception_type}")
                lines.append(f"    {exception_desc}")
            lines.append("")
        
        return "\n".join(lines).rstrip()
    
    def _generate_sphinx_style(self, doc_info: CodeDocumentation) -> str:
        """
        Generate a Sphinx-style docstring.
        
        Internal method to format documentation according to Sphinx
        reStructuredText standards.
        
        Args:
            doc_info (CodeDocumentation): Documentation information to format
            
        Returns:
            str: Sphinx-style formatted docstring
        """
        lines = [doc_info.description, ""]
        
        # Add parameters
        for param_name, param_desc in doc_info.parameters.items():
            lines.append(f":param {param_name}: {param_desc}")
        
        # Add return type
        if doc_info.return_type:
            lines.append(f":returns: {doc_info.return_type}")
        
        # Add raises
        for exception_type, exception_desc in doc_info.raises.items():
            lines.append(f":raises {exception_type}: {exception_desc}")
        
        return "\n".join(lines).rstrip()
    
    def validate_documentation(self, code_content: str) -> Dict[str, List[str]]:
        """
        Validate the documentation quality of Python code.
        
        This method analyzes Python code to check for documentation completeness
        and quality, providing suggestions for improvement. It's particularly useful
        when used with GitHub Copilot to ensure comprehensive documentation.
        
        Args:
            code_content (str): The Python code content to analyze
            
        Returns:
            Dict[str, List[str]]: A dictionary containing validation results with
                                keys 'missing_docstrings', 'suggestions', and 'warnings'
                                
        Raises:
            ValueError: If code_content is empty or invalid
            
        Examples:
            >>> generator = DocumentationGenerator()
            >>> code = '''
            ... def add_numbers(a, b):
            ...     return a + b
            ... '''
            >>> result = generator.validate_documentation(code)
            >>> print(result['missing_docstrings'])
            ['Function add_numbers is missing a docstring']
        """
        if not code_content or not isinstance(code_content, str):
            raise ValueError("Code content must be a non-empty string")
        
        validation_results = {
            'missing_docstrings': [],
            'suggestions': [],
            'warnings': []
        }
        
        # Simple validation logic (in practice, you'd use AST parsing)
        lines = code_content.split('\n')
        
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            
            # Check for function definitions without immediate docstrings
            if line_stripped.startswith('def ') and ':' in line_stripped:
                func_name = line_stripped.split('(')[0].replace('def ', '')
                # Look ahead for docstring
                next_lines = lines[i+1:i+3]
                has_docstring = any('"""' in nl or "'''" in nl for nl in next_lines)
                
                if not has_docstring:
                    validation_results['missing_docstrings'].append(
                        f'Function {func_name} is missing a docstring at line {i+1}'
                    )
                    validation_results['suggestions'].append(
                        f'Consider adding a docstring for {func_name} describing its purpose, '
                        'parameters, and return value'
                    )
            
            # Check for class definitions
            elif line_stripped.startswith('class ') and ':' in line_stripped:
                class_name = line_stripped.split('(')[0].replace('class ', '')
                next_lines = lines[i+1:i+3]
                has_docstring = any('"""' in nl or "'''" in nl for nl in next_lines)
                
                if not has_docstring:
                    validation_results['missing_docstrings'].append(
                        f'Class {class_name} is missing a docstring at line {i+1}'
                    )
        
        return validation_results
    
    def export_documentation_template(self, 
                                    filename: str, 
                                    format_type: str = "json") -> bool:
        """
        Export a documentation template for easy reuse.
        
        Creates a template file that can be used as a starting point for
        documenting new code. This is particularly helpful when working
        with GitHub Copilot to maintain consistency across projects.
        
        Args:
            filename (str): The name of the file to create
            format_type (str, optional): The format for the template ('json' only supported).
                                       Defaults to 'json'.
        
        Returns:
            bool: True if the template was successfully created, False otherwise
            
        Raises:
            IOError: If the file cannot be written
            ValueError: If format_type is not 'json'
            
        Examples:
            >>> generator = DocumentationGenerator()
            >>> success = generator.export_documentation_template("doc_template.json")
            >>> print(f"Template created: {success}")
            Template created: True
        """
        if format_type not in ["json"]:
            raise ValueError("format_type must be 'json'")
        
        template = {
            "function_name": "your_function_name",
            "description": "Brief description of what the function does",
            "parameters": {
                "param1": "Description of parameter 1",
                "param2": "Description of parameter 2"
            },
            "return_type": "Description of what the function returns",
            "examples": [
                "Example usage 1",
                "Example usage 2"
            ],
            "raises": {
                "ValueError": "When this exception is raised",
                "TypeError": "When this exception is raised"
            },
            "style": "google"
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(template, f, indent=2)
            
            self.logger.info(f"Documentation template exported to {filename}")
            return True
            
        except IOError as e:
            self.logger.error(f"Failed to export template: {e}")
            return False


def calculate_statistics(numbers: List[Union[int, float]]) -> Tuple[float, float, float]:
    """
    Calculate basic statistics for a list of numbers.
    
    This function computes mean, median, and standard deviation for a given
    list of numeric values. It demonstrates proper type hints and comprehensive
    documentation that can be generated with GitHub Copilot's assistance.
    
    Args:
        numbers (List[Union[int, float]]): A list of numeric values to analyze.
                                         Must contain at least one element.
    
    Returns:
        Tuple[float, float, float]: A tuple containing (mean, median, std_deviation)
        
    Raises:
        ValueError: If the numbers list is empty
        TypeError: If any element in numbers is not numeric
        
    Examples:
        >>> stats = calculate_statistics([1, 2, 3, 4, 5])
        >>> print(f"Mean: {stats[0]:.2f}")
        Mean: 3.00
        
        >>> mean, median, std_dev = calculate_statistics([10, 20, 30])
        >>> print(f"Statistics: {mean}, {median}, {std_dev:.2f}")
        Statistics: 20.0, 20.0, 8.16
    """
    if not numbers:
        raise ValueError("Numbers list cannot be empty")
    
    # Validate that all elements are numeric
    for i, num in enumerate(numbers):
        if not isinstance(num, (int, float)):
            raise TypeError(f"Element at index {i} is not numeric: {type(num)}")
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        # Even number of elements
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        # Odd number of elements
        median = sorted_numbers[n // 2]
    
    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_deviation = variance ** 0.5
    
    return mean, median, std_deviation


def find_duplicates_with_positions(data: List[str]) -> Dict[str, List[int]]:
    """
    Find duplicate strings in a list and return their positions.
    
    This utility function identifies all duplicate strings in a list and
    returns a dictionary mapping each duplicate string to all positions
    where it appears. Demonstrates complex logic documentation.
    
    Args:
        data (List[str]): List of strings to analyze for duplicates
        
    Returns:
        Dict[str, List[int]]: Dictionary where keys are duplicate strings
                             and values are lists of 0-based indices where
                             each string appears
                             
    Examples:
        >>> data = ["apple", "banana", "apple", "cherry", "banana"]
        >>> duplicates = find_duplicates_with_positions(data)
        >>> print(duplicates)
        {'apple': [0, 2], 'banana': [1, 4]}
        
        >>> # No duplicates case
        >>> unique_data = ["cat", "dog", "bird"]
        >>> result = find_duplicates_with_positions(unique_data)
        >>> print(result)
        {}
    """
    position_map = {}
    duplicates = {}
    
    # First pass: map each string to all its positions
    for index, item in enumerate(data):
        if item not in position_map:
            position_map[item] = []
        position_map[item].append(index)
    
    # Second pass: identify items that appear more than once
    for item, positions in position_map.items():
        if len(positions) > 1:  # Item appears multiple times
            duplicates[item] = positions
    
    return duplicates


if __name__ == "__main__":
    """
    Demonstration of the documentation utilities.
    
    This main section shows how to use the DocumentationGenerator class
    and related functions. It serves as both example code and a test
    of the implemented functionality.
    """
    # Configure logging for demonstration
    logging.basicConfig(level=logging.INFO)
    
    print("GitHub Copilot Documentation Example")
    print("=" * 40)
    
    # Create a documentation generator
    doc_generator = DocumentationGenerator()
    
    # Example 1: Generate documentation for a function
    print("\n1. Generating documentation for a sample function:")
    sample_doc = CodeDocumentation(
        function_name="process_data",
        description="Process and clean input data for analysis",
        parameters={
            "raw_data": "List of raw data elements to process",
            "clean_nulls": "Whether to remove null values"
        },
        return_type="Processed and cleaned data list",
        examples=[
            "process_data(['a', None, 'b'], clean_nulls=True)",
            "# Returns ['a', 'b']"
        ],
        raises={
            "ValueError": "If raw_data is empty",
            "TypeError": "If raw_data is not a list"
        }
    )
    
    generated_docstring = doc_generator.generate_docstring(sample_doc)
    print(generated_docstring)
    
    # Example 2: Validate documentation
    print("\n2. Validating code documentation:")
    sample_code = '''
def add(a, b):
    return a + b

class Calculator:
    def multiply(self, x, y):
        return x * y
'''
    
    validation_results = doc_generator.validate_documentation(sample_code)
    print("Missing docstrings:", validation_results['missing_docstrings'])
    print("Suggestions:", validation_results['suggestions'])
    
    # Example 3: Demonstrate utility functions
    print("\n3. Testing utility functions:")
    
    # Statistics calculation
    test_numbers = [1, 2, 3, 4, 5, 2, 3]
    mean, median, std_dev = calculate_statistics(test_numbers)
    print(f"Statistics for {test_numbers}:")
    print(f"  Mean: {mean:.2f}, Median: {median:.2f}, Std Dev: {std_dev:.2f}")
    
    # Duplicate finding
    test_strings = ["hello", "world", "hello", "python", "world"]
    duplicates = find_duplicates_with_positions(test_strings)
    print(f"\nDuplicates in {test_strings}:")
    for item, positions in duplicates.items():
        print(f"  '{item}' appears at positions: {positions}")
    
    print("\nDemonstration completed!")