#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "jinja2==3.1.6",
#   "PyYAML==6.0.1"
# ]
# ///
import re
import yaml
import shutil
import argparse
import time
from glob import glob
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, TemplateNotFound, pass_context

# --------------------------------------------------------------------------------------------------

# Define roots:
home = Path.home()
here = Path(__file__).parent # home != here :(

qwen = Path(home, '.qwen')
claude = Path(home, '.claude')
opencode = Path(home, '.config/opencode')


# --------------------------------------------------------------------------------------------------

# Collect guides:
guides = {}
for path in here.glob('guides/*.md'):
    _, frontmatter, content = path.read_text().split('---\n', 2)

    guide = yaml.safe_load(frontmatter)
    guide['name'] = path.stem
    guide['path'] = path.relative_to(here)
    guide['content'] = content.strip()

    guides[guide['name']] = guide


# --------------------------------------------------------------------------------------------------

# Prepare templating:
env = Environment(loader=FileSystemLoader(str(here)))

def render(src: Path, dst_root: Path, dst_rel: Path):
    now = round(time.time() * 1000)
    src = src.relative_to(here)
    dst = dst_root / dst_rel

    content = env.get_template(str(src)).render(root = dst_root, guides = guides)

    # Save backup for existing files (if changed):
    if dst.exists():
        old_content = dst.read_text()

        if content != old_content:
            bak = Path(dst_root, 'backup', str(dst_rel) + f".{now}")
            bak.parent.mkdir(parents=True, exist_ok=True)
            bak.write_text(dst.read_text())

    # Replace file:
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(content)

@pass_context
def ref(ctx, name):
    return f"`{Path(ctx['root'], guides[name]['path']).resolve()}`"

@pass_context
def embed(ctx, name):
    return guides[name]['content'] + '\n'

env.globals['ref'] = ref
env.globals['embed'] = embed


# --------------------------------------------------------------------------------------------------

# Parse command line arguments:
parser = argparse.ArgumentParser(description='Install LLM School resources to AI agent configuration directories')
parser.add_argument('--install-claude', action='store_true', help='Install to Claude Code')
parser.add_argument('--install-qwen', action='store_true', help='Install to Qwen Code')
parser.add_argument('--install-opencode', action='store_true', help='Install to OpenCode')
args = parser.parse_args()

# Require at least one flag
if not (args.install_claude or args.install_qwen or args.install_opencode):
    parser.error('At least one installation flag must be provided: --install-claude, --install-qwen, or --install-opencode')


# --------------------------------------------------------------------------------------------------

# Install to Qwen:
if args.install_qwen:
    render(Path(here, 'PROMPT.md'), qwen, Path('QWEN.md'))
    for path in here.glob('agents/*.md'): render(path, qwen, Path('agents', path.name))
    for path in here.glob('guides/*.md'): render(path, qwen, Path('guides', path.name))

# Install to Claude:
if args.install_claude:
    render(Path(here, 'PROMPT.md'), claude, Path('CLAUDE.md'))
    for path in here.glob('agents/*.md'): render(path, claude, Path('agents', path.name))
    for path in here.glob('guides/*.md'): render(path, claude, Path('guides', path.name))

# Install to OpenCode:
if args.install_opencode:
    render(Path(here, 'PROMPT.md'), opencode, Path('AGENTS.md'))
    for path in here.glob('agents/*.md'): render(path, opencode, Path('agent', path.name))
    for path in here.glob('guides/*.md'): render(path, opencode, Path('guides', path.name))

