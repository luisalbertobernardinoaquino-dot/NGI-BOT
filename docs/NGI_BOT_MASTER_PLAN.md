# NGI-BOT Master Plan

This document defines the long-term vision, principles, experience goals, and
development roadmap for NGI-BOT. All future technical and product decisions
should remain aligned with these guidelines.

## 1. Project Vision

NGI-BOT is a Bible-based spiritual companion chatbot for NGI Iglesia Cristiana
Nueva Generación Internacional. Its purpose is to help users find biblical
guidance, reflection, and spiritual accompaniment based on their emotional
state or personal situation.

NGI-BOT should provide a welcoming path toward Scripture and thoughtful
reflection while remaining clear about its role as a digital support tool.

## 2. Core Principle

The Bible and approved church documents are the source of authority. AI, if
added later, must only support understanding, tone, organization, and user
experience. AI must never replace Scripture, pastoral care, or church
leadership.

Every future response engine, search feature, or AI-assisted capability must be
grounded in approved sources and designed to direct users toward trustworthy
biblical and pastoral guidance.

## 3. Cost Principle

The project must remain as economical as possible. Avoid paid APIs in the first
versions. Prefer local files, rule-based responses, SQLite, local search, and
open-source tools. Paid AI should be optional and only added later if demand
justifies it.

New infrastructure or third-party services should be evaluated according to
their recurring cost, operational complexity, portability, and ability to be
replaced. The application should continue providing useful core functionality
without depending on paid AI services.

## 4. User Experience Goal

The user should feel peace, trust, and spiritual support from the first screen.
The interface should feel like a quiet place of reflection, not a generic
chatbot.

Language, motion, spacing, colors, and interaction patterns should communicate
warmth and clarity without creating emotional pressure or overstating the
system's spiritual or pastoral role.

## 5. Visual Identity

Use white, soft blue, and subtle gold accents. Use smooth animations only when
they help create peace. Avoid distracting effects. Use the dove image as a
gentle spiritual symbol.

The visual system should prioritize:

- Calm, uncluttered layouts.
- Clear hierarchy and comfortable reading widths.
- Consistent color, spacing, typography, and interaction states.
- Subtle depth through restrained shadows and translucent surfaces.
- Accessible contrast and legible text on every supported screen size.

## 6. Interface Requirements

- Centered NGI logo and church name.
- Title: **NGI-BOT**.
- Subtitle: **"Este BOT te refiere citas bíblicas que son guía en tu proceso"**.
- Soft animated background using `fondo.png`.
- Animated dove using `ES.png`.
- Welcome card with close button and **Comenzar** button.
- ChatGPT-style conversation area.
- Modern message bubbles.
- Typing indicator: **"NGI-BOT está preparando una respuesta..."**.
- Responsive design for mobile and desktop.
- High readability and accessibility.

All interface features should work without requiring paid services or
third-party frontend dependencies.

## 7. Functional Roadmap

### Phase 1: Professional interface and spiritual user experience

Create a peaceful, accessible, responsive interface around the existing
rule-based chatbot while preserving current functionality.

### Phase 2: Local Bible engine using Reina-Valera content

Add an approved, legally usable Reina-Valera Bible dataset and a local module
for retrieving passages. Confirm edition, licensing, attribution, and church
approval before adding the content.

### Phase 3: Emotional classification without paid AI

Expand deterministic classification using curated vocabulary, normalization,
weighted rules, and transparent confidence handling.

### Phase 4: Prayer and reflection engine

Provide curated prayers, reflection prompts, and gentle next steps derived from
approved biblical and church materials.

### Phase 5: Local search and topic-based Bible retrieval

Implement local full-text and topic-based search over approved content. Keep
retrieval deterministic, inspectable, and independent of paid AI APIs.

### Phase 6: Anonymous analytics and statistics

Introduce privacy-conscious, aggregated statistics to understand feature use
and improve content. Avoid storing message text or personal information unless
there is a clearly approved need.

### Phase 7: Optional AI integration only when needed

Evaluate AI only when real usage demonstrates a justified need. Any integration
must be optional, cost-controlled, source-grounded, privacy-reviewed, and able
to fall back to the local system.

### Phase 8: Admin dashboard and user management

Add administration and user-management capabilities only after requirements,
roles, security controls, privacy responsibilities, and operational ownership
have been formally defined.

## 8. Architecture Roadmap

Future modules:

- **Bible Engine:** Stores, normalizes, searches, and retrieves approved Bible
  passages and metadata.
- **Emotion Engine:** Classifies emotional context through transparent local
  rules and future open-source techniques.
- **Prayer Engine:** Selects approved prayers and reflection prompts appropriate
  to a user's expressed situation.
- **Conversation Engine:** Coordinates conversation flow, context, response
  selection, and safe fallbacks.
- **Knowledge Engine:** Searches approved church documents and organizes local
  topic-based knowledge.
- **Analytics Engine:** Produces anonymous, aggregated product statistics with
  strict privacy boundaries.

These modules should remain loosely coupled so they can evolve independently.
The Flask application should coordinate them through clear local interfaces
rather than embedding domain logic directly in routes.

## 9. Privacy Principle

Avoid collecting sensitive personal data unless absolutely necessary. Prefer
anonymous or aggregated statistics. The system should support spiritual
accompaniment without exposing private user information.

Future data collection must have a defined purpose, minimal scope, retention
policy, access policy, and deletion process. Spiritual conversations should be
treated as potentially sensitive even when users do not provide identifying
information.

## 10. Current Development Rule

For now, do not add paid APIs, login, database, or RAG. Focus first on the
interface and the rule-based chatbot.

Until this rule is deliberately revised and approved:

- Preserve the current Flask backend and Render compatibility.
- Keep all existing chatbot responses working.
- Use local assets and deterministic response logic.
- Improve the user interface, accessibility, maintainability, and tests.
- Prepare clean extension points without implementing future roadmap phases
  prematurely.
