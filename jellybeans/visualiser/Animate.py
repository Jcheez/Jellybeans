from typing import Callable
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import matplotlib.animation as anim

def Show(lst:list, callable:Callable, speed:float = 0.5, sortKey:Callable = lambda x:x) -> None:
    '''
    A function to visualise sorting animations
    Args: 
        lst: Takes in a list 
        callable: Sorting function 
        Speed: Animation in seconds (Default 0.5 seconds)
        sortKey: sort by what (Default original value)
    '''
    epochs = [-2]
    frames = list(callable(lst, animate=True, key=sortKey))
    fig, ax = plt.subplots()
    texts = []

    def add_labels(lst):
        for i in range(len(lst)):
            texts.append(plt.text(i, lst[i], lst[i], ha = 'center'))

    def remove_labels(lst):
        for frame in lst:
            Artist.remove(frame)
        lst.clear()

    def update_plot(x, rec, epochs, frames):
        remove_labels(texts)
        epochs[0] += 1
        for rec, val in zip(rec, x):
            rec.set_height(val)
        add_labels(frames[epochs[0]])

    bar_rec = ax.bar(range(len(lst)), frames[0], align='center')
    add_labels(frames[0])
    _ = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs, frames), frames=frames, interval=speed*1000, repeat=False)
    plt.show()

def Print(lst:list, callable:Callable, sortKey:Callable = lambda x:x) -> None:
    '''
    A function to print the current state of list after every iteration
    Args: 
        lst: Takes in a list 
        callable: Sorting function 
        sortKey: sort by what
    '''
    for i in callable(lst, visualise=True, key=sortKey):
        print(i)