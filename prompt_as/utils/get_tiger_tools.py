from upsonic import Tiger


the_tiger_tools = None

def get_tiger_tools():
    return []
    global the_tiger_tools
    if the_tiger_tools == None:
        the_tiger_tools = Tiger().crewai(prefix="interpreter")
        
    return the_tiger_tools
