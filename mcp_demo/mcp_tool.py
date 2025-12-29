from mcp.server.fastmcp import FastMCP
import math
import requests


mcp= FastMCP("test_tools")

@mcp.tool()
def add(a:float, b:float) -> int:
    """Add two numbers and return the result."""
    result = a + b
    return result

@mcp.tool()
def subtract(a:float, b:float) -> int:
    """Subtract two numbers and return the result."""
    result = a - b
    return result

@mcp.tool()
def multiply(a:float, b:float) -> int:
    """Multiply two numbers and return the result."""
    result = a * b
    return result

@mcp.tool()
def divide(a:float, b:float) -> float:
    """Divide two numbers and return the result."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    result = a / b
    return result

@mcp.tool()
def power(base:float, exponent:float) -> float:
    """Raise a number to a power and return the result."""
    result = math.pow(base, exponent)
    return result


@mcp.tool()
def ecl(pd:float, lgd:float, ead:float)-> float:
    """Calculate the Expected Credit Loss (ECL) using the formula:
    ECL = PD * LGD * EAD
    where:
    PD = Probability of Default
    LGD = Loss Given Default
    EAD = Exposure at Default
    """
    el =  pd * lgd * ead
    
    
    return el
    

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="stdio") 