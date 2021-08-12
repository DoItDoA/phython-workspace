import inspect
import random
print(inspect.getfile(random)) # random 모듈의 위치

from travel import thailand
print(inspect.getfile(thailand)) # thailand 모듈의 위치