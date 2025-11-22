import json
import nbformat
import re

def split_markdown_by_heading(text: str):
    """
    Split text into chunks where each chunk starts with a markdown heading.
    """
    lines = text.splitlines()
    chunks = []
    current_chunk = []

    for line in lines:
        if re.match(r"^\s*#{1,6}\s+", line):
            # New heading: start a new chunk
            if current_chunk:
                chunks.append("\n".join(current_chunk).strip())
            current_chunk = [line]
        else:
            current_chunk.append(line)

    if current_chunk:
        chunks.append("\n".join(current_chunk).strip())

    # Remove empty chunks
    return [c for c in chunks if c]

def chatgpt_json_to_ipynb(json_file: str, output_ipynb: str):
    """
    Convert a ChatGPT JSON session to a Jupyter notebook.
    Only code blocks starting with ```python are converted to code cells.
    Other text becomes markdown cells.
    Each heading (#, ##, ###) starts a new markdown cell.
    """
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    nb = nbformat.v4.new_notebook()
    cells = []

    def traverse(node_id):
        node = data["mapping"][node_id]
        msg = node.get("message")
        if msg and msg.get("author", {}).get("role") == "assistant":
            parts = msg.get("content", {}).get("parts", [])
            for part in parts:
                if not part.strip():
                    continue

                # Pattern to find ```python code blocks```
                pattern = re.compile(r"(.*?)```python\n(.*?)```", re.DOTALL)
                last_end = 0
                for m in pattern.finditer(part):
                    # Text before code block -> markdown
                    before = m.group(1).strip()
                    if before:
                        chunks = split_markdown_by_heading(before)
                        for chunk in chunks:
                            cells.append(nbformat.v4.new_markdown_cell(chunk))
                    # Code block -> code cell
                    code = m.group(2).strip()
                    if code:
                        cells.append(nbformat.v4.new_code_cell(code))
                    last_end = m.end()

                # Any remaining text after last code block
                remaining = part[last_end:].strip()
                if remaining:
                    chunks = split_markdown_by_heading(remaining)
                    for chunk in chunks:
                        cells.append(nbformat.v4.new_markdown_cell(chunk))

        # Recurse into children
        for child_id in node.get("children", []):
            traverse(child_id)

    traverse("client-created-root")

    nb["cells"] = cells

    with open(output_ipynb, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print(f"Notebook saved to {output_ipynb}")