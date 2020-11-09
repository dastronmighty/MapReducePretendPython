# MapReducePretendPython

### Have you ever thought "MapReduce is Great I wish theyd make it worse"

Look No further I put together this because trying to wrap your head around how map reduce works can be a nightmare
and its alot of hassel to download HDP or spin up a server to try it out so I implemented a terrible class in Python
that functions as the Map Reduce backend.
All you gotta do to use it is:

```Python
from MapReduce import MapReduce

class MyMapReduceClass(MapReduce):
  def __init__(self):
    super().__init__()

  def Map(self, v):
    # your code for the Mapper

  def Reduce(self, k, v):
    # your code for the reducer

```

Don't ask why I didn't name the methods "Mapper" and "Reducer" I just didn't okay
Same Idea though


## If you want to see how it works theres some examples in /examples

note: I was too lazy to implement a matrix class so I used NumPy in the MatrixMultiplication example
