''' A module is an external library that is available to us to import it to use its content in our code.
That way, we don't need to write the desired functionality fro scratch.

Regex or Regular Expressions are strings or expressions that, if met certain conditions, they allow some condition executions.
'''

import re
string = "'I AM NOT YELLING', she said. Though we know this was not true."

# Patter = re.sub('[expression to match]', 'substitution', variable)
# Creating a pattern for substituting the capital letters [A-Z] for blank space ''
new = re.sub('[A-Z]', '', string)
print(new)

# We could do the same thing but for the lowercase letters
# new = re.sub('[a-z]', '', string)

