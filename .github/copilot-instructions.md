## Project Overview

- This repository is a static Computer Science course portal for Mergington High School.
- Keep the project framework-free. Use the existing HTML, CSS, browser JavaScript, JSON, Markdown, and Python structure.
- Do not add a package manager, bundler, server, or external dependency unless the user explicitly requests it.
- Preserve the existing folder structure and use relative paths that work when the site is served from the repository root.

## Web Code Standards

- Use two spaces for indentation in HTML, CSS, and JavaScript.
- Use semicolons in JavaScript and double quotes for JavaScript strings unless a template literal is needed.
- Use `camelCase` for JavaScript variables, methods, and properties. Use PascalCase for JavaScript classes.
- Prefer `const` and `let`; do not introduce `var`.
- Keep browser behavior in the appropriate file under `assets/js/`. Reuse the existing class-based page controllers and initialize them on `DOMContentLoaded`.
- Use `textContent` for plain text. Only assign to `innerHTML` when rendering trusted, repository-controlled markup or when the existing Markdown flow requires it.
- Handle failed `fetch` requests and missing data with clear user-facing error states and useful `console.error` messages.
- Read course and assignment metadata from `config.json`; do not duplicate assignment data in page scripts.
- Keep links and asset paths relative to the page that uses them. Check path depth when editing files under `assets/pages/`.

## HTML and CSS

- Preserve semantic HTML, valid document structure, `lang="en"`, responsive viewport metadata, and meaningful image `alt` text.
- Reuse existing class names and CSS custom properties before adding new styles.
- Keep styles in `assets/css/styles.css`; avoid inline styles except where the existing dynamic display behavior requires them.
- Maintain responsive layouts for desktop and mobile widths. Do not rely on hover as the only way to access information or controls.
- Keep visual changes consistent with the existing school portal design: blue-gray primary colors, clear assignment status, readable contrast, and restrained motion.
- Respect `prefers-reduced-motion` when adding animations.

## Python Assignment Materials

- Use four spaces for Python indentation and follow standard `snake_case` naming for functions and variables.
- Keep starter code beginner-friendly and limited to the concepts described by the assignment.
- Do not remove task comments or required function names from starter files unless the assignment itself changes.
- Keep each assignment's `README.md`, `starter-code.py`, and supporting data files synchronized with its entry in `config.json`.
- Use Markdown headings, concise requirements, examples, and fenced code blocks in assignment instructions.

## Change and Validation Guidelines

- Make the smallest change that satisfies the request and preserve unrelated user changes.
- Before finishing, verify JSON parses correctly and inspect changed relative links when applicable.
- For JavaScript or UI changes, serve the repository from its root with a simple local static server and test both the main page and an assignment page in a browser.
- For Python changes, run the affected starter file or a focused syntax check when execution is not appropriate.
- There is no configured build or test suite; do not invent one for small changes. Report any validation that could not be run.
