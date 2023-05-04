import random
class dogs:
  def __init__(self, name):
      self.name = name
      self.gladness = 50
      self.respect = 0
      self.alive = True

  def guard(self):
      print("Ти повинен гавкати на всіх собак, що проходять повз!")
      self.gladness -= 10
      self.respect += 0.5

  def to_sleep(self):
      print("Тобі треба поспати.")
      self.gladness += 3


  def to_chill(self):
      print("Вільний час.")
      self.gladness += 5
      self.respect -= 0.2


  def is_alive(self):
      if self.respect <-0.5:
          print("Тебе ні одна собака не поважає:(")
          self.alive = False
      elif self.gladness <= 0:
          print("На жаль, ти витратив свій час...")
          self.alive = False
      elif self.respect > 5:
          print("Тебе всі собаки поважають!")
          self.alive = False

  def end_of_day(self):
      print(f"Gladness = {self.gladness}")
      print(f"Respect = {round(self.respect,2)}")

  def live(self, day):
      day = "Day" + str(day) + "of" + self.name + "live"
      print(f"{day:=^50}")
      live_cube = random.randint(1,3)
      if live_cube == 1:
        self.guard()
      elif live_cube == 2:
          self.to_sleep()
      elif live_cube == 3:
          self.to_chill()

      self.end_of_day()
      self.is_alive()

dog = dogs(name="Пушок")

for day in range(365):
    if dog.alive == False:
        break
    dog.live(day)