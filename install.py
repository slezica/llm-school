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
from glob import glob
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, TemplateNotFound, pass_context


# Define roots:
home = Path.home()
here = Path(__file__).parent # home != here :(

qwen = Path(home, '.qwen')
claude = Path(home, '.claude')
opencode = Path(home, '.config/opencode')


# Collect guides:
guides = {}
for path in here.glob('guides/*.md'):
    _, frontmatter, content = path.read_text().split('---\n', 2)

    guide = yaml.safe_load(frontmatter)
    guide['name'] = path.stem
    guide['path'] = path.relative_to(here)
    guide['content'] = content.strip()

    guides[guide['name']] = guide


# Prepare templating:
env = Environment(loader=FileSystemLoader(str(here)))

def render(src: Path, dst_root: Path, dst_rel: Path):
    src = src.relative_to(here)
    dst = dst_root / dst_rel

    content = env.get_template(str(src)).render(root = dst_root, guides = guides)

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


# Render prompt:
path = Path(here, 'PROMPT.md')
render(path, qwen, Path('QWEN.md'))
render(path, claude, Path('CLAUDE.md'))
render(path, opencode, Path('AGENTS.md'))

# Render agents:
for path in here.glob('agents/*.md'):
    render(path, qwen, Path('agents', path.name))
    render(path, claude, Path('agents', path.name))
    render(path, opencode, Path('agent', path.name))

# Render guides:
for path in here.glob('guides/*.md'):
    render(path, qwen, Path('guides', path.name))
    render(path, claude, Path('guides', path.name))
    render(path, opencode, Path('guides', path.name))

