import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for v in range(0, int(value)):
        self.contents.append(key)

  def draw(self, dn):
    dropped = []
    if dn < len(self.contents):
      for n in range(0, dn):
        rand = random.randrange(0, len(self.contents))
        dropped.append(self.contents[rand])
        self.contents.pop(rand)
    return dropped


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  hat1 = copy.deepcopy(hat)
  M = 0
  for n in range(0, num_experiments):
    dropped = hat1.draw(num_balls_drawn)
    cnt = {d: dropped.count(d) for d in dropped}

    is_subset = all(key in cnt and cnt[key] >= value
                    for key, value in expected_balls.items())
    if is_subset:
      M += 1
    hat1 = copy.deepcopy(hat)

  return float(M / num_experiments) if M != 0 else 1
