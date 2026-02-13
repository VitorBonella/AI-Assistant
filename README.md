# AI Assistant with Calculator Tool

## 📌 Project Overview

This project implements a simple AI Assistant capable of answering
general questions using a Large Language Model (LLM) and invoking an
external calculator tool when a mathematical question is detected.

The assistant decides whether to: 
- Respond directly using an LLM
- Invoke a calculator tool to compute exact numerical results before
answering

The goal is to demonstrate structured thinking, clean architecture
principles, LLM integration, and tool orchestration.

------------------------------------------------------------------------

## 🚀 How to Run the Project

### 1️⃣ Requirements

-   Docker
-   Docker Compose
-   A [Google AI Studio API Key](https://aistudio.google.com/app/api-keys) with access to the model:
    -   `gemini-2.5-flash-lite`

⚠️ **Do not share your API key publicly.**

### 2️⃣ Build and Run

``` bash
docker-compose up --build
```

After the container starts, access the application at:

    http://localhost:8501

------------------------------------------------------------------------

## 🤖 Available Model Implementations

Currently, two LLM provider implementations are available:

1.  **Google Gemini using the official Python SDK**
2.  **Google Gemini using LangChain**

You can select the desired model in the UI and provide the corresponding
API key.

------------------------------------------------------------------------

## 🧠 Implementation Logic

The assistant follows this decision flow:

1.  The user submits a question.
2.  The assistant determines whether the input is a mathematical
    expression.
3.  If it is mathematical:
    -   The calculator tool is invoked.
    -   The result is returned to the user.
4.  Otherwise:
    -   The question is sent directly to the selected LLM provider.

The assistant acts strictly as an **orchestrator**:

-   The **Calculator** is responsible only for arithmetic operations.
-   The **LLM Provider** is responsible only for communicating with the
    model API.
-   The **Assistant** coordinates both components.

This ensures compliance with the **Single Responsibility Principle
(SRP)**.

------------------------------------------------------------------------

## 🏗️ Architecture & Design Decisions

The project follows:

-   SOLID Principles
-   Clean Architecture
-   Design Patterns (Factory + Strategy)

### 📁 Project Structure

    App/
     ├── core/
     ├── infrastructure/
     ├── interfaces/
     └── ui/

### 🔹 core

Contains the domain entities and business rules.

### 🔹 infrastructure

-   Implements the **Factory Pattern** to instantiate the correct LLM
    provider.
-   Contains integrations with:
    -   Google SDK
    -   LangChain
    -   Calculator tool

### 🔹 interfaces

Defines abstractions such as `ILLMProvider`.

This enables: - Dependency Inversion
- Easy model replacement
- High extensibility

The `Assistant` depends on `ILLMProvider`, not on concrete
implementations.

### 🔹 ui

Implements the frontend using **Streamlit**.

------------------------------------------------------------------------

## 🔄 Difference Between SDK and LangChain Implementation

### Google SDK

-   Uses native function calling
-   Automatically handles tool execution and response generation
-   More direct integration

### LangChain

-   Provides explicit control over chains and tool invocation
-   Requires manual configuration of tool behavior
-   Greater flexibility for complex agent workflows

------------------------------------------------------------------------

## 📚 What I Learned

This challenge reinforced:

-   Clean architecture organization for LLM-based systems
-   Practical differences between native SDK integration and agent
    frameworks like LangChain
-   Updated usage patterns from the latest Google SDK documentation

It also highlighted API rate-limit considerations when working with
Google AI Studio Free Tier.

------------------------------------------------------------------------

## 🔮 What I Would Improve With More Time

With additional time, I would:

-   Implement unit tests and integration tests
-   Add automated provider connectivity validation
-   Improve error handling with custom exception classes
-   Add structured logging
-   Expand mathematical parsing capabilities
-   Add additional tools (e.g., weather API or public data API)

------------------------------------------------------------------------

## ⏱️ Development Context

The challenge email was received on **February 12, 2026 (4:32 PM)**.

Due to a previously scheduled trip during the Brazilian Carnival holiday
(February 14--18, 2026), I had limited internet access during that
period. As a result, the implementation was completed within a short
development window outside of those dates.

The solution was intentionally focused on delivering a clean,
well-structured, and functional implementation within the available
timeframe, prioritizing architecture clarity and separation of concerns.
