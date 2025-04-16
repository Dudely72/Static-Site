


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag                #string representing html tag name
        self.value = value            #string representing value of html tag
        self.children = children      #list of html nodes that are children of this node
        self.props = props            #dictionary of key-value pairs that represent attributes of html tag

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props != None:
            prop_string = ""
            for p in self.props:
                prop_string += ' ' + p + '="' + self.props[p] + '"'
            return prop_string
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        elif self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"