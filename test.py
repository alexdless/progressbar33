from progressbar33 import ProgressBar

import time

pbar = ProgressBar(maxval=10)

pbar.start()

for i in range(1, 11):

    pbar.update(i)

    time.sleep(1)

pbar.finish()