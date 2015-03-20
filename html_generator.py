def generate_concept_HTML(content):
    full_html_text = ""
    for each_item in content:
        i = 0
        title = each_item[0]
        nav_tag = '"' +  each_item[0]  + '"'
        desc = each_item[1]
        html_text_1 = '''
    <a id= ''' + nav_tag
        html_text_2 = '''></a> 
    <p class="subtitle">''' + title
        html_text_3 = '''</p>
        <p class="notes">
        ''' + desc
        html_text_4 = '''
        </p>'''
        full_html_text =  full_html_text + html_text_1 + html_text_2 + html_text_3+ html_text_4
    return full_html_text



content = [('Python','''Python is a programming language. When code writtein in Python is executed, Python interpreter converts the code into set of instructions. 
    Since computers are dumb, code that you write has to be granatically correct in Python language.'''),
('Functions','''Functions are block of code that is self contained.  It takes some input, does processing based on instructions provided in the code, 
    and return some output.  Function block starts wiht "def" key word followed by function name and "()" which can contain variables.'''),
('Strings','''Strings are created when you enclose characters in quotes.  Strings can be manipulated in Python using various built in functions like: '''
    '''find, len, [] with index number for getting substring'''),
('Structures', '''Data structures basiclly hold related data. Python has different types of data structures that include lists, tuples, dictionaries, etc. <br />
    Lists contain orderd items and can contain values of any type.  Lists are also mutable which means they can be modified. 
    Some list operators are "append", "+" and "len".
    * append- is a method that adds an element at the end of a list.  Syntax for append is <list>.append(<element>).<br />
    * '+'  takes two lists and produces new list combining elements from both lists.  It does not mutate the list.<br />
    * 'len' is another list operator that gives number of elements in a list.<br />
    * 'index' - finds the position of a value in a list'''),
('Loops','''Loops are usefull when you want to execute same code until certain condition is met.  Using Loop reduces repeated code.  
     Loops can be exited by using 'break' statement.  Break statement resumes code at next statement in your block.  
     Other statements like 'pass' and 'continue' are also used to exit a loop. The two main types of loop are as follows:<br />
    *  while loop - run the code while a condition is true.<br />
    *  for loop  - runs the code multiple times.''')]



print generate_concept_HTML(content)