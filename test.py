import unittest

class ScoringSystem:
  def __init__(self):
      self.score = 0

  def correct_answer(self):
      self.score += 1

  def get_score(self):
      return self.score

class TestScoringSystem(unittest.TestCase):
  def setUp(self):
      self.scoring_system = ScoringSystem()

  def test_correct_answer(self):
      self.scoring_system.correct_answer()
      self.assertEqual(self.scoring_system.get_score(), 1)

  def test_multiple_correct_answers(self):
      self.scoring_system.correct_answer()
      self.scoring_system.correct_answer()
      self.assertEqual(self.scoring_system.get_score(), 2)

class Worm:
 def __init__(self):
     self.body = [(0, 0)]

 def move_up(self):
     self.body.insert(0, (self.body[0][0], self.body[0][1] - 1))
     self.body.pop()

 def move_down(self):
     self.body.insert(0, (self.body[0][0], self.body[0][1] + 1))
     self.body.pop()

 def move_left(self):
     self.body.insert(0, (self.body[0][0] - 1, self.body[0][1]))
     self.body.pop()

 def move_right(self):
     self.body.insert(0, (self.body[0][0] + 1, self.body[0][1]))
     self.body.pop()

class TestWorm(unittest.TestCase):
 def setUp(self):
     self.worm = Worm()

 def test_move_up(self):
     self.worm.move_up()
     self.assertEqual(self.worm.body[0], (0, -1))

 def test_move_down(self):
     self.worm.move_down()
     self.assertEqual(self.worm.body[0], (0, 1))

 def test_move_left(self):
     self.worm.move_left()
     self.assertEqual(self.worm.body[0], (-1, 0))

 def test_move_right(self):
     self.worm.move_right()
     self.assertEqual(self.worm.body[0], (1, 0))


if __name__ == '__main__':
  unittest.main()
