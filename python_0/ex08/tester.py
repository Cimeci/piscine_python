from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

import sys

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()

if len(sys.argv) == 2 and sys.argv[1] == "--doc":
    print(tqdm.__doc__)
    print()
    print(ft_tqdm.__doc__)
