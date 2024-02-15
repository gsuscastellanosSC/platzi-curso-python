import matplotlib.pyplot as plt

labels = ['A', 'B', 'C'] 
values = [200, 34, 120]
def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.savefig('pie.png')
  plt.close()