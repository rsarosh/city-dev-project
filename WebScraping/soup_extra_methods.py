from bs4 import Tag
import warnings

'''
@input 
    tag: tag to get attributes of (type Tag)
    attr: attribute to get from tag (type Dict)
@output
    the attribute of the tag, without throwing any errors
'''
def safe_attr_access(tag, attr):
    if tag.has_attr(attr):
        return tag[attr]
    else:
        return -1

'''
@input  
    tag: starting tag (type Tag)
    [optional] tag_name: specific tag name to find (type String)
    [optional] len: amount of tags to go through before choosing (type Int)
    [optional] err_handle: how to handle errors (type String)
                'throw': throws errors, stopping the program
                'ignore': ignores error, and returns -1
@output 
    the next tag in the script that matches specified requirements (type Tag)
'''
def next_tag(tag, tag_name=-1, len=1, err_handle='throw'):
    next_option = tag.nextSibling

    for i in range(len):
        if i > 0:
            next_option = next_option.nextSibling
        num = 0
        while (not isinstance(next_option, Tag)) or (tag_name != -1 and next_option.name != tag_name):
            num += 1
            if err_handle == 'throw':
                next_option = next_option.nextSibling
            elif err_handle == 'ignore':
                try:
                    next_option = next_option.nextSibling
                except AttributeError:
                    return -1
            else:
                warnings.warn('INPROPER TAG NAME "'+err_handle+'"')
            if num > 20:
                warnings.warn('NO TAG FOUND AT ' + tag.toText())
                break
    return next_option

'''
[applies to both find and find_all]
@input
    tag_name: the tag to find
    container: what HTML to search within (if you want all, use 'soup')
    [optional] attrs: specific attributes to search for
@output
    first tag that matches all of the specifications, of the form
    container.find(tag_name, attrs) 
'''
def find(tag_name, container, attrs={}):
    tag = container.find(tag_name, attrs)
    if tag:
        return tag
    else:
        warnings.warn("COULD NOT FIND TAG " + tag_name +" IN CONTAINER " + container.name + " WITH ATTRIBUTES " + str(attrs))
        return -1

def find_all(tag_name, container, attrs={}):
    tags = container.find_all(tag_name, attrs)
    if tags:
        return tags
    else:
        warnings.warn("COULD NOT FIND TAGS " + tag_name +" IN CONTAINER " + container.name + " WITH ATTRIBUTES " + str(attrs))
    return -1

'''
@input  
    main_div: outer div to search within
@output
    list of divs within the first layer of the main div
'''
def surface_search(main_div):
    divs = main_div.find_all('div', recursive=False)

    while len(divs) == 1: # Account for random 'middle' divs, for example: <div> <random middle div> <subdiv 1> <subdiv2> <subdiv3>
        divs = divs[0].find_all('div', recursive=False)

    return divs

def format_string(txt):
    txt = txt.strip()  # strip leading/ending whitespace
    txt = txt.replace('   ', '')  # 3 spaces becomes none
    txt = txt.replace('  ', ' ')  # 2 spaces becomes 1
    txt = txt.replace('\n', '')  # remove newlines
    txt = txt.replace('\t', '')  # remove tabs
    return txt