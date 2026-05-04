# Agentic Design Blueprint

- Generated at: 2026-05-04T14:27:12+01:00
- Source commit: 53a3f5262747e62d85ae385aae21a400bbf78f67
- Content version: 53a3f5262747

## Summary

This document defines the core design principles for AI-enabled products and services in which the system does more than respond to user inputs. It interprets intent, performs actions, coordinates processes, and completes work on the user’s behalf.

Conventional digital experiences were designed around direct interaction. In that model, the user remains the primary operator throughout the journey, progressing step by step through a sequence of actions.

AI systems, particularly agentic systems, introduce a materially different model. In these environments, the user is no longer solely the operator of the interface. Instead, the user increasingly assumes the role of supervisor, director, or decision-maker, while the system undertakes execution.

This blueprint establishes the design principles required to support that transition responsibly and coherently.

## Strategic Premise

Traditional interaction design rests on several assumptions:

* the user is continuously present
* the user performs each material step directly
* the user requires visibility of each stage of the process
* the interface is the principal site of value creation

These assumptions weaken when AI systems are capable of acting independently, operating asynchronously, and coordinating work across tools, data sources, or multiple agents.

In an agentic context, the product experience is no longer defined solely by the visible interface. It is defined by the relationship between:

* user intent
* delegated authority
* system execution
* visibility and accountability
* human intervention when required
* review and acceptance of outcomes

The central design question therefore changes.

It is no longer only: **How does the user complete the task?**

It becomes: **How does the user delegate the task safely, remain appropriately informed, and intervene only when necessary?**

## Design Philosophy

The objective of AI design is not to create an impression of magic.

The objective is to make autonomy:

* understandable
* trustworthy
* governable
* interruptible
* reviewable

The ambition should not be invisible intelligence. It should be **legible autonomy**.

Systems that act on behalf of users must be designed in a manner that preserves clarity, supports confidence, and maintains an appropriate balance between automation and human oversight.

## Clusters

### Delegation

Principles that help teams move from direct manipulation toward bounded, steerable delegation.

Principles: Design for delegation rather than direct manipulation, Replace implied magic with clear mental models, Optimise for steering, not only initiating

### Visibility

Principles that keep background AI work legible through clear signals, system state, and operator context.

Principles: Ensure that background work remains perceptible, Align feedback with the user’s level of attention, Expose meaningful operational state, not internal complexity

### Trust

Principles that make system authority, inspectability, and review boundaries explicit.

Principles: Apply progressive disclosure to system agency, Establish trust through inspectability, Make hand-offs, approvals, and blockers explicit

### Orchestration

Principles that model delegated work as systems with visible nodes, handoffs, and review points.

Principles: Represent delegated work as a system, not merely as a conversation

## Principles

### 1. Design for delegation rather than direct manipulation

Slug: `design-for-delegation-rather-than-direct-manipulation`

Design experiences around the assignment of work, the expression of intent, the setting of constraints, and the review of results, rather than requiring users to execute each step manually.

Cluster: delegation

Implications:

- Enable users to define goals, constraints, and preferences with precision.
- Make the scope of delegated authority explicit.
- Provide clear controls for initiation, pause, redirection, and termination of work.
- Treat prompt input as one mechanism among several, not as the entire experience model.

### 2. Ensure that background work remains perceptible

Slug: `ensure-that-background-work-remains-perceptible`

When the system is operating asynchronously or outside the user’s immediate focus, it should provide persistent and proportionate signals that work is continuing.

Cluster: visibility

Implications:

- Provide lightweight but reliable status indicators.
- Use ambient progress signals instead of relying exclusively on blocking states.
- Enable users to leave and return without losing continuity.
- Preserve task state across sessions where relevant.

### 3. Align feedback with the user’s level of attention

Slug: `align-feedback-with-the-user-s-level-of-attention`

The system should calibrate the depth and frequency of feedback according to whether the user is actively engaged, passively monitoring, or temporarily absent.

Cluster: visibility

Implications:

- Support both foreground and background modes of engagement.
- Reduce unnecessary operational noise for routine work.
- Increase detail where risk, uncertainty, or required intervention rises.
- Escalate clearly when user attention is materially required.

### 4. Apply progressive disclosure to system agency

Slug: `apply-progressive-disclosure-to-system-agency`

Provide the minimum information necessary by default, while enabling users to inspect additional detail when confidence, understanding, or intervention is required.

Cluster: trust

Implications:

- Prioritise intent, status, and outcome in the primary view.
- Allow expansion into actions taken, supporting evidence, decision logic, or tool usage.
- Present explanation at an appropriate level of abstraction.
- Distinguish clearly between summary information and detailed inspection.

### 5. Replace implied magic with clear mental models

Slug: `replace-implied-magic-with-clear-mental-models`

The product should help users understand what the system can do, what it is currently doing, what it cannot do, and what conditions govern its behaviour.

Cluster: delegation

Implications:

- Describe capabilities in plain and specific terms.
- Distinguish between suggestion, execution, and automation.
- Make permissions, dependencies, and limitations explicit.
- Indicate when action requires approval and when it proceeds independently.

### 6. Expose meaningful operational state, not internal complexity

Slug: `expose-meaningful-operational-state-not-internal-complexity`

Present the state of the system in language and structures that are relevant to the user, rather than exposing low-level internals that do not support action or understanding.

Cluster: visibility

Implications:

- Use states such as active, queued, blocked, awaiting approval, complete, or failed.
- Communicate dependencies when they affect progress or outcome.
- Describe activity in user-relevant terms.
- Reserve deeper technical detail for specialist or diagnostic views where appropriate.

### 7. Establish trust through inspectability

Slug: `establish-trust-through-inspectability`

Users should be able to examine how a result was produced when confidence, accountability, or decision quality is important.

Cluster: trust

Implications:

- Make source material traceable.
- Provide visibility into actions taken and decisions reached.
- Support comparison between recommendation and result, or between draft and final output.
- Maintain appropriate task history or auditability where needed.

### 8. Make hand-offs, approvals, and blockers explicit

Slug: `make-hand-offs-approvals-and-blockers-explicit`

When the system cannot proceed, the reason should be immediately visible, along with any action required from the user or another dependency.

Cluster: trust

Implications:

- Surface waiting states clearly.
- Explain whether the dependency is user action, system access, policy constraint, or tool failure.
- Make required actions specific and minimal.
- Distinguish between interruption, failure, and approval gating.

### 9. Represent delegated work as a system, not merely as a conversation

Slug: `represent-delegated-work-as-a-system-not-merely-as-a-conversation`

Where work involves multiple steps, agents, dependencies, or concurrent activities, it should be represented as a structured system rather than solely as a message stream.

Cluster: orchestration

Implications:

- Use task views, status layers, timelines, maps, boards, or orchestration frameworks where appropriate.
- Separate conversational exchange from execution state.
- Show dependencies and relationships across subtasks.
- Make concurrent activity understandable at a glance.

### 10. Optimise for steering, not only initiating

Slug: `optimise-for-steering-not-only-initiating`

The system should support users not only in starting tasks, but also in guiding, refining, reprioritising, and correcting work while it is underway.

Cluster: delegation

Implications:

- Support intervention mid-process.
- Allow constraints and priorities to be updated dynamically.
- Preserve continuity when the direction of work changes.
- Treat the user as an active governor of execution, not only as an originator of requests.

## Example Summaries

### Level 1: Augmented LLM — Single API Call

- Slug: `agents-agent-complexity-1-augmented-llm`
- Difficulty: advanced
- Libraries: pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Level 1: Augmented LLM — Single API Call One model call with structured output, system prompt, and context. No loops, no tools.

### Level 2: Prompt Chains & Routing — Deterministic DAGs

- Slug: `agents-agent-complexity-2-prompt-chains`
- Difficulty: advanced
- Libraries: pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Level 2: Prompt Chains & Routing — Deterministic DAGs Multiple LLM calls in a fixed sequence. Code controls the flow, not the model.

### Level 3: Tool-Calling Agent — Scoped Autonomy

- Slug: `agents-agent-complexity-3-tool-calling-agent`
- Difficulty: advanced
- Libraries: pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Level 3: Tool-Calling Agent — Scoped Autonomy The agent decides which tools to call and in what order, but only within a fixed set of well-defined capabilities.

### Level 4: Agent Harness — Full Runtime Access

- Slug: `agents-agent-complexity-4-agent-harness`
- Difficulty: advanced
- Libraries: pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Level 4: Agent Harness — Full Runtime Access Give the agent a full runtime via the agent runtime SDK. It can search files, read docs, and reason through problems autonomously.

### Level 5: Multi-Agent Orchestration — Delegated Autonomy

- Slug: `agents-agent-complexity-5-multi-agent`
- Difficulty: advanced
- Libraries: pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Level 5: Multi-Agent Orchestration — Delegated Autonomy An orchestrator delegates to specialized subagents defined via the agent runtime SDK. Each subagent has its own prompt, tools, and model. The orchestrator coordinates.

### Intelligence: The "brain" that processes information and makes decisions using LLMs.

- Slug: `agents-building-blocks-1-intelligence`
- Difficulty: intermediate
- Libraries: openai, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Intelligence: The "brain" that processes information and makes decisions using LLMs. This component handles context understanding, instruction following, and response generation.

### Memory: Stores and retrieves relevant information across interactions.

- Slug: `agents-building-blocks-2-memory`
- Difficulty: intermediate
- Libraries: openai, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Memory: Stores and retrieves relevant information across interactions. This component maintains conversation history and context to enable coherent multi-turn interactions.

### Tools: Enables agents to execute specific actions in external systems.

- Slug: `agents-building-blocks-3-tools`
- Difficulty: intermediate
- Libraries: openai, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Tools: Enables agents to execute specific actions in external systems. This component provides the capability to make API calls, database updates, file operations, and other practical actions.

### Validation: Ensures LLM outputs match predefined data schemas.

- Slug: `agents-building-blocks-4-validation`
- Difficulty: intermediate
- Libraries: openai, pydantic, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Validation: Ensures LLM outputs match predefined data schemas. This component provides schema validation and structured data parsing to guarantee consistent data formats for downstream code.

### Control: Provides deterministic decision-making and process flow control.

- Slug: `agents-building-blocks-5-control`
- Difficulty: intermediate
- Libraries: openai, pydantic, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Control: Provides deterministic decision-making and process flow control. This component handles if/then logic, routing based on conditions, and process orchestration for predictable behavior.

### Recovery: Manages failures and exceptions gracefully in agent workflows.

- Slug: `agents-building-blocks-6-recovery`
- Difficulty: intermediate
- Libraries: openai, pydantic, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Recovery: Manages failures and exceptions gracefully in agent workflows. This component implements retry logic, fallback processes, and error handling to ensure system resilience.

### Feedback: Provides strategic points where human judgement is required.

- Slug: `agents-building-blocks-7-feedback`
- Difficulty: intermediate
- Libraries: openai, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Feedback: Provides strategic points where human judgement is required. This component implements approval workflows and human-in-the-loop processes for high-risk decisions or complex judgments.

### Get Single Page

- Slug: `context-web-1-get-single-page`
- Difficulty: intermediate
- Libraries: docling, openai, pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from docling.document_converter import DocumentConverter from openai import OpenAI from pydantic import BaseModel, HttpUrl client = OpenAI() converter = DocumentConverter() MODEL = "gpt-4.1-nano" # -------------------------------------------------------------- # Define the output

### Web Search

- Slug: `context-web-2-web-search`
- Difficulty: intermediate
- Libraries: docling, openai, pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from typing import List from openai import OpenAI from pydantic import BaseModel client = OpenAI() MODEL = "gpt-5-nano" # use a reasoning model for better performance # -------------------------------------------------------------- # Define the output model # --------------------

### Search Handbook

- Slug: `context-web-3-search-handbook`
- Difficulty: intermediate
- Libraries: docling, openai, pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: 

### Search Agent

- Slug: `context-web-4-search-agent`
- Difficulty: intermediate
- Libraries: docling, openai, pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import json from openai import OpenAI from tools import ( AgentAnswer, get_handbook_tool, get_web_page, get_web_page_tool, get_web_search_tool, search_handbook, ) MODEL = "gpt-4.1" client = OpenAI() SYSTEM_PROMPT = You are a research assistant for Dutch government organizations. 

### Interactive Agent

- Slug: `context-web-5-interactive-agent`
- Difficulty: intermediate
- Libraries: docling, openai, pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from tools import SearchAgent def main(): Run interactive terminal agent. agent = SearchAgent() print("=" * 70) print("Research Assistant for Dutch Government Organizations") print("=" * 70) print("\nType 'quit' or 'exit' to end the conversation.") print("Type 'reset' to clear co

### Agent

- Slug: `context-web-tools-agent`
- Difficulty: intermediate
- Libraries: openai, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import json import os from typing import List from openai import OpenAI from dotenv import load_dotenv from .get_web_page import get_web_page, get_tool_definition as get_web_page_tool from .models import AgentAnswer from .search_handbook import search_handbook, get_tool_definitio

### Get Web Page

- Slug: `context-web-tools-get-web-page`
- Difficulty: intermediate
- Libraries: docling
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from docling.document_converter import DocumentConverter converter = DocumentConverter() def get_web_page(url: str) -> str: Fetch and convert a web page to markdown. page_content = converter.convert(url) return page_content.document.export_to_markdown() def get_tool_definition():

### Models

- Slug: `context-web-tools-models`
- Difficulty: intermediate
- Libraries: pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from typing import List from pydantic import BaseModel class Citation(BaseModel): text: str url: str = None section: str = None class AgentAnswer(BaseModel): answer: str citations: List[Citation]

### Search Handbook

- Slug: `context-web-tools-search-handbook`
- Difficulty: intermediate
- Libraries: none
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from pathlib import Path HANDBOOK_PATH = Path(__file__).parent.parent / "data" / "handbook.md" def search_handbook(query: str) -> str: Retrieve the handbook content for the agent to interpret. Note: The query parameter is accepted but not used - we return the full handbook. This 

### Web Search

- Slug: `context-web-tools-web-search`
- Difficulty: intermediate
- Libraries: none
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: def get_tool_definition(allowed_domains: list = None): Get web search tool definition for responses API. tool = { "type": "web_search", } if allowed_domains: tool["filters"] = {"allowed_domains": allowed_domains} return tool

### Tutorial: Notebook to Web App in Five Minutes

- Slug: `frameworks-notebooks-1-introduction-1-notebook-to-web-app`
- Difficulty: beginner
- Libraries: gradio, streamlit
- Version: 1baa9d2a5f2d
- Last updated: 2026-03-21T10:51:24Z
- Summary: This notebook shows how to turn a small Python function into a shareable interface with Gradio or Streamlit. It focuses on one clear input -> processing -> output flow so the app wrapper stays explicit and easy to review.

### Quickstart

- Slug: `frameworks-pydantic-ai-2-getting-started-quickstart`
- Difficulty: beginner
- Libraries: pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from typing import Literal from pydantic_ai import Agent from pydantic_ai.models.openai import OpenAIChatModel from pydantic import BaseModel import nest_asyncio nest_asyncio.apply() # Needed to run interactive python # ------------------------------------------------------------

### Agents

- Slug: `frameworks-pydantic-ai-3-core-concepts-1-agents`
- Difficulty: intermediate
- Libraries: none
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from datetime import date import json import nest_asyncio from pydantic_ai import Agent nest_asyncio.apply() # -------------------------------------------------------------- # Static instructions - defined at agent creation # ------------------------------------------------------

### Dependencies

- Slug: `frameworks-pydantic-ai-3-core-concepts-2-dependencies`
- Difficulty: intermediate
- Libraries: pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from datetime import date import json from typing import Literal import nest_asyncio from pydantic import BaseModel from pydantic_ai import Agent, RunContext nest_asyncio.apply() # -------------------------------------------------------------- # Without dependencies - limited con

### Tools

- Slug: `frameworks-pydantic-ai-3-core-concepts-3-tools`
- Difficulty: intermediate
- Libraries: pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import json import nest_asyncio from pydantic import BaseModel from pydantic_ai import Agent, RunContext from youtube_transcript_api import YouTubeTranscriptApi from utils.youtube import extract_video_id nest_asyncio.apply() class Transcript(BaseModel): video_id: str language: st

### Output

- Slug: `frameworks-pydantic-ai-3-core-concepts-4-output`
- Difficulty: intermediate
- Libraries: pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import nest_asyncio from pydantic import BaseModel from pydantic_ai import Agent, RunContext, ModelResponse nest_asyncio.apply() # -------------------------------------------------------------- # Basic output # -------------------------------------------------------------- class 

### Messages

- Slug: `frameworks-pydantic-ai-3-core-concepts-5-messages`
- Difficulty: intermediate
- Libraries: none
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import json import nest_asyncio from pydantic_ai import Agent, ModelMessage nest_asyncio.apply() # -------------------------------------------------------------- # Accessing messages from results # -------------------------------------------------------------- agent = Agent("open

### Direct

- Slug: `frameworks-pydantic-ai-3-core-concepts-6-direct`
- Difficulty: intermediate
- Libraries: none
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: 

### Tool Requires Approval

- Slug: `frameworks-pydantic-ai-5-tools-and-toolsets-human-in-the-loop-1-tool-requires-approval`
- Difficulty: intermediate
- Libraries: python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: { "cells": [ { "cell_type": "code", "execution_count": 1, "id": "0cba1839", "metadata": {}, "outputs": [], "source": [ "from pydantic_ai import (\n", " Agent,\n", " ApprovalRequired,\n", " DeferredToolRequests,\n", " DeferredToolResults,\n", " RunContext,\n", " ToolDenied,\n", ")

### Banking Assisant

- Slug: `frameworks-pydantic-ai-5-tools-and-toolsets-human-in-the-loop-2-banking-assisant`
- Difficulty: intermediate
- Libraries: pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import nest_asyncio from dataclasses import dataclass from typing import Union from pydantic import BaseModel from rich.console import Console from rich.panel import Panel from rich.prompt import Confirm from pydantic_ai import Agent, RunContext, ToolDenied from pydantic_ai.messa

### Extraction

- Slug: `knowledge-docling-1-extraction`
- Difficulty: intermediate
- Libraries: docling, ipykernel, lancedb, openai, pydantic, python-dotenv, requests, streamlit, tiktoken
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from docling.document_converter import DocumentConverter from utils.sitemap import get_sitemap_urls converter = DocumentConverter() # -------------------------------------------------------------- # Basic PDF extraction # ----------------------------------------------------------

### Chunking

- Slug: `knowledge-docling-2-chunking`
- Difficulty: intermediate
- Libraries: docling, ipykernel, lancedb, openai, pydantic, python-dotenv, requests, streamlit, tiktoken
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from docling.chunking import HybridChunker from docling.document_converter import DocumentConverter from dotenv import load_dotenv from openai import OpenAI from utils.tokenizer import OpenAITokenizerWrapper load_dotenv() # Initialize OpenAI client (make sure you have OPENAI_API_

### Embedding

- Slug: `knowledge-docling-3-embedding`
- Difficulty: intermediate
- Libraries: docling, ipykernel, lancedb, openai, pydantic, python-dotenv, requests, streamlit, tiktoken
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from typing import List import lancedb from docling.chunking import HybridChunker from docling.document_converter import DocumentConverter from dotenv import load_dotenv from lancedb.embeddings import get_registry from lancedb.pydantic import LanceModel, Vector from openai import

### Search

- Slug: `knowledge-docling-4-search`
- Difficulty: intermediate
- Libraries: docling, ipykernel, lancedb, openai, pydantic, python-dotenv, requests, streamlit, tiktoken
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import lancedb # -------------------------------------------------------------- # Connect to the database # -------------------------------------------------------------- uri = "data/lancedb" db = lancedb.connect(uri) # ------------------------------------------------------------

### Chat

- Slug: `knowledge-docling-5-chat`
- Difficulty: intermediate
- Libraries: docling, ipykernel, lancedb, openai, pydantic, python-dotenv, requests, streamlit, tiktoken
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import streamlit as st import lancedb from openai import OpenAI from dotenv import load_dotenv # Load environment variables load_dotenv() # Initialize OpenAI client client = OpenAI() # Initialize LanceDB connection .cache_resource def init_db(): Initialize database connection. Re

### Mem0 Cloud Quickstart

- Slug: `knowledge-mem0-01-mem0-cloud-quickstart`
- Difficulty: beginner
- Libraries: mem0, mem0ai, openai, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from mem0 import MemoryClient from dotenv import load_dotenv import os load_dotenv(".env") # -------------------------------------------------------------- # Initialize Mem0 client (Cloud) # -------------------------------------------------------------- client = MemoryClient(api_

### Mem0 Oss Quickstart

- Slug: `knowledge-mem0-02-mem0-oss-quickstart`
- Difficulty: beginner
- Libraries: mem0, mem0ai, openai, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from mem0 import Memory from dotenv import load_dotenv load_dotenv(".env") m = Memory() # Requires OpenAI API key # -------------------------------------------------------------- # Message sequence # -------------------------------------------------------------- messages = [ { "r

### Email Example

- Slug: `knowledge-mem0-cloud-email-example`
- Difficulty: intermediate
- Libraries: mem0, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from mem0 import MemoryClient from email.parser import Parser from dotenv import load_dotenv load_dotenv("../.env") # Initialize Mem0 client client = MemoryClient() class EmailProcessor: def __init__(self): Initialize the Email Processor with Mem0 memory client self.client = clie

### Config

- Slug: `knowledge-mem0-oss-config`
- Difficulty: intermediate
- Libraries: none
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: config = { "vector_store": { "provider": "qdrant", "config": {"host": "localhost", "port": 6333}, }, "llm": { "provider": "openai", "config": {"api_key": "your-api-key", "model": "gpt-4"}, }, "embedder": { "provider": "openai", "config": {"api_key": "your-api-key", "model": "text

### Memory Demo

- Slug: `knowledge-mem0-oss-memory-demo`
- Difficulty: intermediate
- Libraries: mem0, openai, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI from mem0 import Memory from dotenv import load_dotenv load_dotenv("../.env") config = { "vector_store": { "provider": "qdrant", "config": {"host": "localhost", "port": 6333}, }, } openai_client = OpenAI() memory = Memory.from_config(config) def chat_wit

### Support Agent

- Slug: `knowledge-mem0-oss-support-agent`
- Difficulty: intermediate
- Libraries: mem0, openai, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI from mem0 import Memory from dotenv import load_dotenv load_dotenv("../.env") class CustomerSupportAIAgent: def __init__(self): Initialize the CustomerSupportAIAgent with memory configuration and OpenAI client. # ! Make sure qdrant is running (see docker

### Client Sse

- Slug: `mcp-crash-course-3-simple-server-setup-client-sse`
- Difficulty: advanced
- Libraries: mcp
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import asyncio import nest_asyncio from mcp import ClientSession from mcp.client.sse import sse_client nest_asyncio.apply() # Needed to run interactive python Make sure: 1. The server is running before running this script. 2. The server is configured to use SSE transport. 3. The 

### Client Stdio

- Slug: `mcp-crash-course-3-simple-server-setup-client-stdio`
- Difficulty: advanced
- Libraries: mcp
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import asyncio import nest_asyncio from mcp import ClientSession, StdioServerParameters from mcp.client.stdio import stdio_client nest_asyncio.apply() # Needed to run interactive python async def main(): # Define server parameters server_params = StdioServerParameters( command="p

### Client Streamable Http

- Slug: `mcp-crash-course-3-simple-server-setup-client-streamable-http`
- Difficulty: advanced
- Libraries: mcp
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import asyncio import nest_asyncio from mcp import ClientSession from mcp.client.streamable_http import streamablehttp_client nest_asyncio.apply() # Needed to run interactive python Make sure: 1. The server is running before running this script. 2. The server is configured to use

### Server

- Slug: `mcp-crash-course-3-simple-server-setup-server`
- Difficulty: advanced
- Libraries: mcp, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from mcp.server.fastmcp import FastMCP from dotenv import load_dotenv load_dotenv("../.env") # Create an MCP server mcp = FastMCP( name="Calculator", host="0.0.0.0", # only used for SSE transport (localhost) port=8050, # only used for SSE transport (set this to any port) stateles

### Client Simple

- Slug: `mcp-crash-course-4-openai-integration-client-simple`
- Difficulty: advanced
- Libraries: mcp, openai, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import asyncio import json from contextlib import AsyncExitStack from typing import Any, Dict, List import nest_asyncio from dotenv import load_dotenv from mcp import ClientSession, StdioServerParameters from mcp.client.stdio import stdio_client from openai import AsyncOpenAI # A

### Client

- Slug: `mcp-crash-course-4-openai-integration-client`
- Difficulty: advanced
- Libraries: mcp, openai, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import asyncio import json from contextlib import AsyncExitStack from typing import Any, Dict, List, Optional import nest_asyncio from dotenv import load_dotenv from mcp import ClientSession, StdioServerParameters from mcp.client.stdio import stdio_client from openai import Async

### Server

- Slug: `mcp-crash-course-4-openai-integration-server`
- Difficulty: advanced
- Libraries: mcp
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import os import json from mcp.server.fastmcp import FastMCP # Create an MCP server mcp = FastMCP( name="Knowledge Base", host="0.0.0.0", # only used for SSE transport (localhost) port=8050, # only used for SSE transport (set this to any port) ) .tool() def get_knowledge_base() -

### Function Calling

- Slug: `mcp-crash-course-5-mcp-vs-function-calling-function-calling`
- Difficulty: advanced
- Libraries: openai, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import json import openai from dotenv import load_dotenv from tools import add load_dotenv("../.env") This is a simple example to demonstrate that MCP simply enables a new way to call functions. # Define tools for the model tools = [ { "type": "function", "function": { "name": "a

### Tools

- Slug: `mcp-crash-course-5-mcp-vs-function-calling-tools`
- Difficulty: advanced
- Libraries: none
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: def add(a: int, b: int) -> int: Add two numbers together return a + b

### Client

- Slug: `mcp-crash-course-6-run-with-docker-client`
- Difficulty: advanced
- Libraries: mcp, mcp[cli]
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import asyncio import nest_asyncio from mcp import ClientSession from mcp.client.sse import sse_client nest_asyncio.apply() # Needed to run interactive python Make sure: 1. The server is running before running this script. 2. The server is configured to use SSE transport. 3. The 

### Server

- Slug: `mcp-crash-course-6-run-with-docker-server`
- Difficulty: advanced
- Libraries: mcp, mcp[cli], python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from mcp.server.fastmcp import FastMCP from dotenv import load_dotenv load_dotenv("../.env") # Create an MCP server mcp = FastMCP( name="Calculator", host="0.0.0.0", # only used for SSE transport port=8050, # only used for SSE transport (set this to any port) ) # Add a simple cal

### Server

- Slug: `mcp-servers-youtube-server`
- Difficulty: advanced
- Libraries: mcp
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: 

### Service

- Slug: `mcp-servers-youtube-src-service`
- Difficulty: advanced
- Libraries: requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import os from requests import Session from youtube_transcript_api import YouTubeTranscriptApi from youtube_transcript_api.formatters import ( TextFormatter, ) from youtube_transcript_api.proxies import WebshareProxyConfig from .utils import extract_video_id class YouTubeTranscri

### Test

- Slug: `mcp-servers-youtube-test`
- Difficulty: advanced
- Libraries: none
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from server import get_transcript t = get_transcript(") print(t)

### Introduction

- Slug: `models-openai-01-introduction-01-introduction`
- Difficulty: beginner
- Libraries: openai, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI from dotenv import load_dotenv import os load_dotenv() client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

### Making Requests

- Slug: `models-openai-01-introduction-02-making-requests`
- Difficulty: beginner
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI # The OpenAI class will automatically use the OPENAI_API_KEY environment variable client = OpenAI()

### Streaming

- Slug: `models-openai-01-introduction-03-streaming`
- Difficulty: beginner
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI client = OpenAI() stream = client.chat.completions.create( model="gpt-4", messages=[{"role": "user", "content": "Say this is a test"}], stream=True, ) for chunk in stream: if chunk.choices[0].delta.content is not None: print(chunk.choices[0].delta.conten

### Introduction

- Slug: `models-openai-04-structured-output-01-introduction`
- Difficulty: beginner
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI import json client = OpenAI() def send_reply(message: str): print(f"Sending reply: {message}") # -------------------------------------------------------------- # Unstructured output example # --------------------------------------------------------------

### Json Mode

- Slug: `models-openai-04-structured-output-02-json-mode`
- Difficulty: intermediate
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI import json client = OpenAI() def send_reply(message: str): print(f"Sending reply: {message}") # -------------------------------------------------------------- # Structured output example using response_format # ------------------------------------------

### Function Calling

- Slug: `models-openai-04-structured-output-03-function-calling`
- Difficulty: intermediate
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI import json client = OpenAI() def send_reply(message: str): print(f"Sending reply: {message}") # -------------------------------------------------------------- # Structured output example using function calling # -----------------------------------------

### Structured Output

- Slug: `models-openai-04-structured-output-04-structured-output`
- Difficulty: intermediate
- Libraries: openai, pydantic, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from enum import Enum import json import requests from bs4 import BeautifulSoup from openai import OpenAI from pydantic import BaseModel, Field client = OpenAI() MODEL = "gpt-4o-2024-08-06" query = Hi, I'm having trouble with my recent order. I received the wrong item and need to

### Instructor

- Slug: `models-openai-04-structured-output-instructor-01-instructor`
- Difficulty: intermediate
- Libraries: instructor, openai, pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import instructor from pydantic import BaseModel, Field from openai import OpenAI from enum import Enum def send_reply(message: str): print(f"Sending reply: {message}") # -------------------------------------------------------------- # Instructor structured output example # -----

### Output Validation

- Slug: `models-openai-04-structured-output-instructor-02-output-validation`
- Difficulty: intermediate
- Libraries: instructor, openai, pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import instructor from pydantic import BaseModel, Field from openai import OpenAI from enum import Enum # -------------------------------------------------------------- # Instructor Retry Example with Enum Category # -------------------------------------------------------------- 

### Content Filtering

- Slug: `models-openai-04-structured-output-instructor-03-content-filtering`
- Difficulty: intermediate
- Libraries: instructor, openai, pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import instructor from pydantic import BaseModel, Field from openai import OpenAI from pydantic import BeforeValidator from typing_extensions import Annotated from instructor import llm_validator def send_reply(message: str): print(f"Sending reply: {message}") # -----------------

### Ticket System

- Slug: `models-openai-04-structured-output-instructor-04-ticket-system`
- Difficulty: intermediate
- Libraries: instructor, openai, pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import instructor from pydantic import BaseModel, Field from openai import OpenAI from enum import Enum # -------------------------------------------------------------- # Ticket System Example with Structured Output # --------------------------------------------------------------

### Introduction

- Slug: `models-openai-05-responses-01-introduction`
- Difficulty: beginner
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI client = OpenAI() # -------------------------------------------------------------- # Basic text example with the Chat Completions API # -------------------------------------------------------------- response = client.chat.completions.create( model="gpt-4

### Text Prompting

- Slug: `models-openai-05-responses-02-text-prompting`
- Difficulty: intermediate
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI client = OpenAI() Model spec: Dashboard: # -------------------------------------------------------------- # Introducing instructions # -------------------------------------------------------------- Inputs can now be a single string or a list of messages.

### Conversation State

- Slug: `models-openai-05-responses-03-conversation-state`
- Difficulty: intermediate
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI client = OpenAI() # -------------------------------------------------------------- # Manual conversation state # -------------------------------------------------------------- response = client.responses.create( model="gpt-4o-mini", input=[ {"role": "use

### Function Calling

- Slug: `models-openai-05-responses-04-function-calling`
- Difficulty: intermediate
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI client = OpenAI() tools = [ { "type": "function", "name": "send_email", "description": "Send an email to a given recipient with a subject and message.", "parameters": { "type": "object", "properties": { "to": {"type": "string", "description": "The recipi

### Structured Output

- Slug: `models-openai-05-responses-05-structured-output`
- Difficulty: intermediate
- Libraries: openai, pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import json from typing import List from openai import OpenAI from pydantic import BaseModel client = OpenAI() # -------------------------------------------------------------- # Using a JSON Schema # -------------------------------------------------------------- response = client

### Web Search

- Slug: `models-openai-05-responses-06-web-search`
- Difficulty: intermediate
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI client = OpenAI() # -------------------------------------------------------------- # Basic web search # -------------------------------------------------------------- response = client.responses.create( model="gpt-4o", tools=[ { "type": "web_search_previ

### File Search

- Slug: `models-openai-05-responses-07-file-search`
- Difficulty: intermediate
- Libraries: openai, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import requests from io import BytesIO from openai import OpenAI import textwrap client = OpenAI() # -------------------------------------------------------------- # Upload a file # -------------------------------------------------------------- def create_file(client, file_path):

### Reasoning

- Slug: `models-openai-05-responses-08-reasoning`
- Difficulty: intermediate
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI client = OpenAI() prompt = Write a bash script that takes a matrix represented as a string with format '[1,2],[3,4],[5,6]' and prints the transpose in the same format. response = client.responses.create( model="o3-mini", reasoning={"effort": "medium"}, i

### Introduction

- Slug: `models-openai-06-agents-01-introduction`
- Difficulty: beginner
- Libraries: none
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from agents import Agent, Runner import nest_asyncio nest_asyncio.apply() agent = Agent(name="Assistant", instructions="You are a helpful assistant") result = Runner.run_sync(agent, "Write a haiku about recursion in programming.") print(result.final_output)

### Handoffs

- Slug: `models-openai-06-agents-02-handoffs`
- Difficulty: intermediate
- Libraries: none
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from agents import Agent, Runner import asyncio import nest_asyncio nest_asyncio.apply() tech_support_agent = Agent( name="Tech Support Agent", instructions="You handle technical issues with our product. Be concise and helpful.", ) billing_agent = Agent( name="Billing Agent", ins

### Gpt Oss

- Slug: `models-openai-07-gpt-oss-gpt-oss`
- Difficulty: intermediate
- Libraries: pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from pydantic import BaseModel from pydantic_ai import Agent from pydantic_ai.models.openai import OpenAIChatModel from pydantic_ai.providers.openai import OpenAIProvider import nest_asyncio nest_asyncio.apply() class CityLocation(BaseModel): city: str country: str ollama_model =

### Sora Quickstart

- Slug: `models-openai-08-video-1-sora-quickstart`
- Difficulty: beginner
- Libraries: openai, pillow, pydantic, python-dotenv, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import sys import time from openai import OpenAI openai = OpenAI() # -------------------------------------------------------------- # Create a new video # -------------------------------------------------------------- # Takes about 2 minutes video = openai.videos.create( model="s

### References

- Slug: `models-openai-08-video-2-references`
- Difficulty: intermediate
- Libraries: openai, pillow, pydantic, python-dotenv, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import time from openai import OpenAI from pathlib import Path import base64 from utils.resizer import resize_image from utils.downloader import download_sora_video openai = OpenAI() # -------------------------------------------------------------- # Generate a reference image # -

### Sora Pro Model

- Slug: `models-openai-08-video-3-sora-pro-model`
- Difficulty: intermediate
- Libraries: openai, pillow, pydantic, python-dotenv, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI from utils.downloader import download_sora_video openai = OpenAI() # -------------------------------------------------------------- # Generate a video with Sora Pro mode # -------------------------------------------------------------- # Stays stuck in pr

### Sora Prompting

- Slug: `models-openai-08-video-4-sora-prompting`
- Difficulty: intermediate
- Libraries: openai, pillow, pydantic, python-dotenv, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from utils.director import SoraDirector from utils.downloader import download_sora_video from openai import OpenAI openai = OpenAI() director = SoraDirector() # -------------------------------------------------------------- # Generate a Sora prompt # -----------------------------

### Sora Remix

- Slug: `models-openai-08-video-5-sora-remix`
- Difficulty: intermediate
- Libraries: openai, pillow, pydantic, python-dotenv, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import os from datetime import datetime from openai import OpenAI from utils.downloader import download_sora_video openai = OpenAI() # Character description for consistency CHARACTER = ( "A 30-year-old male programmer with short dark hair, beard, wearing a black t-shirt" ) shots 

### Sora Sequence

- Slug: `models-openai-08-video-6-sora-sequence`
- Difficulty: intermediate
- Libraries: openai, pillow, pydantic, python-dotenv, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import os import subprocess import tempfile import sys from pathlib import Path # -------------------------------------------------------------- # Find most recent sequence folder or use provided path # -------------------------------------------------------------- # Check if a v

### Web Search

- Slug: `models-openai-09-web-web-search`
- Difficulty: intermediate
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from openai import OpenAI client = OpenAI() response = client.responses.create( model="gpt-5-mini", reasoning={"effort": "low"}, tools=[ { "type": "web_search", "filters": { "allowed_domains": [ "pubmed.ncbi.nlm.nih.gov", "clinicaltrials.gov", " " " ] }, } ], tool_choice="auto", 

### Human-in-the-Loop: Structured Output with Router

- Slug: `models-openai-10-human-in-the-loop-1-structured-output`
- Difficulty: intermediate
- Libraries: openai, pydantic, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Human-in-the-Loop: Structured Output with Router

### Human-in-the-Loop: Tool Call Approval

- Slug: `models-openai-10-human-in-the-loop-2-tool-call-approval`
- Difficulty: intermediate
- Libraries: openai, python-dotenv
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: Human-in-the-Loop: Tool Call Approval

### Basic

- Slug: `workflows-1-introduction-1-basic`
- Difficulty: beginner
- Libraries: openai
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import os from openai import OpenAI client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) completion = client.chat.completions.create( model="gpt-4o", messages=[ {"role": "system", "content": "You're a helpful assistant."}, { "role": "user", "content": "Write a limerick about the 

### Structured

- Slug: `workflows-1-introduction-2-structured`
- Difficulty: beginner
- Libraries: openai, pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import os from openai import OpenAI from pydantic import BaseModel client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # -------------------------------------------------------------- # Step 1: Define the response format in a Pydantic model # ------------------------------------

### Tools

- Slug: `workflows-1-introduction-3-tools`
- Difficulty: beginner
- Libraries: openai, pydantic, requests
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import json import os import requests from openai import OpenAI from pydantic import BaseModel, Field client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) docs: # -------------------------------------------------------------- # Define the tool (function) that we want to call # --

### Retrieval

- Slug: `workflows-1-introduction-4-retrieval`
- Difficulty: beginner
- Libraries: openai, pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import json import os from openai import OpenAI from pydantic import BaseModel, Field client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) docs: # -------------------------------------------------------------- # Define the knowledge base retrieval tool # -------------------------

### Prompt Chaining

- Slug: `workflows-2-workflow-patterns-1-prompt-chaining`
- Difficulty: intermediate
- Libraries: openai, pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from typing import Optional from datetime import datetime from pydantic import BaseModel, Field from openai import OpenAI import os import logging # Set up logging configuration logging.basicConfig( level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="

### Routing

- Slug: `workflows-2-workflow-patterns-2-routing`
- Difficulty: intermediate
- Libraries: openai, pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from typing import Optional, Literal from pydantic import BaseModel, Field from openai import OpenAI import os import logging # Set up logging configuration logging.basicConfig( level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", )

### Parallizaton

- Slug: `workflows-2-workflow-patterns-3-parallizaton`
- Difficulty: intermediate
- Libraries: openai, pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: import asyncio import logging import os import nest_asyncio from openai import AsyncOpenAI from pydantic import BaseModel, Field nest_asyncio.apply() # Set up logging configuration logging.basicConfig( level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefm

### Orchestrator

- Slug: `workflows-2-workflow-patterns-4-orchestrator`
- Difficulty: intermediate
- Libraries: openai, pydantic
- Version: 5fd90f57f8a1
- Last updated: 2026-03-14T14:44:14Z
- Summary: from typing import List, Dict from pydantic import BaseModel, Field from openai import OpenAI import os import logging # Set up logging configuration logging.basicConfig( level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", ) logger

## Application Guides

### AI Agent Security Design — AI Design Blueprint

- Slug: `security-application`
- Principles: 4, 7, 8, 10
- Summary: A Blueprint guide to securing AI agents with inspectable traces, progressive disclosure, and approval gates against poisoned memory, experience grafting, and adversarial prompts.

### Observable Agent Evaluation — AI Design Blueprint

- Slug: `observable-evaluation`
- Principles: 6, 7, 8, 9
- Summary: Evaluate production AI agents with structured traces, three-tier metrics, and inspectable review states so your team can see what executed, why it failed, and when to intervene.

### Human-in-the-loop governance — AI Design Blueprint

- Slug: `beyond-human-in-the-loop`
- Principles: 8, 10, 7, 1
- Summary: Design human-in-the-loop governance for high-stakes AI agents with explicit escalation tiers, intervention points, override paths, and inspectable delegation boundaries.

### WebMCP Approval Boundaries — AI Design Blueprint

- Slug: `webmcp-action-surfaces-approval-boundaries`
- Principles: 1, 7, 8, 9
- Summary: Design WebMCP website actions as explicit transactions with visible state, inspectable outputs, and approval tiers instead of opaque browser automation.

### Computer-use agents

- Slug: `computer-use-agents`
- Principles: 4, 5, 8
- Summary: Design computer-use agents as inspectable delegated workflows with visible state, explicit blockers, and approval boundaries instead of opaque screen-driving chat.

### Parallel Agent Sessions — AI Design Blueprint

- Slug: `parallel-agent-sessions-shared-state-conflict-resolution`
- Principles: 6, 8, 9, 10
- Summary: Coordinate multiple agent sessions with explicit scope ownership, shared run boards, visible blockers, and conflict tiers so concurrent work stays safe, inspectable, and steerable.

### Agent review operations — AI Design Blueprint

- Slug: `agent-review-operations`
- Principles: 7, 8, 9, 10
- Summary: Blueprint shows how to run agent review operations with comment-to-change workflows, SLAs, and escalation tiers that scale across teams without approval bottlenecks.

### Background Work Visibility — AI Design Blueprint

- Slug: `background-work-visibility`
- Principles: 2, 3, 6, 8
- Summary: Design agents so background execution stays perceptible through persistent progress signals, async state views, and explicit blockers instead of silent polling-only updates.

### Long-Running Agent Recovery — AI Design Blueprint

- Slug: `long-running-agent-recovery-design`
- Principles: 2, 8, 9, 10
- Summary: Build long-running agents that checkpoint work, expose failure states, preserve partial completion, and recover through explicit human-visible paths instead of silent retries.

### Steering Without Restarting — AI Design Blueprint

- Slug: `steering-without-restarting`
- Principles: 2, 7, 9, 10
- Summary: Design agent workflows so users can redirect work mid-task, preserve context, and correct course without restarting from scratch.
