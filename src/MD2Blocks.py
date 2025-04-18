from enum import Enum

def markdown_to_blocks(markdown_text):       #splits raw markdown text into blocks
    blocks = markdown_text.split("\n\n")     #splits based on double \n
    results = []
    for block in blocks:
        stripped = block.strip()             #strips all leading and trailing whitespace
        if len(stripped) != 0:
            results.append(stripped)         #if string is not empty, add to list
    return results


class BlockType(Enum):
    paragraph = "PARAGRAPH"
    heading = "HEADING"
    code = "CODE"
    quote = "QUOTE"
    unordered_list = "UNORDERED"
    ordered_list = "ORDERED"

def block_to_block_type(block):            #returns blocktype given a block
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.heading
    elif block.startswith("```") and block.endswith("```"):
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
        