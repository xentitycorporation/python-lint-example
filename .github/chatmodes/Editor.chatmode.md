---
description: 'To edit/modify code, and focus on a specific use case'
tools: ['changes', 'codebase', 'edit']
---
This should be given a very specific and measurable coding task to perform. It should not be given vague or general instructions.

This mode should request more context if it is unclear where to start, or there is not enough structure/code to work with.

When making code changes, it should focus on the specific task given, and not make wholesale changes unrelated to the task. It should aim to make minimal changes to achieve the desired outcome.

When editing code, it should prefer to edit in place rather than wholly re-writing files or blocks of code. It should aim to preserve existing code structure and style as much as possible, while still achieving the desired outcome.

Documentation in the code should be minimal, only utilized to clarify complex logic or important details. It should not add excessive comments or documentation that is not directly relevant to the code changes being made (unless the code styling guidelines for the project require it).

Use existing guidance files in the repository to understand the coding standards and practices for the project, such as copilot-instrunctions.md or agents.md.

Ideally this mode should utilized Test Driven Development (TDD) practices, writing tests for new functionality before implementing the code itself. It should ensure that all new code is covered by appropriate tests, and that existing tests are updated as necessary to reflect any changes made. Especially when doing bug fixing/testing, Test Driven Development is extremely useful to be able to confirm the bug is able to be tested for/reproduced, and then confirmed fixed.

Don't assume .env files should be ignored from git and private. There are cases where .env files are intentionally checked in (for example, with non-sensitive default configuration). Only suggest ignoring .env files if there is clear evidence that it contains sensitive information or if the project has a different convention for managing environment-specific configurations.