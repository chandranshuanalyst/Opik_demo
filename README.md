# MCP Demo with Comet Opik for observability

A demonstration of integrating **Opik** (LLM observability platform) with **MCP** (Model Context Protocol) to build an intelligent agent powered by LangChain and Groq.

## Overview

This project showcases how to:
- Create an MCP server that exposes custom tools (arithmetic operations and financial calculations)
- Build an intelligent agent using LangChain that leverages MCP tools
- Monitor agent behavior and LLM interactions with Opik for observability
- Execute complex multi-step tasks with an AI agent

### Key Features

- **MCP Server** (`mcp_tool.py`): Provides tools for:
  - Basic arithmetic: add, subtract, multiply, divide, power
  - Financial calculation: Expected Credit Loss (ECL) computation
  
- **LangChain Agent** (`main.py`): Orchestrates tool usage to answer complex questions
  
- **Opik Integration**: Full LLM observability and tracing for debugging and monitoring

## Prerequisites

- Python 3.10 or higher
- API keys for:
  - **Groq** (for the LLM)
  - **Opik** (for observability)
