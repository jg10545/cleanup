"""

        __init__.py
        
WHAT DOES THIS DO?

If you install this package, then when you call "import cleanup" in python, 
it'll run this file. So you can use __init__.py to choose how your user sees
any functions or classes in your package.

Say you've got another file in this directory called foo.py, and it has a 
function bar() that your users will need. Then there's a couple ways you
could add it here:
    
One option would be to add "import cleanup.foo" to this file. Then when
a user imports cleanup, they can access bar() at cleanup.foo.bar().

Another option would be to add "from cleanup.foo import bar" to this file.
Then when a user imports cleanup, they can access bar() at cleanup.bar().

A final option is not to add anything here, in which case foo.py doesn't
get automagically imported when you import cleanup. Your user would run
"import cleanup.foo" in their code.

You need to have an __init__.py for python to recognize the directory as a
module, but strictly speaking you don't have to have anything inside it. 

"""

from cleanup.load import load_and_preprocess
from cleanup.model import random_forest_embeddings
from cleanup.plot import build_embedding_figure