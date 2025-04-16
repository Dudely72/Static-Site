


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag                #string representing html tag name
        self.value = value            #string representing value of html tag
        self.children = children      #list of html nodes that are children of this node
        self.props = props            #dictionary of key-value pairs that represent attributes of html tag

    def __eq__(self, other):          #used for testing the equality of two nodes
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    
    def to_html(self):                #overridden by child classes
        raise NotImplementedError
    
    def props_to_html(self):          #converts props to html
        if self.props != None:
            prop_string = ""
            for p in self.props:
                prop_string += ' ' + p + '="' + self.props[p] + '"'
            return prop_string
    
    def __repr__(self):               #used to debug
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"

class LeafNode(HTMLNode):             #child node with no children, purely tag and value with optional props
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    
    def to_html(self):                #converts leaf tag/value to html
        if self.value == None:
            raise ValueError("LeafNode requires a value")
        if self.tag == None:          #returns raw text if given no tag
            return self.value        
        return f"<{self.tag}{self.props_to_html() or ''}>{self.value}</{self.tag}>" #works whether props are present or not, returns HTML

        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode requires a tag")
        if not self.children:
            raise ValueError("children list is required")
        opening_tag = f"<{self.tag}{self.props_to_html() or ''}>"
        children_html = ''.join(child.to_html() for child in self.children)  #recursive call for each child
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{children_html}{closing_tag}"