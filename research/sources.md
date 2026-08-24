# Research Sources

Research checked on 24 August 2026.

Primary vendor documentation was used for product capabilities and configuration claims. Vendor documentation is treated as first-party evidence, not independent proof of security, reliability, compliance, or production readiness.

## OpenClaw

### Gateway Security
https://docs.openclaw.ai/gateway/security

Used for:
- OpenClaw trust-boundary model
- Gateway security guidance
- least-privilege recommendations
- security-audit guidance

### Tool Configuration
https://docs.openclaw.ai/gateway/config-tools

Used for:
- tool profiles
- `minimal` tool profile
- allow/deny policy behavior

### Sandboxing
https://docs.openclaw.ai/gateway/sandboxing

Used for:
- sandbox modes
- sandbox scope
- workspace access
- distinction between sandboxing and tool policy

### Security Audit Checks
https://docs.openclaw.ai/gateway/security/audit-checks

Used for:
- security-audit capabilities
- configuration and filesystem risk checks

### OpenClaw v2026.7.1 Release Notes
https://docs.openclaw.ai/releases/2026.7.1

Used for:
- GPT-5.6 compatibility
- Codex workflow changes
- authentication and Gateway reliability updates
- permission-policy reporting changes
- security-audit updates

## Anthropic — Claude Code

### Claude Code Overview
https://code.claude.com/docs/en/overview

Used for:
- supported surfaces: terminal, IDE, desktop, and web
- developer and repository workflows
- automation capabilities
- scheduled tasks

### Claude Code Security
https://code.claude.com/docs/en/security

Used for:
- permission-based architecture
- security safeguards
- prompt-injection considerations
- managed deployment/security controls

### Claude Code MCP
https://code.claude.com/docs/en/mcp

Used for:
- Model Context Protocol integrations
- connection to external tools and data sources

### Claude Code Routines
https://code.claude.com/docs/en/routines

Used for:
- recurring cloud routines
- scheduled automation
- API-triggered routines
- GitHub-event-triggered routines

## n8n

### n8n Documentation
https://docs.n8n.io/

Used for:
- workflow automation platform capabilities
- cloud and self-hosted deployment options
- application and API integrations

### Human-in-the-loop for AI Tool Calls
https://docs.n8n.io/advanced-ai/human-in-the-loop-tools/

Used for:
- approval steps for AI-agent tool calls
- human oversight before selected actions

### Security Audit
https://docs.n8n.io/hosting/securing/security-audit/

Used for:
- n8n instance security auditing
- credential, filesystem, node, database, and instance checks

### Workflow Executions
https://docs.n8n.io/workflows/executions/all-executions/

Used for:
- execution history
- execution status and review
- retrying and inspecting workflow runs

## OpenAI — ChatGPT Workspace Agents

### ChatGPT Workspace Agents for Enterprise and Business
https://help.openai.com/en/articles/20001143

Used for:
- repeatable workspace-agent workflows
- schedules
- API triggers
- apps and custom MCPs
- sharing and access controls
- agent write approvals and app constraints

### Apps in ChatGPT
https://help.openai.com/en/articles/11487775

Used for:
- connected apps
- external data and actions
- app capabilities and workspace integrations

### Admin Controls, Security, and Compliance in Apps
https://help.openai.com/en/articles/11509118

Used for:
- workspace app permissions
- read/action controls
- approval settings
- role and access governance

## Source Selection Policy

Primary product documentation was preferred over blogs, social-media posts, third-party tutorials, and marketing summaries.

Where a product vendor described its own security or reliability features, those statements were treated as vendor-supplied evidence.

No vendor documentation was treated as independent proof of:
- enterprise security
- regulatory compliance
- production readiness
- reliability at Elchai Group's scale
- suitability for confidential company data

Those conclusions would require additional technical testing, legal/privacy review, security assessment, and organisational due diligence.
