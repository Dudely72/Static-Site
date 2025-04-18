from enum import Enum
import re

def markdown_to_blocks(markdown_text: str) -> list[str]:       #splits raw markdown text into blocks
    lines = markdown_text.strip().split("\n")
    blocks = []
    current_block = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            current_block.append(line)
            continue

        if stripped == "" and not in_code_block:
            if current_block:
                blocks.append("\n".join(current_block).strip())
                current_block = []
            continue

        if not in_code_block and re.match(r"^#{1,6} ", stripped):
            if current_block:
                blocks.append("\n".join(current_block).strip())
                current_block = []
            blocks.append(stripped)
            continue

        current_block.append(line)
        
    if current_block:
        blocks.append("\n".join(current_block).strip())

    return blocks


class BlockType(Enum):
    paragraph = "PARAGRAPH"
    heading = "HEADING"
    code = "CODE"
    quote = "QUOTE"
    unordered_list = "UNORDERED"
    ordered_list = "ORDERED"

def block_to_block_type(block):            #returns blocktype given a block
    stripped = block.strip()
    if stripped.startswith("#"):
        return BlockType.heading
    elif stripped.startswith("```") and stripped.endswith("```"):
        return BlockType.code
    lines = block.split("\n")              # the rest of these have to be analyzed line by line
    if all(line.strip().startswith(">") for line in lines):
        return BlockType.quote
    if all(line.strip().startswith("- ") for line in lines):
        return BlockType.unordered_list
    is_ordered = True
    for i, line in enumerate(lines):       # gives index and content fot each line
        expected_prefix = f"{i + 1}. "     # sets expected prefix to be "number. "
        if not line.strip().startswith(expected_prefix):
            is_ordered = False
            break
    if is_ordered:                         # as long as whole list is ordered correctly, returns ordered list type
        return BlockType.ordered_list
    return BlockType.paragraph             # if none of the above, returns paragraph type
        