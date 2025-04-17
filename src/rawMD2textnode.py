from textnode import TextNode, TextType




def split_nodes_delimiter(old_nodes, delimiter, text_type): #takes list of old nodes, delimiter, and text type
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.normal_text:      #if the text type isn't normal text, add to list as is
            new_nodes.append(old_node)
            continue                                        #tells program to skip processing for rest of the loop if condition is met
        
        text = old_node.text
        
        start_index = text.find(delimiter)                  #finds index of first occurence of delimiter
        if start_index == -1:
            new_nodes.append(old_node)                      #if index is -1, no delimiter found, add to list as is
            continue                                        #tells program to skip processing for rest of the loop if condition is met
        
        end_index = text.find(delimiter, start_index + len(delimiter)) #finds index of next occurence of delimiter
        if end_index == -1:                                 #if end index isn't found raise an exception
            raise Exception(f"no closing delimiter '{delimiter}' found")
        
        before_delim = text[:start_index]                   #text from [0] to start index
        between_delim = text[start_index + len(delimiter):end_index] #text from where first delimiter is found to where last delimiter is found
        after_delim = text[end_index + len(delimiter):]     #text from after delimiter

        if before_delim:
            new_nodes.append(TextNode(before_delim, TextType.normal_text))  #adds string before delim as normal text
        new_nodes.append(TextNode(between_delim, text_type))       #adds special text as requested type

        if after_delim:
            remaining_node = TextNode(after_delim, TextType.normal_text)  #sets remaining text as a text node
            result_nodes = split_nodes_delimiter([remaining_node], delimiter, text_type)  #runs recursively on remaining node
            new_nodes.extend(result_nodes)                                #extends new node list with all result nodes

    return new_nodes
