# LLM School

Guides to teach LLMs the necessary skills for effective software development. Highly opinionated work in progress.

> [!NOTE]
> The best way to use LLM School is to fork this repository and customize it for yourself.

Includes main prompts, agent definitions and guides that are read on-demand with automatic triggering conditions. Similar to the skills system, but focused on learning rather using external tooling.


## Installation

Render templates and install for one or more AI coding assistants using the `install` script:

```bash
uv run --script install.py [flags] 
```

Pass `--claude`, `--qwen` and/or `--opencode`.

> [!NOTE]
> When replacing files, a backup will be saved to `<config>/backup` under the same relative path.

## Usage

There's nothing special to do. Guides are either embedded in the core instructions or include triggering conditions that make agents read them automatically.

You can explicitly instruct the AI to deploy agents or read specific guides during conversation, too. Use their filenames or topics.

### Agents

- **Architect** - High-level architectural decisions, planning roadmaps, and system design
- **Implementer** - Methodical execution of implementation roadmaps and architectural plans
- **Reviewer** - Code review and quality assessment before proceeding
- **Researcher** - Comprehensive research with verified sources and analytical insights

### Guides

- **Effective Communication** - Clear, concise communication
- **Effective Collaboration** - Working effectively with users
- **Design Philosophy** - Principles for good software design
- **Writing Code** - Writing clean, maintainable code
- **Writing Plans** - Creating effective implementation roadmaps
- **Executing Plans** - Implementing planned solutions
- **Following Plans** - Executing detailed implementation plans
- **Fixing Bugs** - Systematic bug diagnosis and resolution
- **Brainstorming** - Creative ideation and design exploration
- **Implementing Complex Features** - Building non-trivial functionality
- **Refactoring Code** - Improving code structure and quality
- **Reviewing Code** - Conducting thorough code reviews
- **Seeking Guidance** - Knowing when to ask for help
- **Test-driven Development** - Writing tests before implementation
- **Using Version Control** - Git best practices

