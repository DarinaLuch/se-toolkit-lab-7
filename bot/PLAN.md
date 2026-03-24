# Development Plan: Telegram Bot for LMS Analytics

## Overview
This bot provides access to LMS analytics through Telegram. Users can query scores, view lab statistics, and get AI-powered recommendations.

## Architecture Approach

### 1. Testable Handlers (P0.1)
- All command logic lives in `handlers/` directory
- Handlers are pure functions: `(args, config) -> str`
- No Telegram API calls in handlers
- Enables testing via `--test` flag

### 2. Configuration Management
- `.env.bot.secret` for sensitive data (tokens, keys)
- `.env.bot.example` as template
- `config.py` loads and validates all env vars

### 3. Service Layer
- `services/lms_client.py`: HTTP client for backend API
- `services/llm_client.py`: LLM integration for intent routing
- Separates API logic from command handling

### 4. Entry Point (`bot.py`)
- Two modes: Telegram polling and `--test` CLI
- `--test` mode: parse command, call handler, print output
- Telegram mode: use python-telegram-bot library

### 5. Implementation Phases

**Phase 1: Scaffold (This Task)**
- Create directory structure
- Set up `pyproject.toml` with dependencies
- Implement basic handlers with placeholder responses
- Add `--test` mode support

**Phase 2: Backend Integration (Task 2)**
- Implement LMS API client
- Add `/scores`, `/labs`, `/health` commands
- Fetch real data from backend

**Phase 3: Intent Routing (Task 3)**
- Add LLM client for natural language queries
- Implement intent classification
- Route questions to appropriate handlers

**Phase 4: Deployment**
- Deploy on VM with systemd or nohup
- Ensure `.env.bot.secret` is properly configured
- Verify both `--test` and Telegram modes work

## Key Decisions
- Use `python-telegram-bot` v20+ for async support
- Use `httpx` for HTTP requests
- Use `pydantic-settings` for type-safe config
- Keep handlers synchronous for simplicity in `--test` mode

## Testing Strategy
1. Test each handler with `--test` flag
2. Verify backend API calls with mock responses
3. Integration test on VM before Telegram deployment
4. Monitor logs for errors in production
