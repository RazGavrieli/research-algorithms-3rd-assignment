from lastcall import *
  
@lastcall
def f(x: int):
    return x**2

@lastcall
def g(x: int, y:int):
    return x + y

@lastcall
def bfs(start, end, neighbor_function):
    return breadth_first_search(start=start, end=end, neighbor_function=neighbor_function)

if __name__ == "__main__":
    #print(g(3,4), g(3, y=4), g(y=4, x=3), g(x=3, y=4))
    #print(f(3), f(4), f(x=3), f(3))
    print(bfs(start=(2,2), end=(-35,-3), neighbor_function=lattice_graph_w))
    print()
    bfs(start=(2,2), end=(-35,-3), neighbor_function=lattice_graph_w)